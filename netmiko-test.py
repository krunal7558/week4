#!/usr/bin/env python

import json
from getpass import getpass
import netmiko

# define all possible exceptions that you can encounter
# here Conneciton timeout and Authentication failure are captured.
netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)

if __name__=="__main__":
    username = raw_input('Enter username:')
    password = getpass()
    with open('devices.json') as fh:  #Take json file as input with devices
        devices=json.load(fh)

    for device in devices:
        device['username'] = username    # add username in dictionary
        device['password'] = password    # add password in dictionary
        print '#'*79
        try:
            conn = netmiko.ConnectHandler(**device)  # pass whole dictionary
        except netmiko_exceptions as e:
            print e  # just print exception
            continue  # do not terminate programe and continue to next element
        print conn.find_prompt() # print which device is being accessed
        outp = conn.send_command('show arp')
        print outp
        conn.disconnect()

