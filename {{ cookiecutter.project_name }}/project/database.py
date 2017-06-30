from pymongo import MongoClient

from project.settings import MONGODB

db = MongoClient(**MONGODB['connection'])[MONGODB['dbname']]
