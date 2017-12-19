import urllib.request
from xml.etree.ElementTree import XML

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14787&route=22')
data = u.read()
print(data)
doc = XML(data)
for i in doc.findall('.//pt'):
    print(i.text)
