from numpy import percentile
from matplotlib import pyplot as graphs
import data_analysis
import lin_reg

time = [int(i) for i in data_analysis.simple_column_ints('NM Crime Stats', ' \t')[0]]
rate = [int(i) for i in data_analysis.simple_column_ints('NM Crime Stats', ' \t')[1]]

def outliers(iterable):
##Outliers are defined as 1.5 times the interquartile range + the 75th percentile. We decided to change the multiplier to something that made
    #for i in iterable:
    print(iterable)
    iterable.sort()
    print(iterable)
    outliers = []
    big_outliers = []
    iqr = percentile(iterable, 75)-percentile(iterable, 25)
    over = (percentile(iterable, 75)+iqr)*1.5
    way_over = (percentile(iterable, 75)+iqr)*3
    under = (percentile(iterable, 25)-iqr)*1.5
    way_under = (percentile(iterable, 25)-iqr)*3
    for i in iterable:
        if i >= way_over:
            big_outliers.append(i)
        elif i >= over:
            outliers.append(i)
        elif i <= way_under:
            big_outliers.append(i)
        elif i <= under:
            outliers.append(i)
    print(iqr, over, way_over, under, way_under)
    return((outliers, big_outliers))

    
print(outliers(rate))


def line(iter_x, iter_y):
    if len(iter_x) == len(iter_y):
        slopes = []

        iterations = 1
        
        change_x = [x for x in iter_x]
        print(iter_x)
        change_y = [y for y in iter_y]
        print(change_x)
        for u in range(iterations):
            midpoints = [(None, None), ]
            for i in range(len(iter_y)-1):
                #print(i)
                slopes.append((iter_y[i]-iter_y[i+1])/(iter_x[i]-iter_x[i+1]))
                midpoints.append(
                    (((change_x[i]), (change_y[i]+change_y[i+1])/2)))
                
            #print(midpoints)
            change_y = [y[1] for y in midpoints]
            if u != iterations-1:
                midpoints.clear()
        for i in range(len(iter_y)-1):
            graphs.plot([midpoints[i][0], midpoints[i+1][0]], [midpoints[i][1], midpoints[i+1][1]], 'ro-')
            print("====================================")
            print([midpoints[i][0], midpoints[i+1][0]], [midpoints[i][1], midpoints[i+1][1]])
            graphs.plot([iter_x[i], iter_x[i+1]], [iter_y[i], iter_y[i+1]], 'bo-')
        #graphs.show()
        print(change_x)
            
print(line(time, rate))

#graphs.plot([time[0], time[-1]], [rate[0], rate[-1]], 'go-')


def find_intercept(m, x, y):
    if len(x) == len(y):
        intercept = 1
        if True:
            distances = {}
            for i in range(len(x)):
                distances[x[i]] = ((m*x[i])+intercept)-y[i]

            intercept_min = lin_reg.average(distances)

            return(intercept_min-(m*x[0]))

print(find_intercept(lin_reg.lin_reg(time, rate), time, rate), "eeeeeeeeee")

graphs.plot([time[0], time[-1]],
            [time[0]*lin_reg.lin_reg(time, rate)+find_intercept(lin_reg.lin_reg(time, rate), time, rate),
             time[-1]*lin_reg.lin_reg(time, rate)+find_intercept(lin_reg.lin_reg(time, rate), time, rate)],
            'co-')

graphs.show()

