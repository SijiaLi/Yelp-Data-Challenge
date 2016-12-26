import json
import pandas as pd

data = pd.read_csv('data.csv')
N, L = data.shape
columns = list(data.columns)
columns.remove('longitude')
columns.remove('latitude')

json_data = {'type':"FeatureCollection", 'features':[]}

for i in range(N):
    record = data.ix[i]
    one_feature = {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [0,0]
      },
      "properties": {
      }
    }
    one_feature['geometry']['coordinates'][0] = record.longitude
    one_feature['geometry]['coordinates'][1] = record.latitude
    for col in columns:
        one_feature['properties'][col] = record[col]
    json_data['features'].append(one_feature)
    
with open('data.geojson', 'w') as outfile:
    json.dump(json_data, outfile)