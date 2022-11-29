from abc import ABC, abstractmethod
from models.models import  SportBet, CreateBetRequest, CreateBetResponse
from typing import Dict, Tuple

class SportsBettingInterface(ABC):
    @abstractmethod
    def create(self, data: CreateBetRequest) -> CreateBetResponse:
        pass

    # @abstractmethod
    # def read(self, data):
    #     ...

    # @abstractmethod
    # def update(self, data):
    #     ...

    # @abstractmethod
    # def delete(self, data):
    #     ...

class StorageInterface(ABC):
    @abstractmethod
    def create_bet(self, bet: SportBet) -> Tuple[int, str]:
        pass