import requests
from openai import tool

@tool
def get_student_info(student_id: str) -> dict:
    """
    Retrieves student info from FastAPI backend using student ID.
    """
    url = f"http://localhost:8000/students/{student_id}"
    response = requests.get(url)
    return response.json()
