import pandas as pd


class ReadDataService:

    def __init__(self):
        self.all_data = pd.DataFrame(
            columns=['Last Name', 'First Name', 'Age', 'Pos', 'GP', 'Sh', 'TOI', 'G', 'A'])

    def read_data(self, filename, sheet_name):
        """Read data from the csv database."""
        data = pd.read_excel(filename, sheet_name)
        df = data[['Last Name', 'First Name', 'Age', 'Pos', 'GP', 'Sh', 'TOI', 'G', 'A']]
        # remove players with less than 5 gp
        df = df.drop(df[(df.GP < 5)].index)
        self.add_data_to_model(df)

    def add_data_to_model(self, data: pd.DataFrame):
        """Add data to the model.
        Requires checking for duplicates and updating where necessary."""
        assert isinstance(self.all_data, pd.DataFrame)

        # if empty model, just append data
        if self.all_data.size <= 11:

            self.all_data = self.all_data.append(data)

        else:
            # get a dataframe with the most recent data from the master list
            most_recent_data = self.all_data.drop_duplicates(subset=['Last Name', 'First Name'], keep='last')
            assert isinstance(most_recent_data, pd.DataFrame)

            # merge the most recent data with incoming data
            new_data = most_recent_data.merge(data, 'right', on=['Last Name', 'First Name'])

            # make new data frame with values updated properly
            updated_data = new_data.apply(func=(lambda x: self.update_function(x)), axis=1)

            # remove excess columns from the merge
            updated_data = updated_data.drop(columns=['Age_x', 'Age_y', 'Pos_x', 'Pos_y', 'GP_x', 'GP_y', 'Sh_x',
                                                      'Sh_y', 'TOI_x', 'TOI_y', 'G_x', 'G_y', 'A_x', 'A_y'], axis=1)

            # append to master list
            self.all_data = self.all_data.append(updated_data, sort=True, ignore_index=True)

    @staticmethod
    def update_function(x):
        where_are_nans = pd.isnull(x)
        x[where_are_nans] = 0

        x['Age'] = x['Age_y']
        x['GP'] = x['GP_x'] + x['GP_y']
        x['Pos'] = x['Pos_y']
        x['Sh'] = x['Sh_x'] + x['Sh_y']
        x['TOI'] = x['TOI_x'] + x['TOI_y']
        x['G'] = x['G_x'] + x['G_y']
        x['A'] = x['A_x'] + x['A_y']

        return x

    def get_player_by_id(self, player_id):
        # player_id corresponds to the NHLid column in the .xls file
        pass

    def reindex_columns(self):
        # re-order columns
        self.all_data = self.all_data.reindex(
            columns=['Last Name', 'First Name', 'Age', 'Pos', 'GP', 'G', 'A', 'Sh', 'TOI'])

    def convert_to_numeric(self):
        # convert the columns that need to be converted to numeric types
        self.all_data['Age'] = pd.to_numeric(self.all_data['Age'], errors='coerce')
        self.all_data['GP'] = pd.to_numeric(self.all_data['GP'], errors='coerce')
        self.all_data['G'] = pd.to_numeric(self.all_data['G'], errors='coerce')
        self.all_data['A'] = pd.to_numeric(self.all_data['A'], errors='coerce')
        self.all_data['Sh'] = pd.to_numeric(self.all_data['Sh'], errors='coerce')

