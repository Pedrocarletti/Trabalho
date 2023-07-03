from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile, Depends
import uuid
from models.todos import Todo, Admin, Skin
from config.database import collection_name, collection_adm, collection_skin
from schema.schemas import list_serial, list_adm, list_filedatas
from bson import ObjectId
from fastapi.responses import StreamingResponse
import io
from fastapi import Form, HTTPException

from logins.loginadm import verify_password, criar_token_jwt
import functools
from fastapi import Depends, FastAPI, HTTPException, status
rarity = {
  "legendary": 2, 
  "epic": 1, 
  "rare": 0
}

def compare(x, y):
   return rarity[x.get("rarity")]-rarity[y.get("rarity")]

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



async def current_user(username: str = Form(...), password: str = Form(...)):
    user = collection_adm.find_one({"username": username})

    if not user or not password == user["password"]:
        raise HTTPException(status_code=403,
                            detail="Email ou nome de usuário incorretos"
                           )
    return current_user

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = collection_adm.find_one({"username": username})

    if not user or not password == user["password"]:
        raise HTTPException(status_code=403,
                            detail="Email ou nome de usuário incorretos"
                           )
    return {
        "access_token": criar_token_jwt(user["_id"]),
        "token_type": "bearer",
    }
@router.post("/skin/")
async def skin(current_user: collection_adm = Depends(current_user) , file: UploadFile = File(...), rarity: str = "", name: str = "", value: int = 0):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    file_data = {
        "filename": file.filename,
        "contents": contents,
        "rarity": rarity,
        "name": name,
        "value": value
    }
    collection_skin.insert_one(file_data)
    return {}

@router.get("/skin/rarity")
async def get_skin():
    file_data = list_filedatas(collection_skin.find())
    file_data = sorted(file_data, key=functools.cmp_to_key(compare))
    
    return file_data

@router.get("/skin/value")
async def get_skin():
    file_data = list_filedatas(collection_skin.find().sort("value"))
    return file_data


#put request metodo
@router.put("/image/{id}")
async def put_image(id:str, rarity: str = "", name: str = "", value: int = 0):
    file_data = collection_skin.find_one({"_id": ObjectId(id)})
    if file_data is None:
        return {"error": "File not found"}
    collection_skin.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"rarity": rarity, "name": name, "value": value}})
    return {}


#delete request metodo
@router.delete("/image/{id}")
async def delete_image(id:str):
    file_data = collection_skin.find_one({"_id": ObjectId(id)})
    if file_data is None:
        return {"error": "File not found"}
    collection_skin.delete_one({"_id": ObjectId(id)})
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

