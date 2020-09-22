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

######################################
class GetDF:
#######################################
#-------------------------------------#
    def __init__(self, myconfig = 'DB_SIZE', which_config = 'config_reports.ini'):
#-------------------------------------#

        self.myconfig = myconfig

        self.which_config = which_config

        my_pgm = os.path.basename(__file__)

        logger = logging.getLogger()

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

        logging_filename = my_pgm[0:(my_pgm.index('.py'))] + '.log'

        logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

        logging.info("#--------------------------------------#")

        logging.info("# Entering " + os.path.basename(__file__))

        logging.info("#--------------------------------------#")

        logging.info("# " + os.path.basename(__file__) + " Class GetDF received section heading: " + self.myconfig + " using this config file: " + self.which_config)


#-------------------------------------#
    def __repr__(self):
#-------------------------------------#

        return(f'{self.__class__.__name__}('
               
               f'{self.myconfig!r}, {self.which_config!r})')

    

#-------------------------------------#
    def run(self, path = '.', which_config = 'config_reports.ini'):
#-------------------------------------#
        config = configparser.ConfigParser()

        config.read(path + '/' + which_config)

        logging.info("# " + os.path.basename(__file__) + " reading : " + path + '/' + self.which_config )

        self.tbls_list = []

        for section in config.sections():

            if config[section]['CONFIG_HOURLY_TBL'] not in self.tbls_list:

                self.tbls_list.append(config[section]['CONFIG_HOURLY_TBL'])

                logging.info("# " + os.path.basename(__file__) + " returning " + config[section]['CONFIG_HOURLY_TBL'] )

            if config[section]['CONFIG_DAILY_TBL'] not in self.tbls_list:

                self.tbls_list.append(config[section]['CONFIG_DAILY_TBL'])

                logging.info("# " + os.path.basename(__file__) + " returning " + config[section]['CONFIG_DAILY_TBL'] )

        return self.tbls_list

         



#######################################
# MAIN LOGIC
#######################################

if __name__ == '__main__':

    a = GetDF('DB_SIZE', 'config_reports.ini')

    my_output = a.run()

    for table in my_output:

        logging.info("# " + os.path.basename(__file__) + " calling export_cloud_to_csv.py with " + table)

        subr_rc = subprocess.call(["python", "./" + "export_cloud_to_csv.py", table])


