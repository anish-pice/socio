import uuid

import bcrypt
import jwt
import uvicorn
from fastapi import FastAPI

from constants import *
from database import *
from models import User
from queries import *

app = FastAPI()


@app.get("/")
def ServerUp(): 

    return {"response": "Hellow World"}


@app.post("/signup")
def signup(requestDto: UserLogin):
    
    userModel = User
    userModel.Email = requestDto.Email
    userModel.Id = uuid.uuid1()

    print(requestDto)
    userModel.Password = bcrypt.hashpw(requestDto.Password, salt)
    cur.execute("INSERT INTO users VALUES(%s,%s,%s)",
                userModel.Id, userModel.Email, userModel.Password)

    # encoded_jwt = jwt.encode({"userId": "payload"},
    #                          "secret", algorithm="HS256")

    return {"Hello": "World"}


@app.post("/signin")
def signin(UserLoginModel: UserLogin):
    query = FetchUserByEmail.Values(UserLoginModel.Email)
    userModelDb = fetchUsers(query)

    hash = bcrypt.hashpw(userModelDb.Password, salt)

    result = bcrypt.checkpw(userModelDb.Password, hash)

    if result:
        # do something
        # Fetch all the data from db
        return {"User loggedin"}

    else:
        return {"user not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000,  log_level="info", reload=True)
