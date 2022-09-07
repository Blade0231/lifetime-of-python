import strawberry
from typing import List

@strawberry.type
class User:
    name: str
    age: int

@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> List[User]:
        res = [User(name="Patrick", age=100),
            User(name="Vaibhav", age=24)]
        
        return res

schema = strawberry.Schema(query=Query)