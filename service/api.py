from service.interfaces import SportsBettingInterface, StorageInterface
from models.models import CreateBetRequest, CreateBetResponse, SportBet

class SportsBettingService:
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
            print(code)
            if code != 200 and code != 201:
                return CreateBetResponse(400, response)

            return CreateBetResponse(code , response)

        except Exception as e:
            result = (
                f"-Failed to store data in MYSQL DB, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            return CreateBetResponse(500, result)
        