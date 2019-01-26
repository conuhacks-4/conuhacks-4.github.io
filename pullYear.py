import requests
import json

headers = {
    'client-secret': '9923ac9b-8fd3-421f-b0e5-952f807c6885',
}

x = 10
y = 31
placeholder = '-0'
while y<=31:
    if y >= 10:
        placeholder = '-'
    params = (
        ('startDate', '2018-'+ str(x) + placeholder + str(y) + 'T00:00:00Z'),
        ('endDate', '2018-' + str(x) + placeholder + str(y) + 'T23:59:00Z'),
        ('offset', '0'),
        ('artistId', '552'),
        ('totalRecordsCount', '0')
    )



    response = requests.get('https://conuhacks-playback-api.touchtunes.com/plays', headers=headers, params=params).json()

    print(response)

    with open('data' + str(x) + '-' + str(y) + '.json', 'w') as outfile:
        json.dump(response, outfile)
    y+=1