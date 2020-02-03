def average(iterable):
    sum = 0
    for i in iterable:
        sum+=i
    avg = sum/len(iterable)
    return (avg)


def find_slope(x1, y1, x2, y2):
    return((y2-y1)/(x2-x1))



def lin_reg(iter_x, iter_y):

    slopes = []
    for i in range(len(iter_x)-1):
        slopes.append(find_slope(iter_x[i], iter_y[i], iter_x[i+1], iter_y[i+1]))
    return(average(slopes))


def find_intercept(m, x, y):
    if len(x) == len(y):
        intercept = 0
        distances = []
        for i in range(len(x)):
            #print(m, x[i], intercept)
            point = m*x[i]+intercept
            distances.append(y[i]-point)

            #print("pointPOINTpointPOINT", point, "xXxX", x[i], "yYyY", y[i], "The end:", point-y[i])

        #print("\t", distances, "\n\t", x, "\n\t", y)
        intercept_min = average(distances)
        #print(intercept_min)
        #print(m*x[0])
        #print(intercept_min-(m*x[0]))

        return(intercept_min+(m*x[0]))


def line_sign(iter_x, iter_y, weight_modifiers=[]):
    slopes = []
    if weight_modifiers == []:
        weight_modifiers = [1 for x in iter_y]
    else:
        weight_modifiers[1] = int(weight_modifiers[0]) & weight_modifiers[1]
        if weight_modifiers[1] == 0:
            weight_modifiers[1] = 0.3
        del weight_modifiers[0]
    for i in range(len(iter_x)-1):
        slopes.append(find_slope(iter_x[i], iter_y[i], iter_x[i+1], iter_y[i+1]))
    sign = 0
    iterations = 0
    for i in range(len(iter_x)-1):
        if abs(slopes[-(i+1)]) == slopes[-(i+1)]:
            sign += (len(iter_x) - iterations)/recursion(len(iter_x))
        else:
            sign += (len(iter_x) - iterations)*weight_modifiers[i]/recursion(len(iter_x)) * -1
        iterations += 1

    #return(int(sign * -1* (1/sign)))
    return(sign)


def recursion(max_int):
    tot = 0
    for i in range(max_int):
        tot += i+1
    return(tot)


def recent_trend(iter_x, iter_y):
    x = []
    y = []
    for i in range(len(iter_x)):
        x.append(iter_x[-(i+1)])
        y.append(iter_y[-(i+1)])

    line = 0
    prev = 0
    if len(x) >= 5:
        recent = [x[i] for i in range(5)]
    else:
        recent = [x[i] for i in range(len(x))]
    for i in range(len(x)-len(recent)):
        line = lin_reg(x[0:i+5], y[0:i+5])
        if prev != None:
            if line < prev * 1.15 and line > prev * 0.95:
                recent.append(x[i+4])

            else:
                #print(line)
                break

        #prev = line

    #print("line", line, "\tprev", prev, "\trecent", recent)
    #print(recent, y[0:i+5])
    return([line, find_intercept(line, list(reversed(x[0:i+5])), list(reversed(y[0:i+5])))])
