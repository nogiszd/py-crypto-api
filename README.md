# py-crypto-api ![example workflow](https://github.com/nogiszd/py-crypto-api/actions/workflows/test.yml/badge.svg)
Super simple Python API for fetching cryptocurrency exchange rate via Google Search.<br />
Written with [FastAPI](https://fastapi.tiangolo.com/) and scraping via [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## Installation
Firstly you need to install dependencies `pip install -r requirements.txt`.<br />
To host API you need to run it with `uvicorn --reload main:app` (the default port is `8000`).<br />
(the `--reload` switch is optional)<br />

Testing and development was taken on Python 3.10.

## Usage

|URL| Description | Output |
|--|--|--|
|`localhost:8000/v1/{query}`  | Replace `{query}` with search phrase,<br />for e.g. "1 btc to usd" |Outputs JSON formatted response e.g. `{"amount":"9.9"}`<br />where `9.9` is amount of USD for 1 Bitcoin|

*You can use Swagger UI to visualize everything via `localhost:8000/docs`*

