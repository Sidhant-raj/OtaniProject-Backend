from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import Ocr, uuid

app = FastAPI()
IMAGEDIR = "images/"

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslatingItems(BaseModel):
    UpdateLanguage: str
    TargetLanguage: str
    ImageName: str


@app.post('/UploadImages/')
async def upload_file(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.png"
    contents = await file.read()

    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    return {"filename": file.filename}


@app.post('/translate')
async def Translating_endpoint(item: TranslatingItems):
    translated_texts, sentence = Ocr.StarterFunction(item.UpdateLanguage, item.TargetLanguage, item.ImageName)
    return {
        "Originaltext": str(sentence),
        "Translatedtext": str(translated_texts)
    }