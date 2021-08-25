#!/usr/bin/env python3.9

import device

h1 = {
    'device_type': 'linux',
    'ip': '172.17.0.2',
    'username': 'test',
    'password': 'test',
    'port': '22'
    }


h2 = {
    'device_type': 'linux',
    'ip': '172.17.0.3',
    'username': 'test',
    'password': 'test',
    'port': '22'
    }

h3 = {
    'device_type': 'linux',
    'ip': '172.17.0.4',
    'username': 'test',
    'password': 'test',
    'port': '22'
    }

h4 = {
    'device_type': 'linux',
    'ip': '172.17.0.5',
    'username': 'test',
    'password': 'test',
    'port': '22'
    }


h5 = {
    'device_type': 'linux',
    'ip': '172.17.0.6',
    'username': 'test',
    'password': 'test',
    'port': '22'
    }

params = [h1, h2, h3, h4, h5]

info = device.Device(params)
print(info.gather_info())
#print(info.show_info())
