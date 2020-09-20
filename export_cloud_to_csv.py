#! python3
#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#
import os, sys

import _config as config

try:

    import pyexasol

except:

    os.system('pip install pyexasol')

    import pyexasol

try:

    import csv

except:

    os.system("pip install csv")

    import csv

try:

    import pandas as pd

except:

    os.system('pip install pandas')

    import pandas as pd




TABLE=''

if len(sys.argv) > 1:

    TABLE = sys.argv[1]
    
    print("INCOMING: sys.argv", sys.argv, "table", TABLE)

else:
    
    TABLE = 'EXA_DB_SIZE_HOURLY'



currPath = os.getcwd()              # Directory you are in NOW

savePath = config.dsn              # We will be creating this new sub-directory

myPath = (currPath + '/' + savePath)# The full path of the new sub-dir

#-----------------------------------#
# Set up place to save spreadsheet
#-----------------------------------#
if not os.path.exists(myPath):      # The directory you are in NOW
   
    os.makedirs(myPath)             # create a new dir below the dir your are in NOW

os.chdir(myPath)                    # move into the newly created sub-dir

subject= TABLE

saveFile=(subject + '.csv')    # The RESUlTS we are saving on a daily basis


#######################################
# Start the database connection using 
# pyexasol connector
#######################################

try:

    C = pyexasol.connect(dsn=(config.dsn + ":" + str(config.port)), user=config.user, password=config.password, schema=config.schema, compression=True)
    
    print("INFO: Successfully connected to database using schema", config.schema)

except Exception as e:
    
    print("Unable to connect using ", SYS, SYS_PW, "with schema:", SCHEMA)
    
    print(e)
    
    sys.exit(0)

try:

    print("TABLE", TABLE, "saveFile:", saveFile)
    
    print()

    myFile = C.export_to_file(saveFile, TABLE, export_params={"with_column_names":True})

    stmt = C.last_statement()

    print(f'EXPORTED {stmt.rowcount()} rows in {stmt.execution_time}s')

    print(C.meta.sql_columns("Select * from " + TABLE))

    print("You are currently in", os.getcwd())
    

except Exception as e:

    print("Unable to READ, skipping")

    print(e)

    sys.exit(0)     

