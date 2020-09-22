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




#######################################
# VARIABLES
#######################################

# now = dt.today().strftime('%Y%m%d_%H%M%S')

dir_path = os.path.dirname(os.path.realpath(__file__))

new_dir =""

global in_ticket

in_ticket = ""

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

msg_info = "# Starting " + os.path.basename(__file__)

logging.info(msg_info)

logging.info("#####################################")


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


#--------------------------------------
# Get admin configurations
#--------------------------------------

logging.info("# " + my_pgm + " calling tools_parse_config")

try:

    b = ParseConfig(class_chart, 'config_admin.ini')

except Exception as e:
    
    print("#######################################")

    print("# WARNING" + os.path.basename(__file__) )

    print("#-------------------------------------#")

    print("# Unable to read config_admin.ini section REPORTING to get log_level")

    print("# Using defaults:")

    print("# ===> " + os.path.basename(__file__) + " using log_level of WARNING")

    print(e)

try:

    log_level, outlier_threshold, reports_hourly, reports_daily = b.read_config_admin_reporting('.', 'config_admin.ini')

    print("# " + os.path.basename(__file__) + " REPORTING variables log_level " + log_level )


except Exception as e:

    print("#------------------------------------#")

    print("WARNING: " + os.path.basename(__file__) + " in directory " + os.getcwd())

    print("#------------------------------------#")

    print("# " + os.path.basename(__file__) + " unable to reference REPORTING section of config_admin.ini")

    print("# Using defaults:")

    print("# ==> log_level " + log_level)

    print(e)

# log_level = "WARNING"

######################################
# START LOGIC for MAIN
######################################
if __name__ == "__main__":

    if len(sys.argv) == 1:

        config_in = 'config_reports.ini'

        in_ticket = ''

        new_dir = (config_db.dsn)

    elif len(sys.argv) == 2 :

        config_in = sys.argv[1]

        new_dir = (config_db.dsn)

    elif len(sys.argv) > 2:

        config_in = sys.argv[1]

        in_ticket = sys.argv[2]

        new_dir = str("EXA-" + str(in_ticket))


#######################################
#######################################
# BEGIN MAIN LOGIC
#######################################
#######################################

work_dir = os.getcwd()

filename = str(os.getcwd() + '\\' + config_in)

if os.path.exists(filename):

    logging.info("# " + os.path.basename(__file__) + " was given config file " + config_in)

else:

    logging.error("#####################################")

    logging.error("# " + os.path.basename(__file__)) 

    logging.error("# " + os.path.basename(__file__) + " Could not find config file: " + config_in)

    logging.error("# " + os.path.basename(__file__) + " Ensure " + config_in + " exists in this directory: " + os.getcwd())

    logging.error("# ---> Does " + config_in + " exist?")

    logging.error("# ---> Is "  + config_in + " a readable file?")

    logging.error("# " + os.path.basename(__file__) + " Aborting with no action taken")

    logging.error("#####################################")

    print("#####################################")

    print("# " + os.path.basename(__file__)) 

    print("# Could not find config file: " + config_in)

    print("# Ensure " + config_in + " exists in this directory: " + os.getcwd())

    print("# ---> Does " + config_in + " exist?")

    print("# ---> Is "  + config_in + " a readable file?")

    print("# " + os.path.basename(__file__) + " Aborting with no action taken")

    print("#####################################")

    sys.exit(0)


if len(str(in_ticket)) > 3:

    msg_info = "# " + os.path.basename(__file__) + " is calling jira_download.py with " + str(in_ticket)

    logging.info(msg_info)

    print("# INFO:", os.path.basename(__file__))

    print("# is calling jira_download.py with", str(in_ticket))

    print("#####################################")

    print()

    msg_info = "# Executing call " + dir_path + '\\' + "subr_jira_download.py " + str(in_ticket)

    logging.info(msg_info)


    subr_rc = subprocess.call(["python", dir_path + "/" + "subr_jira_download.py", str(in_ticket)])

    if subr_rc != 0:

        logging.error("# " + os.path.basename(__file__) + " received return code " + str(subr_rc) + " from subr_jira_download.py")

        logging.error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        print("# " + os.path.basename(__file__) + " Aborting after receiving subr_rc:" + str(subr_rc) + " from subr_jira_download.py")

        print("#####################################")

        sys.exit(-1)

