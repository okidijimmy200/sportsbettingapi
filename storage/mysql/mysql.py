from typing import Tuple
from sqlalchemy.orm import sessionmaker
from service.interfaces import StorageInterface
from storage.mysql.models import BettingModel, BettingSchema
from models.models import (
    SportBet, 
    ReadBetRequest, 
    ReadBetResponse, 
    UpdateBetRequest, 
    UpdateBetResponse,
    DeleteBetRequest,
    DeleteBetResponse
)

class MySQLStorage(StorageInterface):
    db: sessionmaker
    def __init__(self, db: sessionmaker) -> None:
        self.db = db

    def create_bet(self, bet: SportBet) -> Tuple[int, str]:
        try:
            print(bet)
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

    def update_bet(self, data: UpdateBetRequest) -> UpdateBetResponse:
        try:
            q = self.db.query(BettingModel).filter(
                BettingModel.league == data.league, 
                BettingModel.home_team == data.home_team,
                BettingModel.away_team == data.away_team
                ).first()
            
            if q is None:
                return 404, f'Data with id {data.id} not available'
            schema = BettingSchema()
            new_data = {
                'league': data.league,
                'home_team': data.home_team,
                'away_team': data.away_team,
                'home_team_win_odds': data.home_team_win_odds,
                'away_team_win_odds': data.away_team_win_odds,
                'draw_odds': data.draw_odds,
                'game_date':data.game_date
            }
            result = schema.load(new_data)
            q.body = result
            self.db.commit()
            return 200, 'Data updated in mysql db'
        except Exception as e:
            result = (
                f"-Failed to store data in MYSQL DB, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            print(result)
            reason = '-Failed to update data in db'
            return 500, reason
    
    def delete_bet(self, data: DeleteBetRequest) -> DeleteBetResponse:
        try:
            # schema = BettingSchema()
            print(data.game_date)
            q = self.db.query(BettingModel).filter(BettingModel.league == data.league). \
                                            filter(BettingModel.home_team == data.home_team). \
                                            filter(BettingModel.away_team == data.away_team). \
                                            filter(BettingModel.game_date == data.game_date)
            print(q)
            # result = schema.dump([q], many=True)
            if q is None:
                return 400, 'Data not found'
            self.db.query(BettingModel).filter(BettingModel.league == data.league). \
                                            filter(BettingModel.home_team == data.home_team). \
                                            filter(BettingModel.away_team == data.away_team). \
                                            filter(BettingModel.game_date == data.game_date).delete()
            # self.db.delete(q)
            self.db.commit()
            return 204, 'Data deleted from mysql db'
        except Exception as e:
            reason = (
                f"failed to delete data from storage: "
                + f"{type(e).__name__} {str(e)}"
            )
            print(reason) # TODO: make log
            return 500, reason, None