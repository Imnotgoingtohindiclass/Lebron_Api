from fastapi import FastAPI
import json
import random
import datetime

app = FastAPI()

with open("quotes.json", "r") as file:
    data = json.load(file)

def get_daily_quote():
    today = datetime.date.today()
    random.seed(today.toordinal())
    quote_id = str(random.randint(1, 60))
    return {"id": quote_id, "quote": data.get(quote_id, "Quote not found")}

@app.get("/")
def read_root():
    return {"message": "Welcome to the LeBron Quotes API! IT'S OUR BALL AINT IT? ITS OUR BALL"}

@app.get("/daily-quote")
def daily_quote():
    return get_daily_quote()

@app.get("/quote/{quote_id}")
def get_quote(quote_id: str):
    return {"id": quote_id, "quote": data.get(quote_id, "Quote not found")}

@app.get("/quotes")
def get_all_quotes():
    return data
