'''
name: igapa2_validate_config_jira.py
desc: To edit and if needed, determine 
      which arguements to pass to other
      programs - avoiding argument conflicts.
usage: None, this is a called utility

To-Do
1. Add code to validate config_admin.ini - if not 
   then you must specify credentials.
2. 
'''
import os

import sys

from tools_logger import *

try:

    from datetime import datetime as dt

except:

    os.system('pip install datetime')

    from datetime import datetime as dt

try:

    import subprocess

except:

    os.system('pip import subprocess')

    import subprocess

try:

    from tools_parse_config import ParseConfig

except:
    
    msg = "Unable to find tools_parse_config.py"

    log_and_print("#######################################")

    log_and_print("# ERROR")
    
    loc_and_print(msg)

    log_and_print("aborting with no action taken.")

    log_and_print("#######################################")

    sys.exit(13)

from igapa2_linkage import *


#######################################
# Global Variables
#######################################


#######################################
# FUNCTIONS
#######################################
#--------------------------------------
def log_and_print(msg=''):
#--------------------------------------
    print("# " + os.path.basename(__file__) + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)

#--------------------------------------
def return_fake_error():
#--------------------------------------

    sys.exit(12)

#--------------------------------------
def validate_exists(in_file = ''):
#--------------------------------------

    if os.path.exists(in_file):

        return 0

    log_and_print("####################################################################################################################")

    log_and_print("ERROR--> No file found: " + in_file + " Please validate file exists and is readable. Aborting with no action taken.")

    log_and_print("####################################################################################################################")

    sys.exit(12)

#--------------------------------------
def validate_config(dummy = 'DB_SIZE', config_pass = 'config_reports.ini'):
#--------------------------------------

    log_and_print("Calling tools_parse_config.py to instantiate ParseConfig")

    try:

        b = ParseConfig('DB_SIZE', config_pass)

    except Exception as e:

	    log_and_print("#######################################")

	    log_and_print("FATAL: " +  os.path.basename(__file__))

	    log_and_print("# Unable to reference ParseConfig using:")

	    log_and_print("# b = ParseConfig(class_chart)")

	    log_and_print("# Does pgm tools_parse_config.py exist in " +  os.getcwd(),"?" )

	    log_and_print("# Aborting with no action taken.")

	    log_and_print(e, exc_info = True)

	    log_and_print("#######################################")

	    print("#######################################")

	    sys.exit(13)

    return b

#--------------------------------------
def validate_config_admin(which_b = '', which_config = 'config_admin_ini', which_linkage = JIRA_Linkage):
#--------------------------------------

    if JIRA_Linkage.pass_jira_source:

        log_and_print("validate_config_admin has JIRA_Linkage: " + JIRA_Linkage.pass_jira_source + " user: " + JIRA_Linkage.pass_jira_user + " password <secret>")

        if (JIRA_Linkage.pass_jira_user and JIRA_Linkage.pass_jira_pw):

            return JIRA_Linkage.pass_jira_user, JIRA_Linkage.pass_jira_pw

        log_and_print("Calling_tools_parse_config.py using ParseConfig to validate config_admin.ini")

        user, pasw = which_b.read_config_admin_admin('.', 'config_admin.ini')

        return user, pasw 

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


if len(pass_config) > 1:

    validate_exists(pass_config)

else:

    log_and_print("#########################################")

    log_and_print("ERROR: no config passed into igapa2_linkage: pass_config")

    log_and_print("#########################################")

    raise AttributeError("#Error: " + os.path.basename(__file__) + ": " + "Did not receive Config File. We require -c parameter. Aborting with no action taken.")


    raise Exception("#Error: " + os.path.basename(__file__) + ": " + "Did not receive Config File. We require -c parameter. Aborting with no action taken.")

    return_fake_error()


if pass_jira_source:

    vc = validate_config('', pass_config)

    validate_exists('config_admin.ini') # Add - if fail are JIRA credentials provided.

    JIRA_Linkage.pass_jira_user, JIRA_Linkage.pass_jira_pw  = validate_config_admin(vc, 'config_admin_ini', JIRA_Linkage)

    log_and_print("JIRA_Linkage.pass_jira_user " + JIRA_Linkage.pass_jira_user + " | JIRA_Linkage.pass_jira_pw: <secret>")

log_and_print("#-------------------------------------")

log_and_print("calling igapa2_main.py")

log_and_print("#-------------------------------------")

subr_rc = subprocess.call(["python", dir_path + "/" + "igapa2_main.py", pass_config
                                                                      , JIRA_Linkage.pass_jira_source
                                                                      , JIRA_Linkage.pass_jira_user
                                                                      , JIRA_Linkage.pass_jira_pw
                                                                      , DB_Linkage.pass_host
                                                                      , DB_Linkage.pass_port
                                                                      , DB_Linkage.pass_user
                                                                      , DB_Linkage.pass_pw
                                                                      , DB_Linkage.pass_schema])






