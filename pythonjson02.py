#!/usr/bin/python3

import requests

myr = requests.get('http://api.open-notify.org/astros.json')
astros = myr.json()
#print(type(astros))
#print(astros['people'])

with open('ansible.inv', 'w') as ansinv:
    for astro in astros['people']:
#        print(astro['name'].split()[0], file=ansinv)   # this harvests JUST the first names
        print(astro['name'].replace(' ', '').lower())   # normalize data by removing whitespace and caps
