import os
import time
from fastapi import Request, Query
from app import templates
from app.router import router
from app.database import documents

@router.get("/search")
async def serve_search_results(request: Request, search_input: str = Query(None, alias="search_input"), skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)):

    print("searching for - " + search_input)

    results = await documents.search_content(search_input, skip, limit)

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
        "skip": skip,
        "limit": limit,
        "search_input": search_input
    }

    return templates.TemplateResponse(request=request, name="searchResults.html", context=context)
