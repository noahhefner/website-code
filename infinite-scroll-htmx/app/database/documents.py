from motor.motor_asyncio import AsyncIOMotorClient
import pymongo

client = AsyncIOMotorClient("localhost", 27017)
db = client["infinite-scroll-demo"]
doc_collection = db["infinite-scroll-documents"]

async def search_content (query, limit, skip):
    """ Search for a query. """

    collection_filter = {"content": {"$regex": query, "$options": "i"}}
    cursor = doc_collection.find(filter = collection_filter, skip = skip, sort = [("title", 1)])
    return await cursor.to_list(length = limit)

async def get_content(filename):
    """ Get contents of a document by filename. """

    doc = await doc_collection.find_one({'title': filename})
    if (doc):
        return doc["content"]
    else:
        return None
