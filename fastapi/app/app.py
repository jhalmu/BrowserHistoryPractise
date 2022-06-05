# Importing FastApi class
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

# The data
from app.browserdata import df, aika, osoite

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

# May the force be with API!
app = FastAPI()

api_router = APIRouter()


app.mount("/static", StaticFiles(directory=str(BASE_PATH / "static")), name="static")

templates = Jinja2Templates(directory="../templates")

# Default route
@app.get("/", status_code=200)
def root(request: Request) -> dict:
    """
    Root GET
    """
    return TEMPLATES.TemplateResponse("index.html",
    {"request": request, "data": df, "aika": aika, "osoite": osoite}
    )


@app.get("/api", status_code=200)
def get_API() -> dict:
    """
    Api GET
    """
    return {"data": df}
    


app.include_router(api_router)
    