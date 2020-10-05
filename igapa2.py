''' name: tools_opt_get_parse.py
 desc: To read in runtime overrides 
       to the existing config files.
 usage: python tools_opt_get_parse.py -h
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

    import getopt

except:

	os.system('pip install getopt')

	import getopt

from igapa2_linkage import *

try:

	import subprocess

except:

	os.system('pip install subprocess')

	import subprocess



######################################
# FUNCTIONS - putting the fun back in programming
######################################
#--------------------------------------
def log_and_print(msg = "Error: Nothing passed to log_and_print."):
#--------------------------------------

    print("# " + my_pgm + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)

#--------------------------------------
def usage():
#-------------------------------------
     print("######################################")
     print("# igapa2.py parameters")
     print("######################################")
     print("# -c    Config_file override. You must specify which config to use for reporting.")
     print("#          --> The default config included is config_reports.ini.")
     print("# -j    Jira Source. The JIRA ticket which has the CSV attachments. Specified as a number; leave off the EXA- prefix")
     print("# -k    Jira user. Logon credential for JIRA. Overrides config_admin.ini")
     print("# -l    Jira password. Logon credential for JIRA. Overrides config_admin.ini")
     print("# -m    Database host name or I.P. address. Overrides _config.py")
     print("# -n    Database host port. Overrides _config.py")
     print("# -u    Database user logon credential. Overrides _config.py")
     print("# -p    Database user password credential. Overrides _config.py")
     print("# -s    Database schema. Overrides _config.py")
     print("# -h    Usage help")
     print("#-------------------------------------")

######################################
# MAIN LOGIC
######################################
my_pgm = os.path.basename(__file__)

my_path = os.getcwd()

now = dt.today().strftime('%Y-%m-%d-%H:%M:%S')

logging_filename = os.path.basename(__file__)[0:(os.path.basename(__file__).index('.py'))] + '.log'

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')


log_and_print("#--------------------------------------#")

log_and_print("# Entering " + os.path.basename(__file__))

log_and_print("#--------------------------------------#")


dir_path = os.getcwd()

config_in =''
js_in =''
ju_in =''
jp_in = ''
host_in = ''
port_in = ''
u_in = ''
p_in = ''
s_in = ''

if len(sys.argv) == 1:

	usage()

	sys.exit(0)

try:
	opts, args = getopt.getopt(sys.argv[1:], "c:j:k:l:m:n:p:u:s:h")

except getopt.GetoptError:

	log_and_print("had errors in parsing the arguments. Aborting with no action taken.")

	usage()

for opt,arg in opts:
    if opt == '-h':

    	usage()

    	sys.exit(0)

    elif opt == '-l':

    	jp_in = arg

    elif opt == '-j':

    	js_in = arg

    elif opt == '-k':

    	ju_in = arg

    elif opt == '-c':

    	config_in = arg

    elif opt == '-m':

    	host_in = arg

    elif opt == '-n':

    	port_in = arg

    elif opt == '-u':

    	u_in = arg

    elif opt == '-p':

    	p_in = arg

    elif opt == '-s':

    	s_in = arg

msg = (my_pgm + " is calling igapa_linkage.py to create object X=Pass_Arguments.")

log_and_print(msg)

X = Pass_Arguments(config_in, js_in, ju_in, jp_in, host_in, port_in, u_in, p_in, s_in)

msg = ("--> is passing igapa_linkage.py CONFIG parameter " +  X.pass_config)

log_and_print(msg)

if X.pass_jira_source:
	
	msg = ("--> is passing igapa_linkage.py JIRA parameters JIRA_ticket " +  X.pass_jira_source + ", " + " JIRA _user " + X.pass_jira_user + ", " + " JIRA_pw <secret>" )

	log_and_print(msg)

elif X.pass_host:
	
	msg = ("--> is passing igapa_linkage.py DB Connect parameters Host: " + X.pass_host + ", User: " + X.pass_user + ", Password: <secret> " + ", Schema: " + X.pass_schema)

	log_and_print(msg) 

else:

    msg = ("--> Using default _config_py.py settings to process the database and credentials. See program export_cloud_to_csv.py for processing")
    
    log_and_print(msg) 

log_and_print("#-------------------------------------")

log_and_print("calling igapa2_validate_config_db.py")

log_and_print("#-------------------------------------")

'''
If you use the -j option to specify we want to pull from a ticket,
then we look as Xpass_jira_source. 
If NOT (you did not specify the -j parameter) then skip this paragraph
and look for the -m option.

The default is to read the database host from the file _config.py 
and pull from the database if you only execute with the -c parameter
which specifies which reporting configuration to use.
'''
if X.pass_config:

	pass

else:

	msg = ("ERROR: Parameters found but missing -c parameter which is required. Aborting with no action taben.")

	log_and_print("#######################################")

	log_and_print(msg)

	log_and_print("Aborting with unsuccessful exit.")

	log_and_print("#######################################")

	assert(X.pass_config), msg


if X.pass_jira_source:

	tools_rc = subprocess.call(["python", dir_path + "/" + "igapa2_validate_config_jira.py", X.pass_config
		                                                                                        , X.pass_jira_source
		                                                                                        , X.pass_jira_user
		                                                                                        , X.pass_jira_pw
		                                                                                        , X.pass_host
		                                                                                        , X.pass_port
		                                                                                        , X.pass_user
		                                                                                        , X.pass_pw
		                                                                                        , X.pass_schema])

	if tools_rc > 0:

		msg = ("received FATAL Error from igapa2_validate_config_jira. Check the logs for error messages. Aborting with no action taken.")

		log_and_print(msg)
 
		raise Exception("#Error: " + os.path.basename(__file__) + ": " + "Returned from call with " + str(tools_rc))
	####################
	# Exit for X.pass_jira_source being TRUE

	sys.exit(12)

	####################


try:

	subr_rc = subprocess.call(["python", dir_path + "/" + "igapa2_validate_config_db.py", X.pass_config
	                                                                                     , X.pass_jira_source
	                                                                                     , X.pass_jira_user
	                                                                                     , X.pass_jira_pw
	                                                                                     , X.pass_host
	                                                                                     , X.pass_port
	                                                                                     , X.pass_user
	                                                                                     , X.pass_pw
	                                                                                     , X.pass_schema])

except:

	log_and_print("######################################")

	log_and_print("Unable to call/find program igapa2_validate_config_db.py")

	log_and_print("Aborting with no action taken.")

	log_and_print("--> Is igapa2_validate_config_db.py in the same directory as " + os.path.basename(__file__) + "?")

	log_and_print("--> Are there any logs for igapa2_validate_config_db?")

	log_and_print("--> Does the log for " + os.path.basename(__file__) + " report any errors?")

	log_and_print("######################################")

	sys.exit(12)

if subr_rc != 0:

    log_and_print("####################################")

    log_and_print( "ERROR: received return code " + str(subr_rc) + " from igapa2_validate_config_db.py")

    log_and_print( " Aborting with no action taken.")

    log_and_print("####################################")

    sys.exit(-1)

log_and_print("######################################")

log_and_print("Successfully exiting.")

log_and_print("######################################")