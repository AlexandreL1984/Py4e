#py4e
#Worked Exercise, Chapter 13. Week 6 of Using Python to Access Web Data
#Extracting Data from json

import urllib.request as ur
import json
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#json_url = 'http://py4e-data.dr-chuck.net/comments_1063227.json'

json_url = input("Enter location: ")
print("Retrieving ", json_url)

data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
total_number = 0

for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)
