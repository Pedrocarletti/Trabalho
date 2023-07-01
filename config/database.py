from pymongo import MongoClient


client = MongoClient("mongodb+srv://pedro:pedro@cluster0.lo2qxc0.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collection"]

collection_adm = db["admin_collection"]

collection_skin = db["skin_collection"]

