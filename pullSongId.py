import requests
import json

headers = {
    'client-secret': '9923ac9b-8fd3-421f-b0e5-952f807c6885',
}

x = 1
y = 1
placeholderY = '-0'
placeholderX = '-0'

f = open('songIdList.txt', 'w')
songList = []
while x <= 12:
    while y <= 31:
        if y >= 10:
            placeholderY = '-'

        if x >= 10:
            placeholderX = '-'
        params = (
            ('startDate', '2018' + placeholderX + str(x) + placeholderY + str(y) + 'T00:00:00Z'),
            ('endDate', '2018' + placeholderX + str(x) + placeholderY + str(y) + 'T23:59:00Z'),
            ('offset', '0'),
            ('artistId', '552'),
            ('totalRecordsCount', '0'),
            ('limit', 5000)

        )

        response = requests.get('https://conuhacks-playback-api.touchtunes.com/plays', headers=headers,
                                params=params).json()


        for i in range(len(response["plays"])):
            if response["plays"][i]["songId"] not in songList:
                songList.append(response["plays"][i]["songId"])
            print(response["plays"][i]["songId"])

        

        y += 1

        if (x == 2):
            if (y > 28):
                y = 33

        if (x == 4) or (x == 6) or (x == 9) or (x == 11):
            if (y > 30):
                y = 33

    y = 1
    x += 1
    placeholderY = '-0'


f.close()