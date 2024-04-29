from unittest import result
from fastapi import FastAPI, requests
from pydantic import BaseModel
import deepl
from requests import request, jsonify

from app import traductor

app = FastAPI()

class TraductorRequest(BaseModel):
    translate_text: str
    target_lang: str


@app.route("/", methods=[ 'GET'])
async def root():
    return {"message": "Hello World"}


@app.route('/traductor', methods=[ 'POST'])
async def traductor_func(translate_text, target_lang):
    auth_key = "a4341cbe-a8bd-4ac2-97e4-6bce2574cf8a:fx"
    translator = deepl.Translator(auth_key)
    translate_text = request .get_json()
    target_lang = traductor.target_lang
    response = requests.post()

    if response.status_code != 200:
        translate_text = traductor(translate_text)
        target_lang = traductor(target_lang)

        return jsonify({"data": result.text})

