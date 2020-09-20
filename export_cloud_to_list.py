#! python3
#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#
import os, sys

try:

	from bokeh.plotting import figure, output_file, show

	from bokeh.layouts import column

	from bokeh.models import ColumnDataSource

except:

	os.system('pip install bokeh')

	from bokeh.plotting import figure, output_file, show

	from bokeh.layouts  import column

	from bokeh.models import ColumnDataSource

try:

    import pyexasol

except:

    os.system('pip install pyexasol')

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

try:

    import shutil

except:

    os.system('pip install shutil')

    import shutil

try:

    import numpy as np

except:

    os.system("pip install numpy")

    import numpy as np


IP='demodb.exasol.com'

PORT='8563'

SYS='exasol_joas'

SYS_PW='J0hnsPassw0rdShouldB3Ch4ng3d'

SCHEMA='EXA_STATISTICS' #must be all caps

TABLE=''

if len(sys.argv) > 1:

    TABLE = sys.argv[1]
    
    print("INCOMING: sys.argv", sys.argv, "sys.argv[1]", sys.argv[1], "stock", TABLE)

else:
    
    TABLE = 'EXA_DB_SIZE_MONTHLY'



currPath = os.getcwd()              # Directory you are in NOW

savePath = 'stocks_hold_area'                  # We will be creating this new sub-directory

myPath = (currPath + '/' + savePath)# The full path of the new sub-dir

subject = ""

stock_folder = (currPath + '/askew/')


#-----------------------------------#
# Set up place to save spreadsheet
#-----------------------------------#
if not os.path.exists(myPath):      # The directory you are in NOW
   
    os.makedirs(myPath)             # create a new dir below the dir your are in NOW

os.chdir(myPath)                    # move into the newly created sub-dir

subject= TABLE

saveFile=(subject + '.csv')    # The RESUlTS we are saving on a daily basis

myFile = 'askew_exp.csv'

INTERVAL_START = []

RAW_OBJECT_SIZE_AVG = []

RAW_OBJECT_SIZE_MAX = []

#######################################
# Start the database connection using 
# pyexasol connector
#######################################

try:

    C = pyexasol.connect(dsn=IP+':'+PORT, user=SYS, password=SYS_PW, schema=SCHEMA)
    
    print("INFO: Successfully connected to database using schema", SCHEMA)

except Exception as e:
    
    print("Unable to connect using ", SYS, SYS_PW, "with schema:", SCHEMA)
    
    print(e)
    
    sys.exit(0)

try:

    print("TABLE", TABLE, "saveFile:", saveFile)
    
    print()

    myFile = C.export_to_list(TABLE, export_params={"columns":["INTERVAL_START","RAW_OBJECT_SIZE_AVG", "RAW_OBJECT_SIZE_MAX"]})

    stmt = C.last_statement()

    print(f'EXPORTED {stmt.rowcount()} rows in {stmt.execution_time}s')

    print("You are currently in", os.getcwd())
    
    col_cnt = 0 

    for row in myFile:

	    for col in row:

	        if col_cnt == 0:

	        	INTERVAL_START.append(col)

	        	col_cnt += 1

	        elif col_cnt == 1:

	        	RAW_OBJECT_SIZE_AVG.append(col)

	        	col_cnt += 1

	        else:

	        	RAW_OBJECT_SIZE_MAX.append(col)

	        	col_cnt = 0

    print("INTERVAL_START", INTERVAL_START)
 
    print("RAW_OBJECT_SIZE_MAX", RAW_OBJECT_SIZE_MAX)

    print("RAW_OBJECT_SIZE_AVG", RAW_OBJECT_SIZE_AVG)

except Exception as e:

    print("Unable to READ, skipping")

    print(e)

    sys.exit(0)     

output_file("lines.html")

INTERVAL_START=pd.to_datetime(INTERVAL_START)

q = figure(title="RAW_OBJECT_SIZE_MAX over time", x_axis_type = "datetime", x_axis_label='INTERVAL_START', y_axis_label='RAW_OBJECT_SIZE_MAX', plot_height = 300)

#q.line(INTERVAL_START, RAW_OBJECT_SIZE_MAX, legend="Crap, I need to fix this", line_width=2)

q.vbar(INTERVAL_START, top= RAW_OBJECT_SIZE_MAX,width = 750, line_width =2)

p = figure(title="RAW_OBJECT_SIZE_AVG over time", x_axis_type = "datetime", x_axis_label='INTERVAL_START', y_axis_label='RAW_OBJECT_SIZE_AVG', plot_height = 300, x_range=q.x_range)

p.vbar(INTERVAL_START, top = RAW_OBJECT_SIZE_AVG, width = 750, line_width=2)

# add a line renderer with legend and line thickness



# show the results
show(column([q, p]))

