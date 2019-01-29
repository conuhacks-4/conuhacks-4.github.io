import requests
import json

headers = {
    'client-secret': '9923ac9b-8fd3-421f-b0e5-952f807c6885',
}

x = 1
y = 1

params = (
    ('startDate', '2018-06-19T00:00:00Z'),
    ('endDate', '2018-06-19T23:59:00Z'),
    ('offset', '0'),
    ('totalRecordsCount', '0'),
    ('limit', 5000)
)

response = requests.get('https://conuhacks-playback-api.touchtunes.com/plays', headers=headers, params=params).json()
artList = []
print(response)

with open('dataFull3.json', 'w') as outfile:
    json.dump(response, outfile)

for i in range(len(response["plays"])):
   # print(response["plays"][i]["artistId"])
    if response["plays"][i]["artistId"] not in artList:
        artList.append(response["plays"][i]["artistId"])
headers = {
    'client-secret': '9923ac9b-8fd3-421f-b0e5-952f807c6885',
}

#response = requests.get('https://conuhacks-playback-api.touchtunes.com/artist/', headers=headers)


f = open('artistNames0619.txt','w')

for j in artList:
    #print(j)
    try:
        response = requests.get('https://conuhacks-playback-api.touchtunes.com/artist/' + str(j), headers=headers).json()
        print(str(j) + ': ' + response["artistName"])
        f.write(str(j) + ': ' + response["artistName"]+ '\n')
    except:
        print("exception on " + str(j))











