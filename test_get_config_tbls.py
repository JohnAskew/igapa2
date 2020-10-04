import os

from tools_logger import *

try:

    import configparser

except:

    os.system('pip install configparser')

    import configparser

try:

    import subprocess

except:

    os.system('pip install subprocess')

    import subprocess

from igapa2_linkage import *

#######################################
# FUNCTIONS
#######################################
#--------------------------------------
def log_and_print(msg = ''):
#--------------------------------------

    print("# " + os.path.basename(__file__) + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)

######################################
class GetDF(object):
#######################################
#-------------------------------------#
    def __init__(self, myconfig = 'DB_SIZE', which_config = pass_config):
#-------------------------------------#

        self.myconfig = myconfig

        self.which_config = which_config

        my_pgm = os.path.basename(__file__)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

        logging_filename = my_pgm[0:(my_pgm.index('.py'))] + '.log'

        logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

        log_and_print()

        log_and_print("CALLED class --> GetDF received section heading: " + self.myconfig + " using this config file: " + self.which_config)

        log_and_print()


#-------------------------------------#
    def __repr__(self):
#-------------------------------------#

        return(f'{self.__class__.__name__}('
               
               f'{self.myconfig!r}, {self.which_config!r})')

    
#-------------------------------------#
    def run(self, which_config, path = '.'):
#-------------------------------------#

        config = configparser.ConfigParser()

        config.read(path + '/' + which_config)

        log_and_print()

        log_and_print("CALLED class --> run: reading config: " + path + '/' + self.which_config )

        log_and_print()

        self.tbls_list = []

        for section in config.sections():

            if config[section]['CONFIG_HOURLY_TBL'] not in self.tbls_list:

                self.tbls_list.append(config[section]['CONFIG_HOURLY_TBL'])

                log_and_print("returning " + config[section]['CONFIG_HOURLY_TBL'] )

            if config[section]['CONFIG_DAILY_TBL'] not in self.tbls_list:

                self.tbls_list.append(config[section]['CONFIG_DAILY_TBL'])

                log_and_print("returning " + config[section]['CONFIG_DAILY_TBL'] )

        return self.tbls_list

         



#######################################
# MAIN LOGIC
#######################################

log_and_print("#--------------------------------------#")

log_and_print("# Entering " + os.path.basename(__file__))

log_and_print("#--------------------------------------#")

if __name__ == '__main__':

    a = GetDF('DB_SIZE', pass_config)

    my_output = a.run(pass_config, '.')

    msg_info = ("Executing call export_cloud_to_csv.py with DB_Linkage.pass_host: " 
                 + DB_Linkage.pass_host
                 + " pass_port: "
                 + DB_Linkage.pass_port
                 + " pass_user: "
                 + DB_Linkage.pass_user
                 + " pass_pw: <secret> "
                 + " pass_schema: "
                 + DB_Linkage.pass_schema
                 )

    log_and_print(msg_info)

    for table in my_output:

        log_and_print()

        log_and_print("calling export_cloud_to_csv.py with config:" + pass_config
                                                                    + " pass_jira_source: " + pass_jira_source
                                                                    + " pass_jira_user " + pass_jira_user
                                                                    + " pass_host " + pass_host
                                                                    + " pass_port " + pass_port
                                                                    + " pass_user " + pass_user
                                                                    + " pass_schema " + pass_schema
                                                                    + " table " + table)

        log_and_print()

        subr_rc = subprocess.call(["python", "./" + "export_cloud_to_csv.py"
                                                   , pass_config
                                                   , pass_jira_source
                                                   , pass_jira_user
                                                   , pass_jira_pw
                                                   , pass_host
                                                   , pass_port
                                                   , pass_user
                                                   , pass_pw
                                                   , pass_schema
                                                   , table
                                                   ])
        if subr_rc > 0:

            log_and_print("########################################")

            log_and_print("ERROR: call to export_cloud_to_csv failed. See export_cloud_to_csv.log for details. Aborting.")

            log_and_print("########################################")

            sys.exit(12)




