from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from pydantic import EmailStr

from database import get_database_connection

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    password: hash 

# @app.post("/users")
# async def create_user(user: User):
#     # save user to database
#     connection = get_database_connection()
#     cursor = connection.cursor()
#     query = "INSERT INTO users (name, email) VALUES (%s, %s)"
#     values = (user.name, user.email)
#     cursor.execute(query, values)
#     connection.commit()
#     connection.close()
#     return {"message": "user created successfully"}

@app.post("/users")
async def create_user(user: User):
    if not user.email.endswith("@gmail.com"):
        raise HTTPException(status_code=400, detail="Email must be @gmail.com")
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (user.name, user.email)
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
    query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    values = (user.name, user.email, user_id)
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


# adding code for email validation and error handling


# Run the application
# uvicorn main:app --reload
# The --reload flag will automatically reload the server when you make changes to the code.