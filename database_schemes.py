from pydantic import BaseModel,Field

class User(BaseModel):
    username:str = Field(regex="^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$")
    email :str =Field()
    password:str =Field(regex="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")

class Story(BaseModel):
    title:str = Field(max_length=100)
    description:str = Field(max_length=200)

class Block(BaseModel):
    body :str = Field(max_length=2000)
    