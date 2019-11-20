from numpy import percentile

def simple_column_ints(file_name, seperator):
    data = open(file_name, 'r')
    lst_x = []
    lst_y = []
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-']
    for line in data:
        if seperator in line:
            print(line)
            column_1, column_2 = line.split(seperator)
            for i in column_1:
                if i not in numbers:
                    print(i)
                    column_1 = column_1.replace(i, "")
            for i in column_2:
                if i not in numbers:
                    print(i)
                    column_2 = column_2.replace(i, "")
            lst_x.append(int(column_1))
            lst_y.append(int(column_2))
    print("QQQ", lst_x, "RRR", lst_y)
    return([lst_x, lst_y])

def order(iterable):
    ret_iter = [x for x in iterable]
    ret_iter.sort()
    return(ret_iter)



def outliers(iter_y):
##Outliers are defined as 1.5 times the interquartile range + the 75th percentile. We decided to change the multiplier to something that made
    #for i in iterable:
    iterable = order(iter_y)
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
    print("\n\nTHE OUTS STUFF\n", iqr, "\n", over, "\n", way_over, "\n", under, "\n", way_under)
    return((outliers, big_outliers))

def specialized_file_analysis_ABQ(file_name):

    file = open(file_name, 'r')

    lines = []

    for line in file:
        lines.append(line)

    iter = 0

    rates = {}

    for i in lines:
        if "geometry" in i:
            lat = lines[iter+1]
            long = lines[iter+2]

            if [lat, long] in rates:
                rates[[lat, long]] += 1

            else:
                rates[[lat, long]] = 1

        iter+=1
