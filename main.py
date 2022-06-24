from fastapi import FastAPI, HTTPException, Query, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, PlainTextResponse
import requests, json
from Scrape import Scrape

app = FastAPI()

@app.on_event("startup")
def startup():
    structure = '{"elements": [{"from": "[class=\'BNeawe iBp4i AP7Wnd\']","to": "amount"}]}'
    
    global elements_to_scrape
    elements_to_scrape = json.loads(structure)

@app.get("/")
def root():
    return {"hello":"world"}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    x = exc.errors()
    for i in x:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=jsonable_encoder({"detail": str(i["loc"][1]) +" "+ str(i["msg"])}),
        )

@app.get("/v1/{symbol}/")
def get_data(symbol: str):
    fetched_data = {}
    
    try:
        s = Scrape(1, symbol, elements_to_scrape)
        if s.summary():
            fetched_data = s.summary()  
        else:
            raise HTTPException(status_code=400, detail=f"{symbol} query is empty")
    except requests.TooManyRedirects:
        raise HTTPException(status_code=404, detail=f"{symbol} doesn't exist or cannot be found")
    except requests.HTTPError:
        raise HTTPException(status_code=500, detail="An error has occurred while processing the request.")
    
    return fetched_data

@app.get("/v2/")
def get_data(crypto: str, currency: str):
    fetched_data = {}
    
    try:
        symbols = [crypto, currency]
        s = Scrape(2, symbols, elements_to_scrape)
        if s.summary():
            fetched_data = s.summary()
        else:
            raise HTTPException(status_code=400, detail="query is empty")
    except requests.TooManyRedirects:
        raise HTTPException(status_code=404, detail=f"resource doesn't exist or cannot be found")
    except requests.HTTPError:
        raise HTTPException(status_code=500, detail="An error has occurred while processing the request.")
    
    return fetched_data