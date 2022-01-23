from fastapi import FastAPI, HTTPException
import requests, json
from Scrape import Scrape

app = FastAPI()

@app.on_event("startup")
def startup():
    f = open("structure.json")
    data = f.read()
    f.close()
    
    global elements_to_scrape
    elements_to_scrape = json.loads(data)

@app.get("/")
def root():
    return {"hello":"world"}

@app.get("/v1/{symbol}/")
def get_data(symbol: str):
    fetched_data = {}
    
    try:
        s = Scrape(symbol, elements_to_scrape)
        if s.summary():
            fetched_data = s.summary()  
        else:
            raise HTTPException(status_code=400, detail=f"{symbol} query is empty")
    except requests.TooManyRedirects:
        raise HTTPException(status_code=404, detail=f"{symbol} doesn't exist or cannot be found")
    except requests.HTTPError:
        raise HTTPException(status_code=500, detail="An error has occurred while processing the request.")
    
    return fetched_data