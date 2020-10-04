#######################################
# Name: jira_download.py
# Desc: Provide numeric part of EXA-ticket
#       and download the attachments
# 
#----------------------------------------------------------------Modules
import sys, os

try:

    import logging

except:

    os.system('pip install logging')

    import logging

try:

    from datetime import datetime as dt

except:

    os.system('pip install datetime')

    from datetime import datetime as dt

now = dt.today().strftime('%Y-%m-%d-%H:%M:%S')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

logging_filename = os.path.basename(__file__)[0:(os.path.basename(__file__).index('.py'))] + '.log'

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

#######################################
# FUNCTIONS (out of place but I nee to log and print errors)
#######################################
#--------------------------------------
def log_and_print(msg = ''):

    print("# " + os.path.basename(__file__) + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)

########################################
# CONTINUE SETTIN UP
########################################
try:

    from subr_validate_ticket import ticket_validation

except:

    log_and_print("########################################")

    log_and_print("# Error: " + os.path.basename(__file__))

    log_and_print("# program subr_validate_ticket.py not found")

    log_and_print("# so we are unable to validate the ticket.")

    log_and_print("# Aborting with no action taken...")

    log_and_print("########################################")

    sys.exit(13)

try:

    import csv

except:

    os.system('pip install csv')

    import csv

try:

    import json

except:

    os.system('pip install json')

    import json

try:

    import requests

except:

    os.system('pip install requests')

    import requests

try:

    from datetime import datetime as dt

except:

    os.system('pip install datetime')

    from datetime import datetime as dt

try:
    
    import configparser

except:
    
    os.system('pip install configparser')
    
    import configparser

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
# MAIN LOGIC
#######################################

log_and_print("#--------------------------------------#")

log_and_print("# Entering " + os.path.basename(__file__))

log_and_print(("#--------------------------------------#"))

from igapa2_linkage import *

if len(sys.argv) == 1:

    pass_jira_source = 28615

    log_and_print("Using DEFAULT (testing) pass_jira_source: " + str(pass_jira_source))

else:

    msg = ("received igapa2_linkage: " + pass_config + ", " + pass_jira_source + ", " +  pass_jira_user + ", " + " <secret> " +  pass_host + ", " + pass_port + ", " + pass_user + ", " + pass_pw + ", " + pass_schema)

log_and_print(msg)
 
log_and_print()

log_and_print("#####################################")

log_and_print("# Entering  with  ticket " + str(pass_jira_source))

log_and_print("#####################################")

log_and_print()

now = dt.today().strftime('%Y%m%d-%H%M%S')

log_and_print("Calling subr_validate_ticket.py with : " + str(pass_jira_source))

a = ticket_validation(pass_jira_source)

myTicket= a.ticket_validate_number() # Your ticket: EXA-1234x

log_and_print("created myTicket as : " + str(myTicket))


work_ticket = 0

class_chart = "DB_SIZE"

try:

    b = ParseConfig(class_chart)

except Exception as e:

    logger.error("#######################################")

    logger.error("FATAL: " +  os.path.basename(__file__))

    logger.error("# Unable to reference ParseConfig using:")

    logger.error("# b = ParseConfig(class_chart)")

    logger.error("# Does pgm tools_parse_config.py exist in " +  os.getcwd(),"?" )

    logger.error("# Aborting with no action taken.")

    logger.error(e, exc_info = True)

    logger.error("#######################################")

    print("#######################################")

    print("FATAL:", os.path.basename(__file__))

    print("# Unable to reference ParseConfig using:")

    print("# b = ParseConfig(class_chart)")

    print("# Does pgm tools_parse_config.py exist in", os.getcwd(),"?" )

    print("# Aborting with no action taken.")

    print("#######################################")

    print(e)

    sys.exit(13)

if pass_jira_source:

    if (( pass_jira_user ) and (pass_jira_pw)):

        user = pass_jira_user

        pasw = pass_jira_pw

    else:

        user, pasw = b.read_config_admin_admin('.', 'config_admin.ini')

else:

    user, pasw = b.read_config_admin_admin('.', 'config_admin.ini')

log_and_print("#--------------------------------------")

