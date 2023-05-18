from urllib import request
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI
from typing import Union
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

class Text(BaseModel):
    text: str

app = FastAPI()
# Press the green button in the gutter to run the script.
@app.get('/hello')
def readRoot():
    return "hello"

@app.post('/sentiment')
async def checkSentiment(text:Text):
    doc=nlp(text.text)
    return doc._.polarity
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
