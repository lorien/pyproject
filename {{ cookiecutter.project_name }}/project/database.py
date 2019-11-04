from pymongo import MongoClient

from project.settings import MONGODB


def init_db():
    conn = MongoClient(**MONGODB['connection'])
    return conn[MONGODB['dbname']]


db = init_db()
