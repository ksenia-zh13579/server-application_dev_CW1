from pydantic import BaseModel, computed_field, field_validator, Field
import re

# Task 1.4
class User(BaseModel):
    id: int
    name: str

# Task 1.5
class User2(BaseModel):
    name: str
    age: int

    @computed_field
    def is_adult(self) -> bool:
        return self.age >= 18

# Task 2.1 - 2.2   
class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50, description="Имя должно иметь от 2 до 50 символов")
    message: str = Field(min_length=10, max_length=500, description="Сообщение должно иметь от 10 до 500 символов")

    @field_validator('message', mode='after')
    def validate_message(cls, v):
        if re.search(r"(\bкринж[а-я]{,2}\b)|(\bвайб[а-я]{,2}\b)|(\bрофл[а-я]{,2}\b)", v):
            raise ValueError("Использование недопустимых слов")
        else:
            return v
