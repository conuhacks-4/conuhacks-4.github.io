import requests
import json

headers = {
    'Authorization': 'Bearer',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'client-secret': '3b8b3f84-9217-4339-8652-1cd12f45bfe4',
}

artistName = 'Soundgarden'
#x is the month the loop starts
x = 6
#y is the day
y = 30

placeholderY = '-0'
placeholderX = '-0'
#f = open('entireYearTPetty3.txt','w')

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
            ('artistId', '75450'),
            ('totalRecordsCount', '0'),
            ('limit', 5000)
        )

        response = requests.get(
            'https://prod-us-conuhacks-main.scaffold-workers-ext-main-us.tsp.cld.touchtunes.com/plays', headers=headers, params=params).json()
        print(str(x) + '-' + str(y) + ": " + str(response['totalRecordsCount']))
        print(response)

        with open(artistName + str(x) + '-' + str(y) + '.json', 'w') as outfile:
            json.dump(response, outfile)
        #f.write(str(x) + '-' + str(y) + ": " + str(response['totalRecordsCount']) + ' ' + '\n')

        y+= 1

        if (x == 2):
            if (y > 28):
                y = 33

        if (x == 4) or (x == 6) or (x == 9) or (x == 11):
            if (y > 30):
                y = 33

    y = 1
    x += 1
    placeholderY = '-0'

#f.close()