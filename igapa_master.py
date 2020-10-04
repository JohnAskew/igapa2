'''
name: igapa_master.py
desc: Main program to run solution.

To-Do:
1. Move JIRA URL to config_admin.ini and use config parser in subr_jira_download.py
2. Try setting all the logging_filename in each pgm to igapa_master.log
3. All logging programs log an exit message.
4. Ensure each program doing a call has a log entry stating it's call program..
'''
import os

import sys

try:

    from datetime import datetime as dt

except:

    os.system('pip install datetime')

    from datetime import datetime as dt

my_pgm = os.path.basename(__file__)

now = dt.today().strftime('%Y%m%d_%H%M%S')

logging_filename = my_pgm[0:(my_pgm.index('.py'))] + '.log'

if os.path.exists(logging_filename):

    dest = str(logging_filename + '_' + now + '.log')

    try:

        os.rename(logging_filename, dest)

    except Exception as e:

        print("#--------------------------------------#")

        print("# WARNING: " + os.path.basename(__file__) + " Unable to rename " + logging_filename + " to " + dest)

        print("# " + os.path.basename(__file__) + " REUSING " + logging_filename)

        print(e)

        print("#--------------------------------------#")


#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#


import _config as config_db

try:

    import configparser

except:

    os.system('pip install configparser')

    import configparser

try:

    import subprocess

except:

    os.system("pip install subprocess")

    import subprocess

try:

    import logging

except:

    os.system('pip install logging')

    import logging

try:

    from tools_parse_config import ParseConfig

except:
    
    msg = "Unable to find tools_parse_config.py"

    logging.error("#######################################")

    logging.error("# ERROR in " +  os.path.basename(__file__))
    
    logging.error("# " + msg)

    logging.error("# " +  os.path.basename(__file__) + " aborting with no action taken.")

    logging.error("#######################################")

    print("#######################################")

    print("# ERROR in", os.path.basename(__file__))
    
    print(msg)

    print("#", os.path.basename(__file__), "aborting with no action taken.")

    print("#######################################")

    sys.exit(13)

from igapa2_linkage import *


#######################################
# VARIABLES
#######################################

# now = dt.today().strftime('%Y%m%d_%H%M%S')

dir_path = os.path.dirname(os.path.realpath(__file__))

new_dir =""

global pass_jira_source

pass_jira_source = ""

class_chart = 'DB_SIZE'

log_level = "WARNING"

#######################################
# Save off the old report - do not overlay
#######################################

#-------------------------------------#
# Extract log_level for reporting details
# ------------------------------------#
#######################################
# Start by extracting the LOGGING 
#    reporting level for output 
#    granularity (how much detail).
#######################################
#--------------------------------------
# Log the beginning of processsing
#--------------------------------------

log_level ="INFO"

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')


logging.info("#####################################")

msg_info = "Entering" + os.path.basename(__file__)

logging.info(msg_info)

logging.info("#####################################")


try:

    from tools_parse_config import ParseConfig

except:
    
    msg = "Unable to find tools_parse_config.py"

    log_and_print("#######################################")

    log_and_print("# ERROR in " +  os.path.basename(__file__))
    
    log_and_print("# " + msg)

    log_and_print("# " +  os.path.basename(__file__) + " aborting with no action taken.")

    log_and_print("#######################################")

    sys.exit(13)

#######################################
# FUNCTIONS
#######################################
#--------------------------------------
def log_and_print(msg = ''):
#--------------------------------------
    print("# " + os.path.basename(__file__) + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)
#--------------------------------------
# Get admin configurations
#--------------------------------------

log_and_print("calling tools_parse_config")

try:

    b = ParseConfig(class_chart, 'config_admin.ini')

except Exception as e:
    
    log_and_print("#######################################")

    log_and_print("# WARNING" + os.path.basename(__file__) )

    log_and_print("#-------------------------------------#")

    log_and_print("# Unable to read config_admin.ini section REPORTING to get log_level")

    log_and_print("# Using defaults:")

    log_and_print("# ===> " + os.path.basename(__file__) + " using log_level of WARNING")

    log_and_print(e)

