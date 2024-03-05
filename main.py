from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from pydantic import EmailStr
from passlib.context import CryptContext

from database import get_database_connection

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr
    password: str 


# adding password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
 
@app.post("/users")
async def create_user(user: User):
    if not user.email.endswith("@gmail.com"):
        raise HTTPException(status_code=400, detail="Email must be @gmail.com")
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    values = (user.name, user.email, pwd_context.hash(user.password))
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "user created successfully"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    values = (user_id,)
    cursor.execute(query, values)
    user = cursor.fetchone()
    connection.close()
    return {"id": user[0], "name": user[1], "email": user[2]}

@app.get("/users")
async def get_users():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    connection.close()
    return users

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s"  # Removed the comma before WHERE
    values = (user.name, user.email, pwd_context.hash(user.password), user_id)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "user updated successfully"}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM users WHERE id = %s"
    values = (user_id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "user deleted successfully"}



# Run the application
# uvicorn main:app --reload
# The --reload flag will automatically reload the server when you make changes to the code.
# pip install "passlib[bcrypt]"      useful for password hashing in the application
# useful for email validation in the application pip install pydantic[email]