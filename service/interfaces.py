from abc import ABC, abstractmethod
from models.models import  SportBet, CreateBetRequest, CreateBetResponse, ReadBetRequest, ReadBetResponse
from typing import Dict, Tuple

class SportsBettingInterface(ABC):
    @abstractmethod
    def create(self, data: CreateBetRequest) -> CreateBetResponse:
        pass

    @abstractmethod
    def read(self, data: ReadBetRequest) -> ReadBetResponse:
        pass

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

    @abstractmethod
    def read_bet(self, data: ReadBetRequest) -> ReadBetResponse:
        pass