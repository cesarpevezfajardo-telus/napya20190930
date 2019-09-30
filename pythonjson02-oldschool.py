#!/usr/bin/python3
"""This is a PURE PYTHON way to get at JSON
This span multiple lines
Russell Zachary Feeser || rzfeeser@alta3.com <<-- confused? Contact me!"""

import urllib.request
import json

def main():
    respz = urllib.request.urlopen('http://api.open-notify.org/astros.json')
    
    decoded_respz = respz.read().decode('utf-8')

    ## print(type(decoded_respz))  # reveals the object TYPE (what class is created from)

    ## print(decoded_respz['people']) # TOO SOON! our data is STILL a STRING! (str)

    decoded_respz = json.loads(decoded_respz) # recast decoded_respz as a dict!

    astros = decoded_respz['people']

    for astro in astros:
        print(astro['name'])




if __name__ == "__main__":
    main()
