import requests
import json

URL ="https://chargepoints.dft.gov.uk/api/retrieve/registry/"
#URL+="lat/50.876381/
#URL+="long/-1.245401/"
URL+="postcode/po11aa/"
URL+="format/json/"
URL+="dist/0.5/"
URL+="units/km/"

x = requests.get(URL)

data=json.loads(x.text)
for  device in data["ChargeDevice"]:
  print(device["ChargeDeviceId"] ,  device["ChargeDeviceName"], device["ChargeDeviceStatus"] )
  for connector in device["Connector"]:
     print("Connector status=",  connector["ChargePointStatus"])




#print(data["ChargeDevice"][0]["ChargeDeviceId"])
