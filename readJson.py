import requests
import json

headers = {
    'client-secret': '9923ac9b-8fd3-421f-b0e5-952f807c6885',
}

x = 1
y = 1
placeholderY = '-0'
placeholderX = '-0'

#f = open('test.txt','w')
songList = []

h = open('ArethaMonthly.txt','w')
while x <= 12:
    count = 0
    while y <= 31:
        #count = 0
        if y >= 10:
            placeholderY = '-'

        if x >= 10:
            placeholderX = '-'
        #params = (
          #  ('startDate', '2018' + placeholderX + str(x) + placeholderY + str(y) + 'T00:00:00Z'),
           # ('endDate', '2018' + placeholderX + str(x) + placeholderY + str(y) + 'T23:59:00Z'),
           # ('offset', '0'),
            #('artistId', '552'),
           # ('totalRecordsCount', '0'),

        #)

        with open('Arethra' + str(x) + '-' + str(y) + '.json') as f:
            data = json.load(f)
        count += int(data['totalRecordsCount'])
        print(str(x) + '-' + str(y) + ': ' + str(data['totalRecordsCount']))
        #h.write(str(data['totalRecordsCount']) + '\n')

        for i in range(len(data["plays"])):
            if data["plays"][i]["songId"] not in songList:
                songList.append(data["plays"][i]["songId"])


            #print(data["plays"][i]["songId"])
        #response = requests.get('https://conuhacks-playback-api.touchtunes.com/plays', headers=headers, params=params).json()

        #print(str(x) + '-' + str(y) + ": " + str(response['totalRecordsCount']))

        #f.write(str(x) + '-' + str(y)+ ": " + str(response['totalRecordsCount']) + ' ' + '\n')
        #f.write(str(response['totalRecordsCount']) + '\n')

        #with open('data' + str(x) + '-' + str(y) + '.json', 'w') as outfile:
          #  json.dump(response, outfile)
        #count += int(response['totalRecordsCount'])

        f.close()

        y+=1

        if (x==2):
            if (y>28):
                y = 33

        if (x==4) or (x==6) or (x==9) or (x==11):
            if (y>30):
                y = 33
    print(count)
    h.write(str(count) + '\n')
    #f.write(str(count) + '\n')
    y = 1
    x += 1
    placeholderY = '-0'
songList.sort()
print(songList)

#headers = {
   # 'client-secret': '9923ac9b-8fd3-421f-b0e5-952f807c6885',
#}
#f = open('songNames.txt','w')

#for j in songList:
 #   try:
  #      response = requests.get('https://conuhacks-playback-api.touchtunes.com/song/' + str(j), headers=headers).json()
   #     print(str(j) + ': ' + response["songTitle"])
    #    f.write(str(j) + ': ' + response["songTitle"]+ '\n')
    #except:
     #   print("exception on " + str(j))
h.close()
f.close()
