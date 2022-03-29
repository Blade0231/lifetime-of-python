from fastapi import FastAPI
import fastapi
import uvicorn

from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from api import weather_api
from views import home
from services import open_weather_service 

api = FastAPI()


def configure():
    configure_routing()
    configure_api_key()

def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)

def configure_api_key():
    from dotenv import load_dotenv
    import os

    load_dotenv()

    open_weather_service.api_key = os.environ.get('secret')

if __name__=="__main__":
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()
