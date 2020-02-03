import testApi as gm
import trend_and_line as tl
import data_analysis as da
from datetime import datetime
data = open('file.txt', 'r')
out = open('updata.txt', 'w')

city_crime = {}
rates = {}
dates = []

for line in data.read().splitlines():
    place, time = line.split('\t\t\t')
    if place not in city_crime:
        city_crime[place] = {'times': [time], 'coord': gm.get_lat_long(place)}
    else:
        city_crime[place]['times'].append(time)

for i in city_crime:
    iters = 0
    for j in city_crime[i]['times']:
        time = datetime.strptime(j, "%m-%d-%Y %I:%M %p").day + datetime.strptime(j, "%m-%d-%Y %I:%M %p").hour/24
        print(city_crime[i]['times'])
        city_crime[i]['times'][iters] = time
        iters += 1

for i in city_crime:
    time = city_crime[i]['times']
    rate = [len(time) for x in range(len(time))]
    print(i, rate, time)
    rates[(city_crime[i]['coord']['lat'], city_crime[i]['coord']['lng'])] = tl.average([tl.line_sign(time, rate), (float(rate[0]) *  float(tl.recent_trend(time, rate)[0]) + tl.recent_trend(time, rate)[1])])

print(rates)

for i in city_crime:
    print(i)
    print(str(city_crime[i]['coord']['lat'])+'\t'+str(city_crime[i]['coord']['lng']))
    for j in range(len(city_crime[i]['times'])):
        if city_crime[i]['coord']['lat'] != None:
            out.write(str(city_crime[i]['coord']['lat'])+','+str(city_crime[i]['coord']['lng'])+'\n')

data.close()
out.close()
