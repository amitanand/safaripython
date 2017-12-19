import urllib.request
from xml.etree.ElementTree import XML
import sys

if len(sys.argv) != 3:
    raise SystemExit('Usage: nextbus.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]

# print("Command options :",sys.argv)     #shows the argument is sys.argv
# raise SystemExit(0)

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={}&route={}'.format(stopid,route))
data = u.read()
# print(data)
doc = XML(data)
for i in doc.findall('.//pt'):
    print(i.text)
