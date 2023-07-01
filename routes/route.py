from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile
import uuid
from models.todos import Todo, Admin
from config.database import collection_name, collection_adm
from schema.schemas import list_serial, list_adm
from bson import ObjectId
from fastapi.responses import StreamingResponse
import io

router = APIRouter()

@router.get("/todos")
async def get_todos():
    todos = list_serial(collection_name.find().sort("name"))
    return todos

#post request metodo
@router.post("/todos")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))

#put request metodo
@router.put("/{id}")
async def put_todo(id:str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})

#delete request metodo
@router.delete("/{id}")
async def delete_todo(id:str):
    collection_name.delete_one({"_id": ObjectId(id)})


@router.post("/uploadfile/")
async def post_upload_file(file: UploadFile = File(...), rarity: str = "", name: str = "", value: int = 0):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    file_data = {
        "filename": file.filename,
        "contents": contents,
        "rarity": rarity,
        "name": name,
        "value": value
    }
    collection_name.insert_one(file_data)
    return {}

@router.get("/image/{id}")
async def get_image(id: str):
    file_data = collection_name.find_one({"_id": ObjectId(id)})
    if file_data is None:
        return {"error": "File not found"}
    contents = file_data["contents"]
    return StreamingResponse(io.BytesIO(contents), media_type="image/jpeg")

#put request metodo
@router.put("/image/{id}")
async def put_image(id:str, rarity: str = "", name: str = "", value: int = 0):
    file_data = collection_name.find_one({"_id": ObjectId(id)})
    if file_data is None:
        return {"error": "File not found"}
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"rarity": rarity, "name": name, "value": value}})
    return {}

#delete request metodo
@router.delete("/image/{id}")
async def delete_image(id:str):
    file_data = collection_name.find_one({"_id": ObjectId(id)})
    if file_data is None:
        return {"error": "File not found"}
    collection_name.delete_one({"_id": ObjectId(id)})
    return {}


@router.get("/adm")
async def get_adm():
    Admin = list_adm(collection_adm.find())
    return Admin

#post request metodo
@router.post("/adm")
async def post_adm(adm: Admin):
    collection_adm.insert_one(dict(adm))

#put request metodo
@router.put("/adm/{id}")
async def put_adm(id:str, adm: Admin):
    collection_adm.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(adm)})

#delete request metodo
@router.delete("/adm/{id}")
async def delete_adm(id:str):
    collection_adm.delete_one({"_id": ObjectId(id)})

