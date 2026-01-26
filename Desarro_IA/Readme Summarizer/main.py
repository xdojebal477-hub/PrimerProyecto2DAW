from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from transformers import pipeline
from models import SummaryRequest

app=FastAPI()
print("⏳ Cargando modelo distilbart... esto puede tardar la primera vez.")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
print("IA lista.")


@app.post("/api/summarize")
async def summarize(request: SummaryRequest):

    print("==============================# Peticion recibida #==============================")
    
    prediction = summarizer(request.text, max_length=130, min_length=30, do_sample=False, truncation=True)#generamos el resumen, le metemos trucate para que no pete con textos largos
    
    print("==============================# Resumen generado #==============================")
    return {"summary": prediction[0]['summary_text']}


app.mount("/", StaticFiles(directory="static", html=True), name="static")