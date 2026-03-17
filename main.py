from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.structure import CodeSnippet
from services.analyser import analyze_code
from services.llm import explain_code

app = FastAPI()
templates = Jinja2Templates(directory="views")

# index page
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# endpoint to receive code snippet and return analysis and explanation
@app.post("/submit")
async def submit(snippet: CodeSnippet):
    
    if not snippet.code.strip():
        return {"error": "Code snippet cannot be empty."}

    analysis = analyze_code(snippet.code)

    response = explain_code(snippet.code, analysis)

    return response