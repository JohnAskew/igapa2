import os

import sys

my_pgm = sys.argv[0] #os.path.basename(__file__)

my_log = my_pgm[0:(my_pgm.index('.py'))] + '.log'

try:

	import logging

except:

	os.system('pip install logging')

	import logging

#######################################
# Set up logging
#######################################

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

file_handler = logging.FileHandler(my_log)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

if __name__ == '__main__':

	logger.info("This is a test line for running tools_logger.py")