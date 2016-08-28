pynet_rtr1 = {
    'device_type': 'cisco_ios',
    'ip':   '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
    'secret': 'secret',
    'verbose': False
}

pynet_rtr2 = {
    'device_type': 'cisco_ios',
    'ip':   '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    'secret': 'secret',
    'verbose': False
}


pynet_jnpr_srx1 = {
    'device_type': 'cisco_asa',
    'ip':   '184.105.247.76',
    'username': 'admin',
    'password': '88newclass',
    'secret': 'secret',
    'verbose': False
}

pynet_sw1 = {
    'device_type': 'arista_eos',
    'ip':   '184.105.247.72',
    'username': 'admin1',
    'password': '99saturday',
    'secret': '',
    'port': 22,
    'verbose': False
}

pynet_sw2 = {
    'device_type': 'arista_eos',
    'ip':   '184.105.247.73',
    'username': 'admin1',
    'password': '99saturday',
    'secret': '',
    'port': 22,
    'verbose': False
}

pynet_sw3 = {
    'device_type': 'arista_eos',
    'ip':   '184.105.247.74',
    'username': 'admin1',
    'password': '99saturday',
    'secret': '',
    'port': 22,
    'verbose': False,
}

pynet_sw4 = {
    'device_type': 'arista_eos',
    'ip':   '184.105.247.74',
    'username': 'admin1',
    'password': '99saturday',
    'secret': '',
    'port': 22,
    'verbose': False
}


all_devices = [
    pynet_rtr1,
    pynet_rtr2,
    pynet_sw1,
    pynet_sw2,
    pynet_sw3,
    pynet_sw4,
    pynet_jnpr_srx1
]
