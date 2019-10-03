def average(iterable):
    sum = 0
    for i in iterable:
        sum+=i
    avg = sum/len(iterable)
    return (avg)
    

def lin_reg(iter_x, iter_y):
    
    slopes = []
    for i in range(len(iter_x)-1):
        slopes.append((iter_y[i+1]-iter_y[i])/(iter_x[i+1]-iter_x[i]))
    return(average(slopes))
