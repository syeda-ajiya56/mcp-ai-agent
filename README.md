\# MCP-Powered AI Student Assistant



A simple AI agent that uses Model Context Protocol (MCP) to connect Gemini with external student and course tools.



\## Project Overview



This project demonstrates how an AI agent can:



1\. Connect to an MCP server.

2\. Discover available MCP tools.

3\. Understand a user's request.

4\. Select the appropriate tool or tools.

5\. Call those tools through MCP.

6\. Receive the tool results.

7\. Present the results to the user.



\## Architecture



```text

User

&#x20; ↓

Gemini AI Agent

&#x20; ↓

MCP Client

&#x20; ↓

MCP Server

&#x20; ↓

Student / Course Tools

&#x20; ↓

Tool Results

&#x20; ↓

Final Response

```



\## MCP Tools



The MCP server provides three tools.



\### 1. get\_student\_info



Returns basic academic information for a student.



Example student ID:



```text

STU-101

```



\### 2. get\_course\_info



Returns information about a university course.



Example course ID:



```text

CS-401

```



\### 3. get\_student\_result



Returns a student's result summary including GPA and academic standing.



\## Example Multi-Tool Request



User request:



```text

Give me Ayesha Khan's student information and also tell me about Artificial Intelligence.

```



The AI agent selected two MCP tools:



```text

get\_student\_info

get\_course\_info

```



The MCP server executed both tools and returned their results successfully.



\## Technologies



\- Python

\- FastMCP

\- Model Context Protocol (MCP)

\- Google Gemini API

\- python-dotenv



\## Running the Project



Install the required packages:



```bash

pip install -r requirements.txt

```



Create a `.env` file in the project folder:



```text

GEMINI\_API\_KEY=your\_api\_key\_here

```



Start the MCP server:



```bash

python server.py

```



Then open another terminal, activate the virtual environment, and run:



```bash

python agent.py

```



\## Project Demonstration



The project demonstrates:



\- MCP server running successfully

\- MCP tool discovery

\- AI agent connection to the MCP server

\- Successful single-tool execution

\- Successful multi-tool workflow

\- Tool results returned from the MCP server



\## Learning Outcome



This project demonstrates the basic MCP architecture and shows how an AI agent can discover and use external tools through an MCP server.

