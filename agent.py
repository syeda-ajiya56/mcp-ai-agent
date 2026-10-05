import asyncio
import json
import os

from dotenv import load_dotenv
from fastmcp import Client
from google import genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from the .env file.")

gemini = genai.Client(api_key=GEMINI_API_KEY)

MCP_SERVER_URL = "http://127.0.0.1:8000/mcp"
MODEL = "gemini-3.7-flash"


def clean_schema(schema):
    if not isinstance(schema, dict):
        return schema

    cleaned = {}

    for key, value in schema.items():
        if key in ("additionalProperties", "additional_properties"):
            continue

        cleaned[key] = clean_schema(value)

    return cleaned


async def get_mcp_tools(client):
    tools_result = await client.list_tools()

    tools = []

    for tool in tools_result:
        schema = getattr(tool, "input_schema", None)

        if schema is None:
            schema = getattr(tool, "inputSchema", None)

        tools.append(
            {
                "name": tool.name,
                "description": tool.description or "",
                "parameters": clean_schema(schema),
            }
        )

    return tools


async def call_mcp_tool(client, tool_name, arguments):
    return await client.call_tool(
        tool_name,
        arguments=arguments,
    )


async def run_agent(user_request):

    async with Client(MCP_SERVER_URL) as mcp_client:

        print("\n[Agent] Connected to MCP server.")

        tools = await get_mcp_tools(mcp_client)

        print("[Agent] Available MCP tools:")

        for tool in tools:
            print(f"  - {tool['name']}")

        function_declarations = [
            {
                "name": tool["name"],
                "description": tool["description"],
                "parameters": tool["parameters"],
            }
            for tool in tools
        ]

        system_instruction = """
You are an AI Student Assistant connected to an MCP server.

You MUST use MCP tools whenever the user asks for student,
academic, result, GPA, or course information.

Known students:
- Ayesha Khan = STU-101
- Hamza Khan = STU-102
- Sara Ahmed = STU-103

Known courses:
- Artificial Intelligence = CS-401
- Database Systems = CS-402
- Software Engineering = SE-301

If the user mentions a student or course by name,
use the appropriate MCP tool instead of asking for an ID.

If the user asks for multiple pieces of information,
use multiple MCP tools when appropriate.
"""

        response = gemini.models.generate_content(
            model=MODEL,
            contents=user_request,
            config={
                "system_instruction": system_instruction,
                "tools": [
                    {
                        "function_declarations": function_declarations
                    }
                ],
            },
        )

        function_calls = response.function_calls

        if not function_calls:
            print("\n[Agent] No tool was needed.")
            print("\nFinal response:")
            print(response.text)
            return

        tool_results = []

        print("\n[Agent] Tool calls selected by Gemini:")

        for function_call in function_calls:

            tool_name = function_call.name
            arguments = dict(function_call.args)

            print(
                f"  -> {tool_name}("
                f"{json.dumps(arguments, ensure_ascii=False)}"
                f")"
            )

            result = await call_mcp_tool(
                mcp_client,
                tool_name,
                arguments,
            )

            print(f"\n[MCP] Result from {tool_name}:")
            print(result)

            tool_results.append(
                {
                    "name": tool_name,
                    "arguments": arguments,
                    "result": result,
                }
            )

        print("\nFinal response:")

        for item in tool_results:

            result = item["result"]

            if "get_student_info" in item["name"]:
                print("\nStudent Information:")
                print(result)

            elif "get_course_info" in item["name"]:
                print("\nCourse Information:")
                print(result)

            elif "get_student_result" in item["name"]:
                print("\nStudent Result:")
                print(result)


async def main():

    print("=" * 60)
    print("MCP-Powered AI Student Assistant")
    print("=" * 60)

    user_request = input(
        "\nEnter your request:\n> "
    )

    await run_agent(user_request)


if __name__ == "__main__":
    asyncio.run(main())
