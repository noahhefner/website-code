"""
Endpoint for a document page.

When a filename is requested, fetch the contents of that document from the
MongoDB database.
"""

import re
from fastapi import Request
from app import templates
from app.router import router
from app.database import documents

VALID_FILENAME_PATTERN = re.compile(r'^[a-zA-Z0-9_-]+$')

@router.get("/docs/{filename}")
async def serve_content_page(filename: str, request: Request):
    """ Document page. """

    # Check for invalid filename characters
    filename_ok = bool(VALID_FILENAME_PATTERN.match(filename))
    if (not filename_ok):
        return templates.TemplateResponse(request=request, name="pages/400.html", status_code=404)

    content = await documents.get_content(filename)
    if (content):
        context = {
            "filename": filename,
            "content": content
        }
        return templates.TemplateResponse(request=request, name="pages/content.html", context=context)
    else:
        return templates.TemplateResponse(request=request, name="pages/404.html", status_code=404)
