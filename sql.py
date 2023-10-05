from sqlmodel import SQLModel, Session, create_engine, Field, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.engine import URL
import asyncio

engine = create_engine("sqlite:///database.db", echo=True, future=True)
async_engine = create_async_engine("sqlite+aiosqlite:///database.db", echo=True, future=True)
class Users(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    age: int
    email: str
    password: str

SQLModel.metadata.create_all(engine)

async def create(name, age, email, password):
    async with AsyncSession(async_engine) as session:
        user = Users(name=name, age=age, email=email, password=password)
        session.add(user)
        await session.commit()
        await session.close()
    
async def read():
    async with AsyncSession(async_engine) as session:
        statement = select(Users)
        users = await session.execute(statement)
        for user in users:
            print(user)
   
async def update(id, name):
    async with AsyncSession(async_engine) as session:
        statement = select(Users).where(Users.id == id)
        users = await session.execute(statement)
        user = users.one()
        user[0].name = name
        await session.commit()
        await session.close()

async def delete(id):
    async with AsyncSession(async_engine) as session:
        statement = select(Users).where(Users.id == id)
        users = await session.execute(statement)
        user = users.one()
        session.delete(user[0])
        await session.commit()
        await session.close()

asyncio.run(create(name="John", age=50, email="john@example.com", password="random123"))
# asyncio.run(read())
asyncio.run(update(1, "John Doe"))
# asyncio.run(read())
# delete(4)
# delete(5)
asyncio.run(delete(21))
# asyncio.run(read())
