import geojson
import requests
geojsonurl = 'https://raw.githubusercontent.com/jtweddle89/proj-mapping/master/test/map.geojson'
r = requests.get(geojsonurl)

mydata = r.json()
print(mydata.keys())


##gtlist = []

for i in mydata['features'][0]:
        print(i,mydata['features'][0][i])
        print('-----------------------------------------------------------------------------')
    