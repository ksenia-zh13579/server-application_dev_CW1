from fastapi import FastAPI
from app.models import *

app = FastAPI()

feedback_list = []

# Task 1.3
@app.post("/calculate")
def post_result(num1, num2):
    return {"result": f"{float(num1) + float(num2)}"}

#Task 1.4
user = User(id=1, name="Ksenia Zhuzhleva")

@app.get("/users")
def read_user():
    return user

# Task 1.5
@app.post("/user")
def post_user2(user2 : User2):
    return user2

# Task 2.1 - 2.2
@app.post("/feedback")
def post_feedback(feedback : Feedback):
    feedback_list.append(feedback.model_dump())
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}