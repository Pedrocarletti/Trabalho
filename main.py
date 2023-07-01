from fastapi import FastAPI, File, UploadFile   
import uuid

from routes.route import router
app = FastAPI()

app.include_router(router)

