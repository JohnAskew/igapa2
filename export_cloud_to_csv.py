#! python3
#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#
import os, sys

import _config as config

# if os.path.exists(logging_filename):

#     os.remove(logging_filename)

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
def log_and_print(msg=''):
#--------------------------------------

    print("# " + os.path.basename(__file__) + ": " + str(msg))

    logging.info("# " + os.path.basename(__file__) + ": " + str(msg))

#--------------------------------------
def get_table_and_cols(TABLE, saveFile):
#--------------------------------------
    
    try:
        
        if TABLE.startswith( '$' ):

            pd = C.export_to_pandas('SELECT * FROM {table_name!q}', {'table_name': TABLE})
           
            pd.to_csv((TABLE + '.csv') , na_rep = 0)

            pd_rows, pd_cols = pd.shape

            log_and_print(f'EXPORTED ' + str({pd.shape[0]}) + f'rows from table {TABLE}')

        else:

            myFile = C.export_to_file(saveFile, TABLE, export_params={"with_column_names":True})

            stmt = C.last_statement()

            log_and_print("EXPORTED " + str(stmt.rowcount()) + " rows from table " + TABLE + " in " + str(stmt.execution_time) + " sec")


    except Exception as e:

        log_and_print("#######################################")

        log_and_print("ERROR: unable to READ table " + TABLE +  " Aborting with no action taken!")

        log_and_print("#######################################")

        log_and_print(e)

        sys.exit(12)  



#######################################
# MAIN LOGIC
#######################################

from igapa2_linkage import *

TABLE = 'EXA_DB_SIZE_HOURLY'

if len(sys.argv) > 1:

    if len(sys.argv[10]) > 0:

        TABLE = sys.argv[10]

my_pgm = os.path.basename(__file__)

my_path = os.getcwd()

now = dt.today().strftime('%Y-%m-%d-%H:%M:%S')

logging_filename = os.path.basename(__file__)[0:(os.path.basename(__file__).index('.py'))] + '.log'

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'a', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')


log_and_print("#--------------------------------------#")

log_and_print("# Entering " + os.path.basename(__file__))

log_and_print("#--------------------------------------#")

log_and_print("called with TABLE -->" + TABLE )




currPath = os.getcwd()              # Directory you are in NOW

if DB_Linkage.pass_host:

    savePath = DB_Linkage.pass_host              # We will be creating this new sub-directory

else:

    savePath = config.dsn

myPath = (currPath + '/' + savePath)# The full path of the new sub-dir


#-----------------------------------#
# Set up place to save spreadsheet
#-----------------------------------#
if not os.path.exists(myPath):      # The directory you are in NOW
   
    os.makedirs(myPath)             # create a new dir below the dir your are in NOW

os.chdir(myPath)                    # move into the newly created sub-dir

log_and_print("working dir directory " + myPath )

subject= TABLE

saveFile=(subject + '.csv')    # The RESUlTS we are saving on a daily basis


#######################################
# Start the database connection using 
# pyexasol connector
#######################################

log_and_print("#--------------------------------------#")

log_and_print("# Entering " + os.path.basename(__file__))

log_and_print("#--------------------------------------#")


try:

    if DB_Linkage.pass_host:

        pass

    else:

        DB_Linkage.pass_host = config.dsn

    if DB_Linkage.pass_port:

        pass

    else:

        DB_Linkage.pass_port = config.port

    if DB_Linkage.pass_user:

        pass

    else:

        DB_Linkage.pass_user = config.user

    if DB_Linkage.pass_pw:

        pass

    else:

        DB_Linkage.pass_pw = config.password

    if DB_Linkage.pass_schema:

        pass

    else:

        DB_Linkage.pass_schema = config.schema
    
    log_and_print("calling with: DB_Linkage.pass_host: " + DB_Linkage.pass_host + " DB_Linkage.pass_port " + str(DB_Linkage.pass_port))

    C = pyexasol.connect(dsn=(DB_Linkage.pass_host + ":" + str(DB_Linkage.pass_port)), user=DB_Linkage.pass_user, password=DB_Linkage.pass_pw, schema=DB_Linkage.pass_schema, compression=True)

    log_and_print("successfully connected to database using schema " +  DB_Linkage.pass_schema)

except Exception as e:

    log_and_print("########################################")

    log_and_print("ERROR: Unable to connect using " +  DB_Linkage.pass_user + ":" + " <secret> " +  "with schema:" +  DB_Linkage.pass_schema)

    log_and_print("########################################")
    
    log_and_print(e)

    raise AttributeError("# " + os.path.basename(__file__) + ": Unable to connect to " + DB_Linkage.pass_host + ":" + DB_Linkage.pass_port)
    
    sys.exit(12)

get_table_and_cols(TABLE, saveFile)