try:

    log_level, outlier_threshold, reports_hourly, reports_daily = b.read_config_admin_reporting('.', 'config_admin.ini')

    log_and_print("REPORTING variables log_level " + log_level )


except Exception as e:

    log_and_print("#------------------------------------#")

    log_and_print("WARNING: " + os.path.basename(__file__) + " in directory " + os.getcwd())

    log_and_print("#------------------------------------#")

    log_and_print( " unable to reference REPORTING section of config_admin.ini")

    log_and_print("# Using defaults:")

    log_and_print("# ==> log_level " + log_level)

    log_and_print(e)

######################################
# START LOGIC for MAIN
######################################

from igapa2_linkage import *

if __name__ == "__main__":

    if len(sys.argv) == 1:

        pass_config = 'config_reports.ini'

        pass_jira_source = ''

        new_dir = (config_db.dsn)

    else:

        new_dir = DB_Linkage.pass_host


#######################################
#######################################
# BEGIN MAIN LOGIC
#######################################
#######################################

work_dir = os.getcwd()

filename = str(os.getcwd() + '\\' + pass_config)

if os.path.exists(filename):

    log_and_print("was given config file " + pass_config)

else:

    log_and_print("#####################################")

    log_and_print("# " + os.path.basename(__file__)) 

    log_and_print("Could not find config file: " + pass_config)

    log_and_print("Ensure " + pass_config + " exists in this directory: " + os.getcwd())

    log_and_print("# ---> Does " + pass_config + " exist?")

    log_and_print("# ---> Is "  + pass_config + " a readable file?")

    log_and_print("Aborting with no action taken")

    log_and_print("#####################################")

    
    sys.exit(0)

if len(sys.argv) ==1:

    log_and_print("was not passed any parameters linkage. Using config files to drive processing.")

else:

    # for arg  in range(len(sys.argv)):

    #     log_and_print(my_pgm + " received parm " + str(sys.argv[arg]))

    pass

if len(str(pass_jira_source)) > 3:

    msg_info = "is calling jira_download.py with " + str(pass_jira_source)

    log_and_print(msg_info)

    msg_info = "Executing call " + dir_path + '\\' + "subr_jira_download.py " + str(pass_jira_source)

    log_and_print(msg_info)

    subr_rc = subprocess.call(["python", dir_path + "/" + "subr_jira_download.py", pass_config, pass_jira_source, pass_jira_user, pass_jira_pw, pass_host, pass_port, pass_user, pass_pw, pass_schema])

    if subr_rc != 0:

        log_and_print("#####################################")

        log_and_print( "received return code " + str(subr_rc) + " from subr_jira_download.py")

        log_and_print( "Aborting with no action taken.")

        log_and_print("#####################################")

        sys.exit(-1)

else:

    msg_info = ("Executing call to test_get_config_tbls.py with DB_Linkage.pass_host: "
                                                     + DB_Linkage.pass_host
                                                     + " DB_Linkage.pass_port: "
                                                     + DB_Linkage.pass_port
                                                     + " DB_Linkage.pass_user: "
                                                     + DB_Linkage.pass_user
                                                     + " DB_Linkage.pass_pw: "
                                                     + "<secret>"
                                                     + " DB_Linkage.pass_schema: "
                                                     + DB_Linkage.pass_schema
                                                     )

    log_and_print(msg_info)

    subr_rc = subprocess.call(["python", dir_path + "/" + "test_get_config_tbls.py"
                                                         , DB_Linkage.pass_config
                                                         , JIRA_Linkage.pass_jira_source
                                                         , JIRA_Linkage.pass_jira_user
                                                         , JIRA_Linkage.pass_jira_pw
                                                         , DB_Linkage.pass_host
                                                         , DB_Linkage.pass_port
                                                         , DB_Linkage.pass_user
                                                         , DB_Linkage.pass_pw
                                                         , DB_Linkage.pass_schema
                                                          ])

    if subr_rc != 0:

        log_and_print("####################################")

        log_and_print( "ERROR: received return code " + str(subr_rc) + " from test_get_config_tbls.py")

        log_and_print( " Aborting with no action taken.")

        log_and_print("####################################")

        sys.exit(-1)


config = configparser.ConfigParser()

