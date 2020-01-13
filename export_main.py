import testApi as gm
import trend_and_line as tl
import data_analysis as da
data = open('file.txt', 'r')
out = open('updata.txt', 'w')

city_crime = {}

for line in data.read().splitlines():
    place, time = line.split('\t\t\t')
    if place not in city_crime:
        city_crime[place] = {'times': [time], 'coord': gm.get_lat_long(place)}
    else:
        city_crime[place]['times'].append(time)

for i in city_crime:
    print(i)
    print(str(city_crime[i]['coord']['lat'])+'\t'+str(city_crime[i]['coord']['lng']))
    for j in range(len(city_crime[i]['times'])):
        out.write(str(city_crime[i]['coord']['lat'])+'\t'+str(city_crime[i]['coord']['lng'])+'\n')
