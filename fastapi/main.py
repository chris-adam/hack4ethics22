from fastapi import FastAPI
from pytz import country_names
from models.product import *
import uvicorn
import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/product")
async def get_products(country):
    return get_all_products(country_name=country)

@app.get("/product/{product_name}")
async def get_person(product_name: str):
    product = Product(product_name=product_name, decision=datetime.date.today(), expiration_date=datetime.date.today())
    return {"product_name": product.product_name, 
            "decision": product.decision, 
            "expiration_date": product.expiration_date}

if __name__ == '__main__':
    uvicorn.run("main:app",  host="0.0.0.0", port=8000, reload=True, debug=False)
