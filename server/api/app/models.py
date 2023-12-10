from sqlmodel import SQLModel, Field

class Hero(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    age: int