else:

    msg_info = "# Executing call " + dir_path + '\\' + "test_get_config_tbls.py " 

    logging.info(msg_info)

    subr_rc = subprocess.call(["python", dir_path + "/" + "test_get_config_tbls.py"])

    if subr_rc != 0:

        logging.error("# " + os.path.basename(__file__) + " received return code " + str(subr_rc) + " from test_get_config_tbls.py")

        logging.error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        print("# " + os.path.basename(__file__) + " Aborting after receiving subr_rc:" + str(subr_rc) + " from test_get_config_tbls.py")

        print("#####################################")

        sys.exit(-1)


config = configparser.ConfigParser()

config.read(os.getcwd() + '/' + config_in)

DAILY_TBLZ = []

HOURLY_TBLZ = []

for section in config.sections():

    if config[section]['CONFIG_HOURLY_TBL'] not in HOURLY_TBLZ:

        HOURLY_TBLZ.append(config[section]['CONFIG_HOURLY_TBL'])

    if config[section]['CONFIG_DAILY_TBL'] not in DAILY_TBLZ:

        DAILY_TBLZ.append(config[section]['CONFIG_DAILY_TBL'])



for table in range(len(DAILY_TBLZ)):

    DAILY_TBLZ[table] = str(DAILY_TBLZ[table] + '.csv')

for table in range(len(HOURLY_TBLZ)):

    HOURLY_TBLZ[table] = str(HOURLY_TBLZ[table] + '.csv')

print(my_pgm + ": HOURLY_TBLZ after CSV conversion", HOURLY_TBLZ)
print(my_pgm + ": DAILY_TBLZ after CSV conversion", DAILY_TBLZ)

#os.chdir(dir_path)

msg_info = "# " + os.path.basename(__file__) + " processing igapa pgms in directory " + os.getcwd()

logging.info(msg_info)

print()

print(msg_info)

print()

if (os.path.exists(new_dir + '\\' + DAILY_TBLZ[0])  and (os.path.exists(new_dir + '\\' + HOURLY_TBLZ[0]))) : 

    if len(in_ticket) > 3:

        msg_info = "# " + os.path.basename(__file__) + " calling python " + dir_path + "\\" + "subr_chart_4_rows.py " + str(new_dir)  + " " + str(config_in)

        logging.info(msg_info)

        subr_rc = subprocess.call(["python", dir_path + "/" + "subr_chart_4_rows.py", str(new_dir), str(config_in)])

    else:

        msg_info = "# " + os.path.basename(__file__) + " calling python " + dir_path + "\\" + "subr_chart_4_rows.py " + config_db.dsn  + " " + str(config_in)

        logging.info(msg_info)

        subr_rc = subprocess.call(["python", dir_path + "/" + "subr_chart_4_rows.py", str(config_db.dsn), str(config_in)])


else:

    print("#####################################")

    msg_info = "#####################################"

    logger.warning(msg_info)

    logger.warning("# ===> Check other logs for ERRORS! <=== ")

    logger.warning("# ===> Check other logs for ERRORS! <=== ")

    logger.warning("# ===> Check other logs for ERRORS! <=== ")
 
    msg_info = "# WARNING: " + os.path.basename(__file__)

    logger.warning(msg_info)

    logger.warning("# processed ticket:\t " +  new_dir)

    logger.warning("# BUT did not find any usable CSV files for")

    logger.warning("# generating charts. Ending processing without any charts.")

    logger.warning("#")

    logger.warning("# This solution is looking for: ")

    logger.warning("# " +  str(new_dir + '\\' + DAILY_TBLZ[0]) + " and " +  str(new_dir + '\\' + HOURLY_TBLZ[0]) )

    logger.warning("#####################################")

    print("# WARNING:", os.path.basename(__file__))

    print("# processed ticket:\t", new_dir)

    print("# BUT did not find any usable CSV files for")

    print("# generating charts. Ending processing without any charts.")

    print("#")

    print("# This solution is looking for: ")

    print("#", str(new_dir + '\\' + DAILY_TBLZ[0]), "and", str(new_dir + '\\' + HOURLY_TBLZ[0]) )

    print("#####################################")

logging.info("#####################################")

logging.info("# " + os.path.basename(__file__) + " succeessful exit.")

logging.info("#####################################")
