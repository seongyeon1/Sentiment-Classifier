from fastapi import FastAPI
from .model import router

app = FastAPI()
app.include_router(router.router, prefix="/api")

# from fastapi import FastAPI, Request, Form
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from transformers import pipeline
#
# app = FastAPI()
#
# templates = Jinja2Templates(directory="templates")
#
# pipe = pipeline("text-classification", model="seongyeon1/klue-base-finetuned-nsmc")
#
# @app.get("/", response_class=HTMLResponse)
# async def read_form(request: Request):
#     return templates.TemplateResponse("form.html", {"request": request, "result": None})
#
# @app.post("/", response_class=HTMLResponse)
# async def submit_form(request: Request, text: str = Form(...)):
#     result = pipe(text)[0]
#     return templates.TemplateResponse("form.html", {"request": request, "result": result})
