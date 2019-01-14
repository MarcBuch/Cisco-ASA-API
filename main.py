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
import authentication
import asa
import acl

urllib3.disable_warnings()

#Gets Token from ASA and stores it in an header.
token = authentication.Token
Header = authentication.Header


rule_json = json.dumps(acl.ACL_dict)                    #Read JSON File
aclName = 'pyTest'
acl = asa.add_ext_acl(asa.IP, aclName, rule_json)       #Upload ACL to ASA
print(acl)
ext_acl = asa.get_all_ext_acl(asa.IP)                   #Read all ACL from ASA
print(ext_acl)
delete = authentication.del_X_auth_token(token, asa.IP) #Delete Authentication Token
