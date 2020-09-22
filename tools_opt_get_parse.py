''' name: tools_opt_get_parse.py
 desc: To read in runtime overrides 
       to the existing config files.
 usage: python tools_opt_get_parse.py -h
 '''
import os

import sys

import getopt

######################################
# FUNCTIONS - putting the fun back in programming
######################################
def usage():
#-------------------------------------
     print("######################################")
     print("# tools_opt_get_parse parameters")
     print("######################################")
     print("# -c    Config_file override. Replaces default config file config_reports.ini")
     print("# -j    Jira Source. The JIRA ticket number which has the CSV attachments")
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
config_in =''
js_in =''
ju_in =''
jp_in = ''
host_in = ''
port_in = ''
u_in = ''
p_in = ''
s_in = ''

#args  = '-c -js -ju -jp -host -port -u -p -h'.split()

try:
	opts, args = getopt.getopt(sys.argv[1:], "c:j:k:l:m:n:p:u:s:h")

except getopt.GetoptError:

	print(my_pgm + " had errors")

	sys.exit(2)

for opt,arg in opts:
	if opt == '-l':
		jp_in = arg
	if opt == '-j':
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
	elif opt == '-h':
		usage()
		sys.exit(0)

print("config_in: ", config_in)
print("js_in =", js_in)
print("ju_in =", ju_in)
print("jp_in =", jp_in)
print("host_in =", host_in)
print("port_in =", port_in)
print("u_in =", u_in)
print("p_in =", p_in)
print("s_in =", s_in)

