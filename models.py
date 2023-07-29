
from pydantic import BaseModel


# TODO: create migration
class User(BaseModel):
    Id: str
    Email: str
    Password: str

    



class UserLogin(BaseModel):
    Email: str
    Password: str

    


