#!/usr/bin/python

'''
 Author:    Calum Hunter                                  
 Date:      09-08-2018                                     
 Version:   1.0                                           
 Purpose:   Return currently installed Jenkins plugins                                         
'''

import requests
import json
import sys

# Set up our variables
#JENKINS = ''
#USER = ''
#APITOKEN = ''
JENKINS = raw_input('Provide the Jenkins instance IP/DNS and port number (eg 172.30.3.118:8080) : ')
USER = raw_input('Provide the user account name to login to the Jenkins API with: ')
APITOKEN = raw_input('Provide the above user account\'s API Token: ')

# Place our groovy script between the three ''' to store it as a multi line var
# this will find all 'active' plugins and only plugins that are _NOT_
# installed by being a dependency of another plugin.
GROOVY_SCRIPT = '''
jenkins.model.Jenkins.instance.getPluginManager().getPlugins()
		.findAll { plugin -> plugin.isActive() }
    	.each {
          if ( "${it.hasDependants()}" == "false" ) {
    		println "${it.getShortName()}"
        	}
        }
null
'''

# Use this function to run our GROOVY_SCRIPT
def get_all_plugins(SCRIPT):
	global JENKINS
	global USER
	global APITOKEN
	AUTH = (USER, APITOKEN)
	URL = 'http://' + JENKINS + '/scriptText'
	PAYLOAD = {'script' : SCRIPT}
	request_result = requests.post(URL, data=PAYLOAD, auth=AUTH) 
	return request_result

# Store the result of our request into a variable called RESULT as a list
RESULT = get_all_plugins(GROOVY_SCRIPT).text
RESULT = sorted(RESULT.splitlines())

for result in RESULT:
	print result
