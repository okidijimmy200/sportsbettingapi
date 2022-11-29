from server.grpc.grpc import run
from service.api import SportsBettingService
from storage.mysql.mysql import MySQLStorage
from storage.mysql.functions import auto_create, get_instance

if __name__ == '__main__':
    auto_create()

    db = get_instance()

    bet_storage = MySQLStorage(db)

    sports_service = SportsBettingService(bet_storage)

    run(sports_service)
