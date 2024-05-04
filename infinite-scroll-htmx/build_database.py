from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("localhost", 27017)
db = client["infinite-scroll-demo"]
doc_collection = db["infinite-scroll-documents"]

def main():

    for i in range(500):

        document = {
            "title": "Document " + str(i),
            "description": "Description " + str(i),
            "content": "Content of document " + str(i)
        }

        doc_collection.insert_one(document)

if __name__ == "__main__":

    main()
