from fastapi import FastAPI
from fastapi_app.api import products, search, payments




#app = FastAPI()
app = FastAPI(title="Ecommerce FastAPI")

app.include_router(products.router, prefix="/products")
app.include_router(search.router, prefix="/search")

app.include_router(payments.router, prefix="/payments")
