''' 
name: igapa2_linkage.py
desc: hold linkage between programs
usage: None - it's a utility
'''
import sys

import os

#######################################
class Class_JIRA(object):
#######################################

    def __init__(self, pass_config='config_reports.ini', pass_jira_source='', pass_jira_user='', pass_jira_pw=''):

        self.pass_config      = pass_config

        self.pass_jira_source = pass_jira_source

        self.pass_jira_user   = pass_jira_user

        self.pass_jira_pw     = pass_jira_pw

    @classmethod
    def set_config(cls, in_config):

        cls.pass_config = in_config

    @classmethod
    def set_jira_source(cls, in_jira_source):

    	cls.pass_jira_source = in_jira_source

    @classmethod
    def set_jira_user(cls, in_jira_user):

    	cls.pass_jira_user = in_jira.pass_user

    @classmethod
    def set_jira_pw(cls, in_jira_pw):

        cls.pass_jira_pw = in_jira_pw

#######################################
class Class_DB(object):
#######################################

    def __init__(self, pass_config='config_reports.ini', pass_host='', pass_port='', pass_user='', pass_pw='', pass_schema=''):

        self.pass_config      = pass_config

        self.pass_host        = pass_host

        self.pass_port        = pass_port

        self.pass_user        = pass_user

        self.pass_pw          = pass_pw

        self.pass_schema      = pass_schema

    @classmethod
    def set_config(cls, in_config):

        cls.pass_config = in_config

    @classmethod
    def set_host(cls, in_host):

    	cls.pass_host = in_host

    @classmethod
    def set_port(cls, in_port):

    	cls.pass_port = in_port

    @classmethod
    def set_user(cls, in_user):

    	cls.pass_user = in_user

    @classmethod
    def set_pw(cls, in_pw):

    	cls.pass_pw = in_pw

    @classmethod
    def set_schema(cls, in_schema):

    	cls.pass_schema = in_schema

#######################################
class Pass_Arguments(object):
#######################################

    def __init__(self, pass_config='config_reports.ini', pass_jira_source='', pass_jira_user='', pass_jira_pw='', pass_host='', pass_port='', pass_user='', pass_pw='', pass_schema=''):

        self.pass_config      = pass_config

        self.pass_jira_source = pass_jira_source

        self.pass_jira_user   = pass_jira_user

        self.pass_jira_pw     = pass_jira_pw

        self.pass_host        = pass_host

        self.pass_port        = pass_port

        self.pass_user        = pass_user

        self.pass_pw          = pass_pw

        self.pass_schema      = pass_schema

  
    @classmethod
    def set_config(cls, in_config):

        cls.pass_config = in_config

    @classmethod
    def set_jira_source(cls, in_jira_source):

    	cls.pass_jira_source = in_jira_source

    @classmethod
    def set_jira_user(cls, in_jira_user):

    	cls.pass_jira_user = in_jira.pass_user

    @classmethod
    def set_jira_pw(cls, in_jira_pw):

        cls.pass_jira_pw = in_jira_pw

    @classmethod
    def set_host(cls, in_host):

    	cls.pass_host = in_host

    @classmethod
    def set_port(cls, in_port):

    	cls.pass_port = in_port

    @classmethod
    def set_user(cls, in_user):

    	cls.pass_user = in_user

    @classmethod
    def set_pw(cls, in_pw):

    	cls.pass_pw = in_pw

    @classmethod
    def set_schema(cls, in_schema):

    	cls.pass_schema = in_schema

#######################################
# MAIN LOGIC
#######################################

dir_path = os.getcwd()


if len(sys.argv) > 1:

	pass_config      = sys.argv[1]

else:

	pass_config = ''

if len(sys.argv) > 2:

	pass_jira_source = sys.argv[2]

else:

	pass_jira_source = ''

if len(sys.argv) > 3:

	pass_jira_user   = sys.argv[3]

else:

    pass_jira_user   = ''

if len(sys.argv) > 4:

	pass_jira_pw     = sys.argv[4]

else:

	pass_jira_pw     = ''

if len(sys.argv) > 5:

	pass_host        = sys.argv[5]

else:

	pass_host        = ''

if len(sys.argv) > 6:

	pass_port        = sys.argv[6]

else:

	pass_port        = ''

if len(sys.argv) > 7:

	pass_user        = sys.argv[7]

else:

	pass_user        = ''

if len(sys.argv) > 8:

	pass_pw          = sys.argv[8]

else:

	pass_pw          = ''

if len(sys.argv) > 9:

	pass_schema      = sys.argv[9]

else:

	pass_schema      = ''

X = Pass_Arguments(pass_config, pass_jira_source, pass_jira_user, pass_jira_pw,pass_host, pass_port, pass_user, pass_pw, pass_schema)

JIRA_Linkage = Class_JIRA(pass_config, pass_jira_source, pass_jira_user, pass_jira_pw)

DB_Linkage =   Class_DB(pass_config, pass_host, pass_port, pass_user, pass_pw, pass_schema)