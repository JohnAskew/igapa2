#! python3
#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#
import os, sys

import _config as config

try:

    import logging

except:

    os.system('pip install logging')

    import logging

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
def get_table_cols(TABLE):
#--------------------------------------

    try:

        C = pyexasol.connect(dsn=(config.dsn + ":" + str(config.port)), user=config.user, password=config.password, schema=config.schema, compression=True)
        
        print("INFO: Successfully connected to database using schema", config.schema)

        logging.info("# " + my_pgm + " Successfully connected to database using schema " + config.schema)

    except Exception as e:
        
        print("Unable to connect using ", SYS, SYS_PW, "with schema:", SCHEMA)
        
        logging.info("# " + my_pgm + "Unable to connect using " + SYS + " " + SYS_PW +  " with schema: " +  SCHEMA)

        print(e)
        
        logging.info(e)

        sys.exit(-1)
    
    try:

        dict_cols = (C.meta.sql_columns("Select * from " + TABLE))

        sort_cols = sorted(dict_cols)

        print(sort_cols)

        for col in sort_cols:

            logging.info("# " + my_pgm + " returning " + col)

        logging.info("#--------------------------------------#")

        logging.info("# " + my_pgm + " successfully exiting and returning columns")

        logging.info("#--------------------------------------#")


        return sort_cols
    

    except Exception as e:

        print(os.path.basename(__file__), "unable to READ table", TABLE, "skipping with no action taken!")

        print(e)

        sys.exit(0)   



#######################################
# MAIN LOGIC
#######################################

my_pgm = os.path.basename(__file__)

logger = logging.getLogger()

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

logging_filename = my_pgm[0:(my_pgm.index('.py'))] + '.log'

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

logging.info("#--------------------------------------#")

logging.info("# Entering " + os.path.basename(__file__))

logging.info("#--------------------------------------#")

TABLE=''

if len(sys.argv) > 1:

    TABLE = sys.argv[1]
    
    print(my_pgm, ": incoming: sys.argv", sys.argv, "table", TABLE)

else:
    
    TABLE = 'EXA_DB_SIZE_HOURLY'




#######################################
# Start the database connection using 
# pyexasol connector
#######################################

get_table_cols(TABLE)
  

