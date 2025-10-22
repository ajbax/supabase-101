## Main file

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routes import car_routes

app = FastAPI()

#Mounting the static files dir
app.mount("/static", StaticFiles(directory="app/static"), name="static")

#Setting up the templates dir
templates = Jinja2Templates(directory="app/templates")

#Including the car routes
app.include_router(car_routes.router, prefix="/cars", tags=["cars"])
