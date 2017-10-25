import geojson
import requests
geojsonurl = 'https://raw.githubusercontent.com/jtweddle89/proj-mapping/master/test/map.geojson'
r = requests.get(geojsonurl)

mydata = r.json()
print(mydata.keys())


#print out keys and values of every item in every properties dictionary, skipping items that have value of ""
ix = len(mydata['features']) - 1
for i in mydata['features']:
#        print (mydata['features'][ix]['properties'])
        for (k,v) in mydata['features'][ix]['properties'].items():
                if len(k)>=11:
                        tabs = '\t\t'
                else:
                        tabs = '\t\t\t'
                if v=="":
                        continue
                print k, tabs, v
        ix -= 1
