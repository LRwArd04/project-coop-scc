import testApi as gm
import trend_and_line as tl
import data_analysis as da
from datetime import datetime
import tkinter as tk
from tkinter import ttk


data = open('file.txt', 'r')
out = open('updata.txt', 'w')


city_crime = {}
rates = {}
dates = []
elapsedDaysLeap = {1: 0,
                    2: 31,
                    3: 31+29,
                    4: 31+29+31,
                    5: 31+29+31+30,
                    6: 31+29+31+30+31,
                    7: 31+29+31+30+31+30,
                    8: 31+29+31+30+31+30+31,
                    9: 31+29+31+30+31+30+31+31,
                    10: 31+29+31+30+31+30+31+31+30,
                    11: 31+29+31+30+31+30+31+31+30+31,
                    12: 31+29+31+30+31+30+31+31+30+31+30}
elapsedDays = {1: 0,
                2: 31,
                3: 31+28,
                4: 31+28+31,
                5: 31+28+31+30,
                6: 31+28+31+30+31,
                7: 31+28+31+30+31+30,
                8: 31+28+31+30+31+30+31,
                9: 31+28+31+30+31+30+31+31,
                10: 31+28+31+30+31+30+31+31+30,
                11: 31+28+31+30+31+30+31+31+30+31,
                12: 31+28+31+30+31+30+31+31+30+31+30}

for line in data.read().splitlines():
    place, time = line.split('\t')
    if place not in city_crime:
        city_crime[place] = {'times': [time], 'coord': gm.get_lat_long(place), 'rate': {}}
    else:
        city_crime[place]['times'].append(time)

for i in city_crime:
    iters = 0
    for j in city_crime[i]['times']:
        if datetime.strptime(j, "%m/%d/%Y %I:%M %p").year % 4 == 0:
            time = datetime.strptime(j, "%m/%d/%Y %I:%M %p").day+elapsedDaysLeap[datetime.strptime(j, "%m/%d/%Y %I:%M %p").month]
        else:
            time = datetime.strptime(j, "%m/%d/%Y %I:%M %p").day+elapsedDays[datetime.strptime(j, "%m/%d/%Y %I:%M %p").month]
        print(city_crime[i]['times'])
        if time in city_crime[i]['rate']:
            city_crime[i]['rate'][time] += 1
        else:
            print(time, i)
            city_crime[i]['rate'][time] = 1
        city_crime[i]['times'][iters] = time
        iters += 1

print('\n\n\n\n\n\n\n\n\n\n\n\n', city_crime, '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

for i in city_crime:
    time = city_crime[i]['rate']
    rate = [city_crime[i]['rate'][x] for x in city_crime[i]['rate']]
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
