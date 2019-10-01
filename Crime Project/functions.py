from numpy import percentile
from matplotlib import pyplot as graphs


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

    
print(outliers(
    [1, 2, 5, 6, 10, 9, 4, 2, 15, 7, 3, 4, 7, 4, 5, 6, 3, -14, 7, 2]))


def line(iter_x, iter_y):
    if len(iter_x) == len(iter_y):
        slopes = []

        iterations = 100
        
        change_x = [x for x in iter_x]
        print(iter_x)
        change_y = [y for y in iter_y]
        print(change_x)
        for u in range(iterations):
            midpoints = [(0, 0), ]
            for i in range(len(iter_y)-1):
                print(i)
                slopes.append((iter_y[i]-iter_y[i+1])/(iter_x[i]-iter_x[i+1]))
                midpoints.append(
                    (((change_x[i]), (change_y[i]+change_y[i+1])/2)))
                
            print(midpoints)
            change_x = [x[0] for x in midpoints]
            change_y = [y[1] for y in midpoints]
            if u != iterations-1:
                midpoints.clear()
        for i in range(len(iter_y)-1):
            graphs.plot([midpoints[i][0], midpoints[i+1][0]], [midpoints[i][1], midpoints[i+1][1]], 'ro-')
            print("====================================")
            print([midpoints[i][0], midpoints[i+1][0]], [midpoints[i][1], midpoints[i+1][1]])
            graphs.plot([iter_x[i], iter_x[i+1]], [iter_y[i], iter_y[i+1]], 'bo-')
        graphs.show()
        print(change_x)
            
print(line(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 2, 5, 6, 10, 9, 4, 2, 15, 7, 3, 4, 7, 4, 5, 6, 3, -14, 7, 2]
))
