import pytest
from unittest import mock
import pymongo
import mongomock
from service.api.api import SportsBettingService

class Helpers:
    @staticmethod
    def sport_bet_api(storage):
        client = SportsBettingService(storage)
        return client
    

@pytest.fixture
def helpers():
    return Helpers

@pytest.fixture
def db_name(request):
    service = request.config.getoption('--service')
    return service

@pytest.fixture
@mock.patch('storage.mysql.mysql.MySQLStorage')
def storage(mock_mysql, db_name):
    print(db_name)
    if db_name == 'mysql':
        return mock_mysql
    
def pytest_addoption(parser):
    parser.addoption(
        "--service", action="store", default="mysql"
    )

@pytest.fixture(scope="session")
def mongo_conn():
    myclient = pymongo.MongoClient("mongodb://0.0.0.0:27017/")

    yield myclient
    myclient.drop_database('testdb')

@pytest.fixture()
def mongo_mock():
    client = mongomock.MongoClient()
    return client



