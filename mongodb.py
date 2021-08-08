import pymongo
#password removed for purpose
client = pymongo.MongoClient(f"mongodb+srv://archit:<password>t@cluster0.n4nbh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
data_collection = db.blog

def insert_data(posts):
        try:
                data_collection.insert_many(posts)
        except:
                print("Error While inserting")

# for i in data_collection.find():
#         print(i)

# d = data_collection.delete_many({'Active_Drug': 'XTPara 650mg Tablet'})
# print(d.deleted_count)
