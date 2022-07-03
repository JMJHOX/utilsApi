
from pydantic import BaseModel


class Weather(BaseModel):
    country: str
    temperature: str
    description: str

class Currency(BaseModel):
    coin: str
    skip: str
    limit: str