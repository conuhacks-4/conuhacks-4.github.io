import requests
import json

headers = {
    'client-secret': '9923ac9b-8fd3-421f-b0e5-952f807c6885',
}

params = (
    ('startDate', '2018-02-19T21:00:00Z'),
    ('endDate', '2018-02-19T22:00:00Z'),
    ('offset', '0'),
)

response = requests.get('https://conuhacks-playback-api.touchtunes.com/plays', headers=headers, params=params)
json_data=response.json()
print (json_data)



#for d in y:
 #   for playDate, artistId in d.iteritems():
  #      print(playDate, artistId)
# the result is a Python dictionary:
print(json_data["plays"][0]["playDate"])





