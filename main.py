from matplotlib import pyplot as graphs
import data_analysis
import trend_and_line
import random

#time = [int(i) for i in data_analysis.simple_column_ints('Minnesota Crime Stats', '  ')[0]]
#rate = [int(i) for i in data_analysis.simple_column_ints('Minnesota Crime Stats', '  ')[1]]
#time = [int(i) for i in data_analysis.simple_column_ints('NM Crime Stats', ' \t')[0]]
#rate = [int(i) for i in data_analysis.simple_column_ints('NM Crime Stats', ' \t')[1]]
#time = [int(i) for i in data_analysis.simple_column_ints('CO Crime Stats', '\t')[0]]
#rate = [int(i) for i in data_analysis.simple_column_ints('CO Crime Stats', '\t')[1]]
#time = [int(i) for i in data_analysis.simple_column_ints('AL Crime Stats', '\t')[0]]
#rate = [int(i) for i in data_analysis.simple_column_ints('AL Crime Stats', '\t')[1]]
time = [int(i) for i in data_analysis.simple_column_ints('NY Crime Stats', '\t')[0]]
rate = [int(i) for i in data_analysis.simple_column_ints('NY Crime Stats', '\t')[1]]

print("BITIME", time, rate)

#outs = data_analysis.outliers(rate)
outs = [[], []]

print("\n\n\n0 1_1 -1- 5", outs)

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

print("0utliers", outs, "R3ms", rems, "R8", rate)

print("PITIME", time, rate)

print("is it mixed??????" ,rate)

print("MITIME", time, rate)

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
#print(find_intercept(trend_and_line.lin_reg(time, rate), time, rate), "eeeeeeeeee")

print(time[-1]+1, rate[-1]*trend_and_line.line_sign(time, rate, [x[1] for x in individual_weights])+ rate[-1], 'o-')

graphs.plot(time[-1]+1, rate[-1]*trend_and_line.line_sign(time, rate, [x[1] for x in individual_weights])+ rate[-1], 'o-')

#graphs.plot([time[0], time[-1]],
#            [time[0]*trend_and_line.lin_reg(time, rate)+trend_and_line.find_intercept(trend_and_line.lin_reg(time, rate), time, rate),
#             time[-1]*trend_and_line.lin_reg(time, rate)+trend_and_line.find_intercept(trend_and_line.lin_reg(time, rate), time, rate)],
#            'co-')

print([0, time[-1]],
             [0*trend_and_line.recent_trend(time, rate)[0]+trend_and_line.recent_trend(time, rate)[1],
             time[-1]*trend_and_line.recent_trend(time, rate)[0]+trend_and_line.recent_trend(time, rate)[1]], 'si zhi gou')

#graphs.plot([0, time[-1]],
#            [0*trend_and_line.recent_trend(time, rate)[0]+trend_and_line.recent_trend(time, rate)[1],
#             time[-1]*trend_and_line.recent_trend(time, rate)[0]+trend_and_line.recent_trend(time, rate)[1]], 'go-')

graphs.plot([time[-1]+1],
            [0*trend_and_line.recent_trend(time, rate)[0]+trend_and_line.recent_trend(time, rate)[1]],
             'go-')

print(trend_and_line.recent_trend(time, rate))

graphs.plot([time[-1]+1], [trend_and_line.average([0*trend_and_line.recent_trend(time, rate)[0]+trend_and_line.recent_trend(time, rate)[1], rate[-1]*trend_and_line.line_sign(time, rate, [x[1] for x in individual_weights])+ rate[-1]])], 'mo')

print([0, time[-1]],
            [0*trend_and_line.recent_trend(time, rate)[0]+trend_and_line.recent_trend(time, rate)[1],
             time[-1]*trend_and_line.recent_trend(time, rate)[0]+trend_and_line.recent_trend(time, rate)[1]], 'go-')

print("y-int:\t", trend_and_line.recent_trend(time, rate)[1])
print("val1:\t", time[0]*trend_and_line.recent_trend(time, rate)[0])
print("val0:\t", time[-1]*trend_and_line.recent_trend(time, rate)[0])

graphs.show()


#MISSING FROM Minnesota: 2018  124243
