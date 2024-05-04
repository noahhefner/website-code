import os
import time
from fastapi import Request
from fastapi.responses import FileResponse
from app import templates
from app.router import router

@router.get("/")
async def serve_root(request: Request):

    return templates.TemplateResponse(request=request, name="pages/root.html")

@router.get("/favicon.ico")
async def get_favicon():
    
    return FileResponse("static/favicon.ico", media_type='application/octet-stream')
