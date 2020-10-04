'''
name: igapa2_main.py
desc: Read arguments and manage all process 
      thru visualization.
usage: python igapa2_main.py (uses defaults from config files).
       To control processing and enter parameters/arguments 
       run > python igapa2.py <parameters>
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

	os.system('pip install subprocess')

	import subprocess

my_pgm = os.path.basename(__file__)

#######################################
# FUNCTIONS
#######################################
#--------------------------------------
def log_and_print(msg = ''):
#--------------------------------------

    print("# " + os.path.basename(__file__) + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)

#######################################
# MAIN PROCESSING
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

if len(sys.argv) ==1:

    log_and_print("was not passed any parameters linkage. Using config files to drive processing.")

else:

     pass

msg = ("calling igapa_master.py using igapa2_linkage: " + pass_config + ", " + pass_jira_source + ", " +  pass_jira_user + ", " + "<secret>" + ", " +  pass_host + ", " + pass_port + ", " + pass_user + ", " + "<secret>" + ", " + pass_schema)

log_and_print(msg)

subr_rc = subprocess.call(["python", dir_path + "/" + "igapa_master.py", pass_config, pass_jira_source, pass_jira_user, pass_jira_pw, pass_host, pass_port, pass_user, pass_pw, pass_schema])

if subr_rc != 0:

    log_and_print("####################################")

    log_and_print( "ERROR: received return code " + str(subr_rc) + " from igapa_master.py")

    log_and_print( " Aborting with no action taken.")

    log_and_print("####################################")

    sys.exit(-1)

