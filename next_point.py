
def next_point(time, rate):
    import data_analysis
    import trend_and_line
    import random

    file = open('datas.txt', 'w')

    #time = [int(i) for i in data_analysis.simple_column_ints('Minnesota Crime Stats', '  ')[0]]
    #rate = [int(i) for i in data_analysis.simple_column_ints('Minnesota Crime Stats', '  ')[1]]
    #time = [int(i) for i in data_analysis.simple_column_ints('NM Crime Stats', ' \t')[0]]
    #rate = [int(i) for i in data_analysis.simple_column_ints('NM Crime Stats', ' \t')[1]]
    #time = [int(i) for i in data_analysis.simple_column_ints('CO Crime Stats', '\t')[0]]
    #rate = [int(i) for i in data_analysis.simple_column_ints('CO Crime Stats', '\t')[1]]
    #time = [int(i) for i in data_analysis.simple_column_ints('AL Crime Stats', '\t')[0]]
    #rate = [int(i) for i in data_analysis.simple_column_ints('AL Crime Stats', '\t')[1]]

    outs = [[], []]

    rems = []
    iters = 0
    individual_weights = []
    for i in rate:
        if i in outs[0]:
            individual_weights.append([time[iters], 0.3])
        elif i in outs[1]:
            rems.append([time[iters], i])
        else:
            individual_weights.append([time[iters], 1])
        iters+=1

    for i in rems:
        rate.remove(i[1])
        time.remove(i[0])

    def line(iter_x, iter_y):
        if len(iter_x) == len(iter_y):
            slopes = []

            iterations = 1

            change_x = [x for x in iter_x]
            change_y = [y for y in iter_y]
            for u in range(iterations):
                midpoints = [(None, None), ]
                for i in range(len(iter_y)-1):
                    slopes.append((iter_y[i]-iter_y[i+1])/(iter_x[i]-iter_x[i+1]))
                    midpoints.append(
                        (((change_x[i]), (change_y[i]+change_y[i+1])/2)))

                change_y = [y[1] for y in midpoints]
                if u != iterations-1:
                    midpoints.clear()


    return(trend_and_line.average([0*trend_and_line.recent_trend(time, rate)[0]+trend_and_line.recent_trend(time, rate)[1], rate[-1]*trend_and_line.line_sign(time, rate, [x[1] for x in individual_weights])+ rate[-1]]))

    #MISSING FROM Minnesota: 2018  124243
