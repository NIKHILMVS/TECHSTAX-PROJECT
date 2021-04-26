import json
from pymongo import MongoClient
client=MongoClient("mongodb+srv://nikhil:<personalpassword>@flipkart.iivz3.mongodb.net/<dbname>?retryWrites=true&w=majority")

db=client["nikhil"]
collection=db["techstax"]

path=r'D:\Techstax'

def uploadJSONToMongo(jsonname):
    fpath=path+"\\"+jsonname
    fh=open(fpath).read()
    jobject= json.loads(fh)
    if isinstance(jobject, list): 
        collection.insert_many(jobject)   
    else: 
        collection.insert_one(jobject) 
def executeUpload():
    uploadJSONToMongo("techstax.json")
if __name__=="__main__":
    executeUpload()
