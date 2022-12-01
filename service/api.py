from service.interfaces import SportsBettingInterface, StorageInterface
from models.models import (
    CreateBetRequest, 
    CreateBetResponse, 
    SportBet, 
    ReadBetRequest, 
    ReadBetResponse, 
    UpdateBetRequest, 
    UpdateBetResponse,
    DeleteBetRequest,
    DeleteBetResponse
)

class SportsBettingService(SportsBettingInterface):
    def __init__(self, storage: StorageInterface) -> None:
        self.storage = storage

    def create(self, data: CreateBetRequest) -> CreateBetResponse:
        try:
            code, response = self.storage.create_bet(SportBet(
                id=None,
                league=data.league,
                home_team=data.home_team,
                away_team=data.away_team,
                home_team_win_odds=data.home_team_win_odds,
                away_team_win_odds=data.away_team_win_odds,
                draw_odds=data.draw_odds,
                game_date=data.game_date
            )
                )
            if code != 200 and code != 201:
                return CreateBetResponse(400, response)

            return CreateBetResponse(code , response)

        except Exception as e:
            result = (
                f"-Failed to store data in MYSQL DB, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            return CreateBetResponse(500, result)

    def read(self, data: ReadBetRequest) -> ReadBetResponse:
        try:
            code, response, reason = self.storage.read_bet(ReadBetRequest(
                league=data.league,
                start_date=data.start_date,
                end_date = data.end_date
            ))
            if code != 200:
                return ReadBetResponse(400, None, reason)
            
            return ReadBetResponse(code, response, reason)
        except Exception as e:
            result = (
                f"-Failed to read data from MYSQL DB, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            return ReadBetResponse(500, '', result)

    
    def update(self, data: UpdateBetRequest) -> UpdateBetResponse:
        try:
            code, response = self.storage.update_bet(SportBet(
                id=data.id,
                league=data.league,
                home_team=data.home_team,
                away_team=data.away_team,
                home_team_win_odds=data.home_team_win_odds,
                away_team_win_odds=data.away_team_win_odds,
                draw_odds=data.draw_odds,
                game_date=data.game_date
            )
                )
            if code != 200 and code != 201:
                return UpdateBetResponse(400, response)

            return UpdateBetResponse(code , response)

        except Exception as e:
            result = (
                f"-Failed to store data in MYSQL DB, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            return UpdateBetResponse(500, result)

    def delete(self, data: DeleteBetRequest) -> DeleteBetResponse:
        new_date = data.game_date.split()[0]
        try:
            code, reason = self.storage.delete_bet(DeleteBetRequest(
                league=data.league,
                home_team=data.home_team,
                away_team = data.away_team,
                game_date = new_date
            ))
            if code != 204:
                return DeleteBetResponse(400, reason)
            
            return DeleteBetResponse(code, reason)
        except Exception as e:
            result = (
                f"-Failed to delete data from MYSQL DB, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            return DeleteBetResponse(500, '', result)
