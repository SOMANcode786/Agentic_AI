from fastapi import FastAPI

app = FastAPI()

# Mock database
students = {
    "1": {"name": "Ali", "age": 21},
    "2": {"name": "Ahmed", "age": 22},
    "3": {"name": "Sana", "age": 20}
}

@app.get("/students/{student_id}")
def get_student(student_id: str):
    return students.get(student_id, {"error": "Student not found"})

@app.get("/")
def root():
    return {"message": "Student API is running"}
