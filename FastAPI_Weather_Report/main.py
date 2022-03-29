from fastapi import FastAPI
from sklearn.covariance import fast_mcd
import uvicorn

api = FastAPI()

@api.get('/')
def index():
    return "Hello Weather App"


if __name__=="__main__":
    uvicorn.run(api, port=8000, host='127.0.0.1')
