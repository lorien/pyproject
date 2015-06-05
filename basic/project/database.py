from pymongo import MongoClient
from project.settings import MONGODB_CONNECTION, MONGODB_NAME

db = MongoClient(**MONGODB_CONNECTION)[MONGODB_NAME]
