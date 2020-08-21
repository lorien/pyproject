from pymongo import MongoClient

from project.config import config


def init_db():
    conn = MongoClient(**config['mongodb']['connection'])
    return conn[config['mongodb']['dbname']]


db = init_db()
