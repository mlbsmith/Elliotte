import sqlite3 as sql
from ReadDataService import *

# get the read data service
ReadDataService = ReadDataService()

# load the data
ReadDataService.read_data('C:\Projects\Elliotte\Model\Database\2012-13.xls', 'Main Page')
ReadDataService.read_data('C:\Projects\Elliotte\Model\Database\2013-14.xls', 'Main Page')
ReadDataService.read_data('C:\Projects\Elliotte\Model\Database\2014-15.xls', 'Main Page')
ReadDataService.read_data('C:\Projects\Elliotte\Model\Database\2015-16.xls', 'Main Page')
ReadDataService.read_data('C:\Projects\Elliotte\Model\Database\2016-17.xls', 'Main Page')
ReadDataService.read_data('C:\Projects\Elliotte\Model\Database\2017-18.xls', 'Main Page')

# reindex the columns for readability
ReadDataService.reindex_columns()

# convert relevant columns to numeric type
ReadDataService.convert_to_numeric()

# get basic info on the data
print(ReadDataService.all_data.describe())

# add to sql db
conn = sql.connect("C:\Projects\Elliotte\Model\Database\model.db")
cursor = conn.cursor()

ReadDataService.all_data.to_sql('Players', conn, if_exists='replace')