log_and_print("using JIRA credentials for user " + user)

log_and_print("#--------------------------------------")

print()

jiraURL = 'https://www.exasol.com/support/rest/api/2/issue/EXA-'

attachment_final_url="" # To validate if there are or not attachments

log_and_print("#--------------------------------------")

log_and_print("processing ticket for myTicket: " + str(myTicket) + " --> Will be converted to EXA-" + str(myTicket))

log_and_print("#--------------------------------------#")

print()

save_dir = os.getcwd()

#-------------------------------------#
def main() :
#-------------------------------------#
    global myTicket
    
    myTicket = str(myTicket)

    try:
        
        log_and_print("making URL Call: " + jiraURL + myTicket)

        r = requests.get(jiraURL+myTicket, auth=(user, pasw),timeout=5)

    except Exception as e:

        log_and_print("#####################################")

        log_and_print("# Error ")

        log_and_print("Unable to find ticket " +  str(myTicket))

        log_and_print("Aborting with no action taken.")

        log_and_print("#####################################")

        log_and_print(e, exc_info = True)



        sys.exit(13)

    # status of the request
    rstatus = r.status_code

    work_ticket = str('EXA-' + str(myTicket))

    if rstatus == 200:

        data = r.json()
#-------------------------------------#
# Create new directory same as ticket
#-------------------------------------#

        if os.path.exists(work_ticket):

            try:
                
                dest_dir = str(work_ticket + '_' + now)

                os.rename(work_ticket, dest_dir )

                log_and_print("renaming " + str(work_ticket) + " to " + dest_dir)

            except:

                logging.info("#-------------------------------------#")

                logging.info("# WARNING: " +  os.path.basename(__file__) + " unable to rename")

                logging.info("# from: " +  str(work_ticket) +  " to " +  dest_dir)

                logging.info("#-------------------------------------#")

     
        work_dir = os.path.join(save_dir, work_ticket)

        os.mkdir(work_ticket)

        log_and_print("saving work in: " + work_dir)

        #######################################
        # C H A N G I N G    D I R E C T O R Y
        #######################################

        os.chdir(work_ticket)

    else:

        log_and_print("#####################################")

        log_and_print("Error: accessing JIRA with return code: " + str(rstatus))

        log_and_print("Unable to process ticket " +  work_ticket)

        log_and_print("# ---> Does ticket " + work_ticket + " even exist?")

        log_and_print("# ---> For ticket " + work_ticket + " Do you have access permission on JIRA?")

        log_and_print("had URL read return code: " + str(rstatus))

        log_and_print("Aborting with no action taken.")

        log_and_print("#####################################")

        sys.exit(13)

    if not data['fields']['attachment'] :

        status_attachment = 'ERROR: Nothing attached'

        attachment_final_url=""

        log_and_print()

        log_and_print("#####################################")

        log_and_print("# " + os.path.basename(__file__) + " WARNING")

        log_and_print("#  No Attachments found for " +  work_ticket)

        log_and_print("# The folder " +  work_ticket, "will be empty")

        log_and_print("# and no reports will be run")

        log_and_print("#####################################")

        log_and_print()

        sys.exit(13)

    else:

        for i in data['fields']['attachment'] :

             attachment_final_url = i['content']
            
             attachment_filename = i['filename']
            
             status_attachment_name = 'OK: The desired attachment exists: ' + attachment_filename
            
             log_and_print("trying to download " + attachment_final_url)

             attachment_name = False
            
             attachment_amount = False
            
             attachment_files = False
            
             if attachment_final_url != "" :
            
                 r = requests.get(attachment_final_url, auth=(user, pasw), stream=True)
            
                 with open(attachment_filename, "wb") as f:
            
                     f.write(r.content.decode('iso-8859-1').encode('utf8'))
            
                 f.close()
            
             else:
            
               print ("no file")

    #-------------------------------------#
    # C H A N G E   D I R E C T O R Y
    #-------------------------------------#
    os.chdir(save_dir)

if __name__ == "__main__" :

    main() 

log_and_print("#-------------------------------------#")

log_and_print("successfully exited")

log_and_print("#-------------------------------------#")