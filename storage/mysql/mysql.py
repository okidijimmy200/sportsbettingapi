from typing import Tuple
from sqlalchemy.orm import sessionmaker
from service.interfaces import StorageInterface
from storage.mysql.models import BettingModel, BettingSchema
from models.models import SportBet, ReadBetRequest, ReadBetResponse

class MySQLStorage(StorageInterface):
    db: sessionmaker
    def __init__(self, db: sessionmaker) -> None:
        self.db = db

    def create_bet(self, bet: SportBet) -> Tuple[int, str]:
        try:
            new_data = BettingModel(
                league=bet.league,
                home_team=bet.home_team,
                away_team=bet.away_team,
                home_team_win_odds=bet.home_team_win_odds,
                away_team_win_odds=bet.away_team_win_odds,
                draw_odds=bet.draw_odds,
                game_date=bet.game_date
            )
            self.db.add(new_data)
            self.db.commit()
            result = 'Data stored successfully in MYSQL db'
            return 201, result
        except Exception as e:
            reason = (
                f"failed to read data from storage: "
                + f"{type(e).__name__} {str(e)}"
            )
            print(reason) # TODO: make log
            return 500, reason, None

    def read_bet(self, data: ReadBetRequest) -> ReadBetResponse:
        try:
            schema = BettingSchema()
            q = self.db.query(BettingModel).filter(BettingModel.league == data.league, BettingModel.game_date.between(data.start_date, data.end_date)).first()
            reason = schema.dump([q], many=True)
            if reason is None:
                return 403, None, 'Data not found'
            return 200, reason, 'Data read from mysql db'
        except Exception as e:
            reason = (
                f"failed to read data from storage: "
                + f"{type(e).__name__} {str(e)}"
            )
            print(reason) # TODO: make log
            return 500, reason, None