from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

# Replace 'your_database_name' with the actual database name you want to use or created in Atlas
db = client['resumes']

collection = db['parsed_data']  # collection name you choose