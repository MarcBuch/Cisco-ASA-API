#!/usr/bin/python
# coding : utf-8

'''
Created on 12.10.2018
@author: MBU
'''

if __name__ == '__main__':
    pass

import requests
import urllib3
import json
import asa

urllib3.disable_warnings()

IP = ''
URL = 'https://' + IP

#Gets Token from ASA, needs an IP-Address
def get_X_auth_token(ip):
    token = None
    username = ''
    password = ''
    #Directory of the ASA Tokenservice
    url = 'https://'+ username + ':' + password + '@' + ip + '/api/tokenservices'
    headers = {'Content-Type':"application/json"}
    payload = ""
    # Send POST Request to ASA, containing Username and Password in URL, empty payload, JSON Header. It doesn't verify SSL Cetificate!
    r = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
    #Check if response got received, if not print an error message
    if(not r):
        print("No Data returned")
    #Search for the token in the header and stores the value.
    else:
        token = r.headers['x-auth-token']
    return token

#Delete Token on ASA
def del_X_auth_token(token, ip):
    url = URL + '/api/access/in'
    headers = Header
    r = requests.delete(url, headers = headers, verify = False)

Token = get_X_auth_token(IP)
Header = {
        'X-Auth-Token': Token,
        'Content-Type':"application/json"   }