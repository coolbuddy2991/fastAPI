#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

from pymongo import MongoClient
from model import Todo

client = MongoClient('mongodb+srv://Saurabh2991:batista_2991@cluster1.fliglis.mongodb.net/')
database = client.TodoList
collection = database.todo

async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    for document in cursor:
        await todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True