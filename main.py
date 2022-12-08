import os
from server.grpc.grpc import run
from service.api import SportsBettingService
from storage.mysql.mysql import MySQLStorage
from storage.mongo.mongo import MongoStorage
from storage.mysql.functions import auto_create, get_instance

if __name__ == '__main__':
    auto_create()

    db = get_instance()
    mongo_db = os.environ['DATABASE_LOCAL']

    # bet_storage = MySQLStorage(db)
    bet_storage = MongoStorage(mongo_db)

    sports_service = SportsBettingService(bet_storage)

    run(sports_service)
