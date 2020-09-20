#! python3
#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#
import os, sys

import _config as config


from tools_logger import *

try:

    from datetime import datetime as dt

except:

    os.system('pip install datetime')

    from datetime import datetime as dt

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


#######################################
# FUNCTIONS
#######################################

#--------------------------------------
def get_table_and_cols(TABLE, saveFile):
#--------------------------------------
    
    try:

        print()

        myFile = C.export_to_file(saveFile, TABLE, export_params={"with_column_names":True})

        stmt = C.last_statement()

        print(f'{my_pgm} EXPORTED {stmt.rowcount()} rows from table {TABLE} in {stmt.execution_time}s')

        logging.info("# " + my_pgm + " EXPORTED " + str(stmt.rowcount()) + " rows from table " + TABLE + " in " + str(stmt.execution_time) + " sec")


    except Exception as e:

        print(os.path.basename(__file__), "unable to READ table", TABLE, "skipping with no action taken!")

        print(e)

        sys.exit(0)   



#######################################
# MAIN LOGIC
#######################################

my_pgm = os.path.basename(__file__)

my_path = os.getcwd()

now = dt.today().strftime('%Y-%m-%d-%H:%M:%S')

logging_filename = my_pgm[0:(my_pgm.index('.py'))] + '.log'

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'a', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

TABLE=''

if len(sys.argv) > 1:

    TABLE = sys.argv[1]
    
else:
    
    TABLE = 'EXA_DB_SIZE_HOURLY'

logging.info("#--------------------------------------#")

logging.info("# Entering " + os.path.basename(__file__))

logging.info("#--------------------------------------#")

logging.info("# " + my_pgm +  " called with TABLE " + TABLE )




currPath = os.getcwd()              # Directory you are in NOW

savePath = config.dsn              # We will be creating this new sub-directory

myPath = (currPath + '/' + savePath)# The full path of the new sub-dir

#-----------------------------------#
# Set up place to save spreadsheet
#-----------------------------------#
if not os.path.exists(myPath):      # The directory you are in NOW
   
    os.makedirs(myPath)             # create a new dir below the dir your are in NOW

os.chdir(myPath)                    # move into the newly created sub-dir

logging.info("# " + my_pgm + " working dir directory " + myPath )

subject= TABLE

saveFile=(subject + '.csv')    # The RESUlTS we are saving on a daily basis


#######################################
# Start the database connection using 
# pyexasol connector
#######################################

try:

    C = pyexasol.connect(dsn=(config.dsn + ":" + str(config.port)), user=config.user, password=config.password, schema=config.schema, compression=True)
    
    print("INFO: ", my_pgm, "successfully connected to database using schema", config.schema)

    logging.info("# " + my_pgm +  " successfully connected to database using schema " + config.schema)

except Exception as e:
    
    print("Unable to connect using ", SYS, SYS_PW, "with schema:", SCHEMA)
    
    print(e)
    
    sys.exit(0)

get_table_and_cols(TABLE, saveFile)
  

