import requests
import re


response = requests.get('http://meteoinfo.by/5/')
handle = open("weather.txt", 'w')
handle.write(str(response.content))
handle.flush()
handle.close()
regex = ur'\d{2}\:\d{2}\;\s\d{2}\s.*\s\d{4}'
handle = open("weather.txt", 'r')
for line in handle.readlines():
    line = line.decode('1251')
    m = re.findall(regex, line)
    if m:
        print m[0]
count = 0
handle = open("weather.txt", 'r')
for line in handle.readlines():
    line = line.decode('1251')
    regex2 = '#F2F2FF'
    if line.find(regex2) >= 0:
        count += 1
        if count < 2:
            print ('The weather today :')
    regex3 = r'[+-]\d\d?\.\.[+-]\d\d?'
    if count > 0 and count < 2:
        m = re.findall(regex3, line)
        if m:
            print m[0]
