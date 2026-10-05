from fastmcp import FastMCP

mcp = FastMCP(
    "Student MCP Server",
    instructions="Provides student academic information through MCP tools."
)

STUDENTS = {
    "STU-101": {
        "name": "Ayesha Khan",
        "program": "Computer Science",
        "semester": 4,
        "gpa": 3.72,
    },
    "STU-102": {
        "name": "Hamza Khan",
        "program": "Software Engineering",
        "semester": 3,
        "gpa": 3.45,
    },
    "STU-103": {
        "name": "Sara Ahmed",
        "program": "Information Technology",
        "semester": 5,
        "gpa": 3.88,
    },
}

COURSES = {
    "CS-401": {
        "name": "Artificial Intelligence",
        "department": "Computer Science",
        "credits": 3,
        "description": "Introduction to artificial intelligence concepts and applications.",
    },
    "CS-402": {
        "name": "Database Systems",
        "department": "Computer Science",
        "credits": 3,
        "description": "Fundamentals of relational databases, SQL, and database design.",
    },
    "SE-301": {
        "name": "Software Engineering",
        "department": "Software Engineering",
        "credits": 3,
        "description": "Software development processes, requirements, design, and testing.",
    },
}


@mcp.tool
def get_student_info(student_id: str) -> dict:
    """Get academic information for a student using their student ID."""
    student = STUDENTS.get(student_id.upper())

    if not student:
        return {
            "error": f"Student ID {student_id} was not found."
        }

    return student


@mcp.tool
def get_course_info(course_id: str) -> dict:
    """Get information about a university course using its course ID."""
    course = COURSES.get(course_id.upper())

    if not course:
        return {
            "error": f"Course ID {course_id} was not found."
        }

    return course


@mcp.tool
def get_student_result(student_id: str) -> dict:
    """Get a student's result summary including GPA and academic standing."""
    student = STUDENTS.get(student_id.upper())

    if not student:
        return {
            "error": f"Student ID {student_id} was not found."
        }

    gpa = student["gpa"]

    if gpa >= 3.7:
        standing = "Excellent"
    elif gpa >= 3.0:
        standing = "Good"
    else:
        standing = "Needs Improvement"

    return {
        "student_id": student_id.upper(),
        "name": student["name"],
        "gpa": gpa,
        "academic_standing": standing,
    }


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)