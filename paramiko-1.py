#!/usr/bin/env python


import paramiko
from getpass import getpass
from time import sleep

if __name__ == "__main__":
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    password = getpass()
    port = 22

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.load_system_host_keys()
#    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        remote_conn_pre.connect(ip_addr,username = username, password = password, look_for_keys = False, allow_agent = False, port = port)
    except:
        pass
    remote_conn = remote_conn_pre.invoke_shell()


    outp = remote_conn.recv(1000)
    print outp
#    stdin,stdout,strerr  = remote_conn_pre.exec_command('show ip int br\n')
#    print stdout.read()

    remote_conn.send("show ip int br\n")
    sleep(5)
    outp = remote_conn.recv(5000)
    print outp

    remote_conn.send("terminal len 0\n")
    sleep(2)
    remote_conn.send("show version\n")
    sleep(2)
    while remote_conn.recv_ready():
        outp += remote_conn.recv(5000)

    print outp
