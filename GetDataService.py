import pandas as pd
import sqlite3 as sql


class GetDataService:
    @staticmethod
    def get_all_players() -> pd.DataFrame:
        # get connection
        conn = sql.connect('C:\Projects\Elliotte\Model\Database\model.db')
        # return all players
        return pd.read_sql(sql='SELECT * FROM players;', con=conn)


