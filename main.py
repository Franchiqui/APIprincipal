from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.traductor import traductor_func
from app.video import video_func

app = FastAPI()

class TraductorRequest(BaseModel):
    translate_text: str
    target_lang: str

@app.get("/video")
def video():
    return video_func()

@app.post("/traductor")
async def traductor_endpoint(request: Request, traductor_data: TraductorRequest):
    translate_text = traductor_data.translate_text
    target_lang = traductor_data.target_lang
    traduccion = traductor_func(translate_text, target_lang)
    return {"data": traduccion}

