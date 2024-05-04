from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("localhost", 27017)
db = client["infinite-scroll-demo"]
doc_collection = db["infinite-scroll-documents"]

async def search_content (search_input, offset, limit):
    """ Search for a query. """

    query = {"content": {"$regex": search_input, "$options": "i"}}
    cursor = doc_collection.find(query).skip(offset).limit(limit)
    return await cursor.to_list(length=limit)

async def get_content(filename):
    """ Get contents of a document by filename. """

    doc = await doc_collection.find_one({'title': filename})
    if (doc):
        return doc["content"]
    else:
        return None
