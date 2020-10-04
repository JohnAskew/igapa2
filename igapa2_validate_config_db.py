'''
name: igapa2_validate_config_db.py
desc: To validate the database connection 
      using parameter/argument input or
      taking connection from config files.
usage: None. This is called as a utility or tool.
'''
import os

import sys

from tools_logger import *

try:

    from datetime import datetime as dt

except:

    os.system('pip install datetime')

    from datetime import datetime as dt

import _config as config_db

try:

	import subprocess

except:

	os.system('pip install subprocess')

	import subprocess

#######################################
# FUNCTIONS
#######################################
#--------------------------------------
def log_and_print(msg = "Error: Nothing passed to log_and_print."):
#--------------------------------------

    print("# " + my_pgm + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)

#######################################
# MAIN LOGIC
#######################################
my_pgm = os.path.basename(__file__)

my_path = os.getcwd()

now = dt.today().strftime('%Y-%m-%d-%H:%M:%S')

logging_filename = os.path.basename(__file__)[0:(os.path.basename(__file__).index('.py'))] + '.log'

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')


log_and_print("#--------------------------------------#")

log_and_print("# Entering " + os.path.basename(__file__))

log_and_print("#--------------------------------------#")

from igapa2_linkage import *

log_and_print("#--------------------------------------#")

log_and_print("received Jira source: " +  JIRA_Linkage.pass_jira_source + " user: " + JIRA_Linkage.pass_jira_user + " password " + JIRA_Linkage.pass_jira_pw)

log_and_print("received: db host: " +  DB_Linkage.pass_host + " port: " + DB_Linkage.pass_port + " user: " + DB_Linkage.pass_user + " password: " + DB_Linkage.pass_pw + " schema: " + DB_Linkage.pass_schema)

log_and_print("#--------------------------------------#")


if DB_Linkage.pass_host:

	log_and_print("Parameter -m received: " + DB_Linkage.pass_host)

	if DB_Linkage.pass_port:

		log_and_print("Parameter -n received: " + DB_Linkage.pass_port )

	else:

		DB_Linkage.pass_port = config_db.port

		log_and_print("No port argument, using _config.py port: " + str(config_db.port))

	if ( DB_Linkage.pass_user and DB_Linkage.pass_pw ):

		log_and_print("will call igapa2_main.py with arguments " + DB_Linkage.pass_host + " port: " + str(DB_Linkage.pass_port) + " user: " + DB_Linkage.pass_user + " password: <secret> " + " schema: " + DB_Linkage.pass_schema)

	else:

		DB_Linkage.pass_user = config_db.user

		DB_Linkage.pass_pw   = config_db.password

		log_and_print("will call igapa2_main.py with _config.py settings " + DB_Linkage.pass_host 
			                                           + " port: " + str(DB_Linkage.pass_port) 
			                                           + " user: " + DB_Linkage.pass_user 
			                                           + " password: <secret>" 
			                                           + " schema: " + DB_Linkage.pass_schema)
 
subr_rc = subprocess.call(["python", dir_path + "/" + "igapa2_main.py", pass_config
                                                                      , JIRA_Linkage.pass_jira_source
                                                                      , JIRA_Linkage.pass_jira_user
                                                                      , str(JIRA_Linkage.pass_jira_pw)
                                                                      , DB_Linkage.pass_host
                                                                      , str(DB_Linkage.pass_port)
                                                                      , DB_Linkage.pass_user
                                                                      , str(DB_Linkage.pass_pw)
                                                                      , DB_Linkage.pass_schema])
if subr_rc != 0:

    log_and_print("####################################")

    log_and_print( "ERROR: received return code " + str(subr_rc) + " from igapa2_main.py")

    log_and_print( " Aborting with no action taken.")

    log_and_print("####################################")

    sys.exit(-1)

