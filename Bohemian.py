import json

headers = {
    'client-secret': '9923ac9b-8fd3-421f-b0e5-952f807c6885',
}

x = 1
y = 1
placeholderY = '-0'
placeholderX = '-0'

#f = open('test.txt','w')
songList = [6131102,
16106511,
16106654,
16110457,
33543404,
3543407,
39829307,
39829316,
78950416,
92680501]

h = open('dailyBohemia.txt','w')

while x <= 12:
    #count = 0
    while y <= 31:
        count = 0
        with open('data' + str(x) + '-' + str(y) + '.json') as f:
            data = json.load(f)

        print(str(x) + '-' + str(y) + ': ' + str(data['totalRecordsCount']))

        for i in range(len(data["plays"])):
            if data["plays"][i]["songId"] in songList:
                count += 1

        f.close()
        h.write(str(count) + '\n')
        y += 1

        if (x == 2):
            if (y > 28):
                y = 33

        if (x == 4) or (x == 6) or (x == 9) or (x == 11):
            if (y > 30):
                y = 33

    y = 1
    x += 1

h.close()