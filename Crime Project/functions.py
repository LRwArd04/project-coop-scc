from numpy import percentile


def outliers(iterable):
##Outliers are defined as 1.5 times the interquartile range + the 75th percentile. We decided to change the multiplier to something that made
    #for i in iterable:
    outliers = []
    big_outliers = []
    iqr = percentile(iterable, 75)-percentile(iterable, 25)
    over = (percentile(iterable, 75)+iqr)*1.5
    way_over = (percentile(iterable, 75)+iqr)*3
    under = (percentile(iterable, 25)-iqr)*1.5
    way_under = (percentile(iterable, 75)+iqr)*3
    for i in iterable:
        if i >= over:
            outliers.append(i)
        elif i >= way_over:
            big_outliers.append(i)
        elif i <= under:
            outliers.append(i)
        elif i <= way_under:
            big_outliers.append(i)
    print(iqr, over, way_over, under, way_under)
    return((outliers, big_outliers))

    
print(outliers(
    [1, 2, 5, 6, 10, 9, 4, 2, 15, 7, 3, 4, 7, 4, 5, 6, 3, -14, 7, 2]))
