from pydantic import BaseModel, conint, constr
from typing import Optional

# class Users(BaseModel):
#     id: int
#     name: str
#     email: str
#     age: int

# user = Users(id=1 , name="Lis", email="lis@gmail.com", age=17)
# print(user)

class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    age: Optional[int] = None

user1 = User(id=1 , name="Lis", email="lis@gmail.com", age=17)
print(user1)

user2 = User(id=2 , name="Darsej", email="darsej@gmail.com")
print(user2)

user3 = User(id=3 , name="Darsej")
print(user3)

class another_user(BaseModel):
    id:conint(gt-0) # <0
    name: constr(min_length=2, max_length=50)

valid_user = another_user(id=1, name="Lis")
print(valid_user)

valid_user1 = another_user(id=0, name="Lis")