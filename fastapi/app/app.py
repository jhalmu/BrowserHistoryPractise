# Importing FastApi class
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.middleware.wsgi import WSGIMiddleware
#import dash

from app.dashboard import dapp

# The data
from app.browserdata import df, aika, osoite

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

# May the force be with API!
app = FastAPI()

app.mount("/dash", WSGIMiddleware(dapp.server))
#api_router = APIRouter()

app.mount("/static", StaticFiles(directory=str(BASE_PATH / "static")), name="static")
templates = Jinja2Templates(directory="../templates", auto_reload=True)


@app.get("/dash/")
def index() -> dict:
    """
    Dashboard GET
    """
    return {"data": df[:101]}

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
    return {"data": df[:101]}
    