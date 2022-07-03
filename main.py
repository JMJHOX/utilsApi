
from typing import Union
from models import model 
from utils import util
from constants import constant as prefix
from fastapi import FastAPI
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




@app.get("/")
def read_root():
    return "Welcome to weatherAPI"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/weather/{country}", tags=[prefix.Tags.weather])
async def update_item(country: str):
    url_api = "https://goweather.herokuapp.com/weather/" + country
    print(url_api)
    get_response = await util.slow_route(url_api)
    return get_response

@app.get("/weatherStyle/{country}",response_model= model.Weather,tags=[prefix.Tags.weather])
async def update_item(country: str):
    url_api = "https://goweather.herokuapp.com/weather/" + country
    get_response  = await util.slow_route(url_api)
    return {
    "country": country, 
    "temperature": get_response['temperature'],
    "description": get_response['description']
    }

@app.post("/coin",tags=[prefix.Tags.coin])
async def update_item(currency: model.Currency):
    url_api = "https://api.coinstats.app/public/v1/coins?skip={}&limit={}&{}".format(currency.skip, currency.limit, currency.coin)
    get_response  = await util.slow_route(url_api)
    return get_response

@app.get("/coffe",tags=[prefix.Tags.random])
async def update_item():
    url_api = "https://coffee.alexflipnote.dev/random.json"
    get_response  = await util.slow_route(url_api)
    return get_response
