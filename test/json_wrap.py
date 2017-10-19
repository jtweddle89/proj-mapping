

markercolour = '#ff0000'
markersize = 'medium'
markersymbol = 'lighthouse'
prop1 = 'val1'
prop2 = 'val2'
prop3 = 'val3'
geometrytype = 'Point'
lat = -80.760498046875
lon = 43.67581809328341

pointentry = '''{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "marker-color": "''' + markercolour + '''",
        "marker-size": "''' + markersize + '''",
        "marker-symbol": "''' + markersymbol + '''",
        "prop1": "''' + prop1 + '''",
        "prop2": "''' + prop2 + '''",
        "prop3": "''' + prop3 + '''"
      },
      "geometry": {
        "type": "''' + geometrytype + '''",
        "coordinates": [
          ''' + str(lat) + ''',
          ''' + str(lon) + '''
        ]
      }
    },
    {

'''

print(pointentry)
