import pandas as pd


class GetComparables:
    def __init__(self, data):
        # data is set as the model to use to find comparables
        self.data = data

    def get_player_comparables(self, player: pd.DataFrame) -> pd.DataFrame:
        """
        Get the top 5 comparable players based on the inputted player data
        :param player: pd.DataFrame
        :return: pd.DataFrame
        """
        assert isinstance(self.data, pd.DataFrame)

        # get the various comparables
        age_comparables = self.data[(self.data['Age'] >= (player['Age'][0]-1)) &
                                    (self.data['Age'] <= (player['Age'][0]+1))]
        gp_comparables = age_comparables[(age_comparables['GP'] >= (player['GP'][0]-20)) &
                                         (age_comparables['GP'] <= (player['GP'][0]+20))]
        g_comparables = gp_comparables[(gp_comparables['G'] >= (player['G'][0]-10)) &
                                       (gp_comparables['G'] <= (player['G'][0]+10))]
        all_comparables = g_comparables[(g_comparables['A'] >= (player['A'][0]-20)) &
                                        (g_comparables['A'] <= (player['A'][0]+20))]

        return all_comparables




