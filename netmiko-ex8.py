#!/usr/bin/env python

import json
from getpass import getpass
import netmiko

# define all possible exceptions that you can encounter
# here Connection timeout and Authentication failure are captured.
netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)
config_commands = ['logging buffered 19999'] 

if __name__=="__main__":
    username = raw_input('Enter username:')
    password = getpass()
    pynet_rtr2 = {
                     "ip" : "184.105.247.71",
                     "device_type" : "cisco_ios",
                     "username" : username,
                     "password" : password,
                     "port" : 22
                 }
    try:
        conn = netmiko.ConnectHandler(**pynet_rtr2)  # pass whole dictionary
    except netmiko_exceptions as e:
        print e  # just print exception
        exit() # terminate program.
    print conn.find_prompt() # print which device is being accessed
    outp = conn.send_config_from_file('config_file.txt')
    print outp
    conn.disconnect()

