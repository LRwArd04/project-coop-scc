def simple_column_ints(file_name, seperator):
    data = open(file_name, 'r')
    lst_x = []
    lst_y = []
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-']
    for line in data:
        if seperator in line:
            column_1, column_2 = line.split(seperator)
            for i in column_1:
                if i not in numbers:
                    column_1 = column_1.strip(i)
            for i in column_2:
                print(i)
                if i not in numbers:
                    column_2 = column_2.replace(i, "")
            lst_x.append(int(column_1))
            lst_y.append(int(column_2))
    return([lst_x, lst_y])