config.read(os.getcwd() + '/' + pass_config)

DAILY_TBLZ = []

HOURLY_TBLZ = []


for section in config.sections():

    if config[section]['CONFIG_HOURLY_TBL'] not in HOURLY_TBLZ:

        HOURLY_TBLZ.append(config[section]['CONFIG_HOURLY_TBL'])

    if config[section]['CONFIG_DAILY_TBL'] not in DAILY_TBLZ:

        DAILY_TBLZ.append(config[section]['CONFIG_DAILY_TBL'])



for table in range(len(DAILY_TBLZ)):

    DAILY_TBLZ[table] = str(DAILY_TBLZ[table] + '.csv')

    log_and_print("DAILY_TBLZ after CSV conversion " + DAILY_TBLZ[table])



for table in range(len(HOURLY_TBLZ)):

    HOURLY_TBLZ[table] = str(HOURLY_TBLZ[table] + '.csv')

    log_and_print("HOURLY_TBLZ after CSV conversion " + HOURLY_TBLZ[table])

#os.chdir(dir_path)

msg_info = "processing igapa pgms in directory " + os.getcwd()

log_and_print(msg_info)

log_and_print("#---------------------------------------")

log_and_print("DIRECTORY " + dir_path + ", using SUB-DIRECTORY : " + new_dir) 

log_and_print("#---------------------------------------")


if pass_host:

    new_dir = pass_host

elif pass_jira_source:

    new_dir = str("EXA-" + str(pass_jira_source))

else:

    log_and_print("Using configdb.dsn as new_dir: " + config_db.dsn)

    new_dir = config_db.dsn

if os.path.exists(new_dir):

    pass

else:

    os.mkdir(new_dir)

if len(HOURLY_TBLZ) > 0:

    log_and_print("Here is the HOURLY Table: " + new_dir + '\\' + HOURLY_TBLZ[0])

    if len(DAILY_TBLZ) > 0:

        log_and_print("Here is the DAILY Table: " +new_dir + '\\' + DAILY_TBLZ[0])
else:

    log_and_print("#####################################")

    log_and_print("# ERROR: Unable to access either: " + new_dir + "\\ DAILY_TABLE OR "  + new_dir + '\\HOURLY_TABLE')

    log_and_print("aborting!")

    log_and_print("#####################################")

    sys.exit(12)


test_dir = (os.path.exists(new_dir + '\\' + DAILY_TBLZ[0]))


if os.path.exists(test_dir):

    log_and_print("Confirming HOURLY Table: " +new_dir + '\\' + HOURLY_TBLZ[0] )

    log_and_print("Confirming DAILY Table: " +new_dir + '\\' + DAILY_TBLZ[0] )

    test_dir = (os.path.exists(new_dir + '\\' + HOURLY_TBLZ[0]))

    if os.path.exists(test_dir): 

        msg_info = ("calling python subr_chart_4_rows.py with host: " + str(new_dir)  + "  and config: " + str(pass_config))

        log_and_print(msg_info)

        subr_rc = subprocess.call(["python", dir_path + "/" + "subr_chart_4_rows.py", str(new_dir), str(pass_config)])

    else:

        msg_info = "#####################################"

        log_and_print(msg_info)

        log_and_print("# ===> Check other logs for ERRORS! <=== ")

        log_and_print("# ===> Check other logs for ERRORS! <=== ")

        log_and_print("# ===> Check other logs for ERRORS! <=== ")
     
        msg_info = "# WARNING: " + os.path.basename(__file__)

        log_and_print(msg_info)

        log_and_print("# processed ticket:\t " +  new_dir)

        log_and_print("# BUT did not find any usable CSV files for")

        log_and_print("# generating charts. Ending processing without any charts.")

        log_and_print("#")

        log_and_print("# This solution is looking for: ")

        log_and_print("# " +  str(new_dir + '\\' + DAILY_TBLZ[0]) + " and " +  str(new_dir + '\\' + HOURLY_TBLZ[0]) )

        log_and_print("#####################################")

logging.info("#####################################")

logging.info("# " + os.path.basename(__file__) + " succeessful exit.")

logging.info("#####################################")
