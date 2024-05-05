import os
import time
from fastapi import Request, Query
from app import templates
from app.router import router
from app.database import documents
import time

@router.get("/search")
async def serve_search_results(request: Request, query: str = Query(None), limit: int = Query(10, ge=0), skip: int = Query(0, ge=0)):

    results = await documents.search_content(query, limit, skip)

    matches = []

    for result in results:

        doc_info = {
            "title": result['title'],
            "description": result['description'],
            "url": "/docs/{}".format(result["title"])
        }

        matches.append(doc_info)

    context = {
        "matches": matches,
        "query": query,
        "limit": limit,
        "skip": skip
    }

    return templates.TemplateResponse(request = request, name = "searchResults.html", context = context)
