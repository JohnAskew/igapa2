import os

from tools_logger import *


import sys

try:

    import configparser

except:

    os.system('pip install configparser')

    import configparser

try:

    from tools_parse_config import ParseConfig

except:
    
    msg = "Unable to find tools_parse_config.py"

    print("#######################################")

    print("# ERROR in", os.path.basename(__file__))
    
    print(msg)

    print("#", os.path.basename(__file__), "aborting with no action taken.")

    print("#######################################")

    sys.exit(13)

try:
	from pyexasol import ExaConnection

except:

	os.system('pip install pyexasol')

	from pyexasol import ExaConnection

#######################################
# GLOBAL VARIABLES
#######################################
sections_list =[]
sections_df_list =[0]
cnt_sections_list = 0
 
config_in = 'config_reports.ini'

CONFIG_HOURLY_TBL        = False
CONFIG_DAILY_TBL         = False
CONFIG_ROW1_COL_X_AXIS   = False
CONFIG_ROW1_COL_Y_AXIS_1 = False
CONFIG_ROW1_COL_Y_AXIS_2 = False
CONFIG_ROW2_COL_X_AXIS   = False
CONFIG_ROW2_COL_Y_AXIS_1 = False
CONFIG_ROW2_COL_Y_AXIS_2 = False
CONFIG_ROW3_COL_X_AXIS   = False
CONFIG_ROW3_COL_Y_AXIS_1 = False
CONFIG_ROW3_COL_Y_AXIS_2 = False
CONFIG_ROW4_COL_X_AXIS   = False
CONFIG_ROW4_COL_Y_AXIS_1 = False
CONFIG_ROW4_COL_Y_AXIS_2 = False

try:

    b = ParseConfig('DB_SIZE', 'config_reports.ini')

except Exception as e:

    print("#######################################")

    print("FATAL: " + os.path.basename(__file__))

    print("# " + os.path.basename(__file__) + " Unable to reference ParseConfig using:")

    print("# b = ParseConfig(class_chart)")

    print("# Does pgm tools_parse_config.py exist in " + os.getcwd(),"?" )

    print("# " + os.path.basename(__file__) + " Aborting with no action taken.")

 
    print(e)

    print("#######################################")

config_sections = b.read_config_sections(os.getcwd())

if len(config_sections) == 0:

    print("FATAL: " + os.path.basename(__file__))

    print("# " + os.path.basename(__file__) + " unable to reference ParseConfig using:")

    print("# config_sections = b.read_config_sections()")

    print("# Does pgm tools_parse_config.py exist in " + os.getcwd(),"?" )

    print("# " + os.path.basename(__file__) + " Aborting with no action taken.")

    sys.exit(13)

for item in config_sections:

    print("# " + os.path.basename(__file__) + " received this section from tool_parse_config: " + item)

#######################################
# LOOP for duration of the program
#
# #      # # #   # # #   #  #
# #      #   #   #   #   #    #
# #      #   #   #   #   #  #
# #      #   #   #   #   #
# # # #  # # #   # # #   #
# 
########################################


for config_section in config_sections:

    process_section = ParseConfig(config_section, config_in)

    CONFIG_HOURLY_TBL,CONFIG_DAILY_TBL,CONFIG_ROW1_COL_X_AXIS,CONFIG_ROW1_COL_Y_AXIS_1,CONFIG_ROW1_COL_Y_AXIS_2,CONFIG_ROW2_COL_X_AXIS,CONFIG_ROW2_COL_Y_AXIS_1,CONFIG_ROW2_COL_Y_AXIS_2,CONFIG_ROW3_COL_X_AXIS,CONFIG_ROW3_COL_Y_AXIS_1,CONFIG_ROW3_COL_Y_AXIS_2,CONFIG_ROW4_COL_X_AXIS,CONFIG_ROW4_COL_Y_AXIS_1,CONFIG_ROW4_COL_Y_AXIS_2 = process_section.run(os.getcwd())

    if CONFIG_ROW1_COL_X_AXIS:

        if  CONFIG_ROW1_COL_Y_AXIS_1:

            if CONFIG_ROW1_COL_Y_AXIS_2:

               COLS_TBL1 = [CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1, CONFIG_ROW1_COL_Y_AXIS_2]

            else:

                COLS_TBL1 = [CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1]
    else:

        COLS_TBL1 = False

    if   CONFIG_ROW2_COL_X_AXIS:

        if  CONFIG_ROW2_COL_Y_AXIS_1:

            if CONFIG_ROW2_COL_Y_AXIS_2:

               COLS_TBL2 = [CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1, CONFIG_ROW2_COL_Y_AXIS_2]

            else:

                COLS_TBL2 = [CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1]
    else:
        
        COLS_TBL2 = False


    if   CONFIG_ROW3_COL_X_AXIS:

        if  CONFIG_ROW3_COL_Y_AXIS_1:

            if CONFIG_ROW3_COL_Y_AXIS_2:

               COLS_TBL3 = [CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2]

            else:

                COLS_TBL3 = [CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1]
    else:
        
        COLS_TBL3 = False

    if   CONFIG_ROW4_COL_X_AXIS:

        if  CONFIG_ROW4_COL_Y_AXIS_1:

            if CONFIG_ROW4_COL_Y_AXIS_2:

               COLS_TBL4 = [CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1, CONFIG_ROW4_COL_Y_AXIS_2]

            else:

                COLS_TBL4 = [CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1]
    else:
        
        COLS_TBL4 = False

    logger.info("# " + os.path.basename(__file__) + " Processing\tConfig section:\t " + config_section)

    logger.info("# " + os.path.basename(__file__) + " Processing\tCONFIG_HOURLY_TBL:\t " + CONFIG_HOURLY_TBL)

    logger.info("# " + os.path.basename(__file__) + " Processing\tCONFIG_DAILY_TBL:\t " +  CONFIG_DAILY_TBL)

    print()

    print("COLS_TBL1", COLS_TBL1)

    print("COLS_TBL2", COLS_TBL2)

    print("COLS_TBL3", COLS_TBL3)

    print("COLS_TBL4", COLS_TBL4)



#######################################
# MAIN LOGIC
#######################################

if __name__ == '__main__':
	
    pass