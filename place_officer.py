qty_officers = 10
effective_radius = 0.002

def officer_placement(qty_officers, effective_radius, data_file):
    data = open(data_file, 'r')
    rates = {}
    rate_qty = []
    high_rates = []
    officer_places = []
    for line in data.read().splitlines():
        lat, long = line.split(',')
        lat, long = int(float(lat)*10000), int(float(long)*10000)
        if (lat, long) in rates:
            rates[(lat, long)] += 1
        else:
            rates[(lat, long)] = 1

    for i in rates:
        rate_qty.append(rates[i])
        print(i, rates[i])

    rate_qty.sort()
    high_rates = rate_qty[-qty_officers:]

    for i in rates:
        if rates[i] in high_rates and len(officer_places) <= qty_officers-1:
            officer_places.append((i[0]/1000000, i[1]/1000000))

    print(officer_places)

    out = open('policedata.txt', 'w')
    for i in officer_places:
        out.write(str(i[0])+','+str(i[1])+'\n')



officer_placement(qty_officers, effective_radius, 'crimedata.txt')
