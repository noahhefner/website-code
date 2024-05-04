from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.router import docs, root, search

app = FastAPI()

app.include_router(docs.router)
app.include_router(root.router)
app.include_router(search.router)
