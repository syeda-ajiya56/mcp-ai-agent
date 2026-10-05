# MCP-Powered AI Student Assistant

A simple AI agent that uses **Model Context Protocol (MCP)** to connect Google Gemini with external student and course tools.

## Project Overview

This project demonstrates how an AI agent can:

1. Connect to an MCP server.
2. Discover available MCP tools.
3. Understand a user's request.
4. Select the appropriate tool or tools.
5. Call those tools through MCP.
6. Receive the tool results.
7. Present the results to the user.

## Architecture

```text
User
  ↓
Gemini AI Agent
  ↓
MCP Client
  ↓
MCP Server
  ↓
Student / Course Tools
  ↓
Tool Results
  ↓
Final Response
```

## MCP Tools

The MCP server provides three tools:

### 1. `get_student_info`

Returns basic academic information for a student.

**Example student ID:**

```text
STU-101
```

### 2. `get_course_info`

Returns information about a university course.

**Example course ID:**

```text
CS-401
```

### 3. `get_student_result`

Returns a student's result summary, including GPA and academic standing.

## Example Multi-Tool Request

**User request:**

```text
Give me Ayesha Khan's student information and also tell me about Artificial Intelligence.
```

The AI agent selected two MCP tools:

```text
get_student_info
get_course_info
```

The MCP server executed both tools and returned their results successfully.

## Technologies

- Python
- FastMCP
- Model Context Protocol (MCP)
- Google Gemini API
- python-dotenv

## Running the Project

### 1. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Create a `.env` file

Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=your_api_key_here
```

### 3. Start the MCP server

```bash
python server.py
```

### 4. Run the AI agent

Open another terminal, activate the virtual environment, and run:

```bash
python agent.py
```

## Project Demonstration

The project demonstrates:

- MCP server running successfully
- MCP tool discovery
- AI agent connection to the MCP server
- Successful single-tool execution
- Successful multi-tool workflow
- Tool results returned from the MCP server

## Learning Outcome

This project demonstrates the basic **MCP architecture** and shows how an AI agent can discover and use external tools through an MCP server.
