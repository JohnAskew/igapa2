'''
name: _igapa_linkage.py
desc: hold the parameter arguments to pass to other pgms.
usage: none, this is a utility.
'''
import os

import sys

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
    def set_jira_source(cls, in_jira_source):

    	cls.pass_jira_source = in_jira_source

    @classmethod
    def set_config(cls, in_config):

        cls.pass_config = in_config

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

if __name__ == "__main__":

	pass




