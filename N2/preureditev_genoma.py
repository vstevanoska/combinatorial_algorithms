import sys
import time

def obrni(genom, start, end):

    while (start < end):

        temp_value = genom[start]
        genom[start] = genom[end]
        genom[end] = temp_value

        start += 1
        end -= 1

    return

def urejanje_s_preobrati(genom):

    genom_sorted = list(range(1, len(genom) + 1))

    for i in range(1, len(genom)):
        
        j = -1

        for temp_j in range(len(genom)):

            if genom[temp_j] == i:
                j = temp_j
                break

        if (j + 1) != i:
            
            obrni(genom, i - 1, j)

            print("Current state: ", genom)

        if (genom == genom_sorted):
            return genom

def count_breakpoints(genom):

    breakpoints = 0

    for i in range(len(genom) - 1):

        if (abs(genom[i] - genom[i + 1]) != 1):
            breakpoints += 1

    return breakpoints


def find_parts(genom):

    ascending = []
    descending = []

    is_switched = True

    temp_list = []
    temp_list_index_asc = []
    temp_list_index_des = []
    temp_list_index = []

    for i in range(len(genom) - 1):

        if (abs(genom[i] - genom[i + 1]) == 1):

            if (is_switched == True):
                temp_list_index.append(i)

            temp_list.append(genom[i])
            is_switched = False
        
        else:
            
            if is_switched == False:

                temp_list.append(genom[i])
                temp_list_index.append(i)
                
                is_switched = True

                if (len(temp_list) > 1):

                    if (temp_list[0] < temp_list[1]):
                        ascending.append(temp_list)

                        temp_list_index_asc.append(temp_list_index)

                    elif (temp_list[0] > temp_list[1]):
                        descending.append(temp_list)

                        temp_list_index_des.append(temp_list_index)

                    temp_list = []

                temp_list_index = []

    # sort descending

    # print("Before descending: ", descending)

    for i in range(len(descending) - 1):

        for j in range(i + 1, len(descending)):

            if (descending[i][len(descending[i]) - 1] > descending[j][len(descending[j]) - 1]):

                temp_value = descending[i]
                descending[i] = descending[j]
                descending[j] = temp_value

                temp_value = temp_list_index_des[i]
                temp_list_index_des[i] = temp_list_index_des[j]
                temp_list_index_des[j] = temp_value


    # print("Ascending: ", ascending)
    # print("Descending: ", descending)
    # print("Temp list index asc: ", temp_list_index_asc)
    # print("Temp list index des: ", temp_list_index_des)

    # print("After descending: ", descending)

    return temp_list_index_asc, temp_list_index_des


def preurejanje_trakov(genom):

    genom = [0] + genom + [len(genom) + 1]
    print("Start: ", genom)

    breakpoints = count_breakpoints(genom)
    
    while (breakpoints > 0):

        # print("Breakpoints: ", breakpoints)

        ascending, descending = find_parts(genom)

        if (len(descending) > 0):
            obrat = descending[0]
        
        else:

            for i in range(len(ascending)):

                if ascending[i][0] != 0:

                    obrni(genom, ascending[i][0], ascending[i][1])
                    obrat = ascending[i]

                    break

        for i in range(len(genom)):

            if (genom[i] + 1 == genom[obrat[1]]) and (i < obrat[1]):

                obrni(genom, i + 1, obrat[1])

                breakpoints = count_breakpoints(genom)

                # if (genom[obrat[1]] + 1 == genom[obrat[1] + 1]):
                #     breakpoints -= 1

                break

            elif (genom[i] + 1 == genom[obrat[1]]) and (i > obrat[0]):

                obrni(genom, obrat[1] + 1, i)

                breakpoints = count_breakpoints(genom)

                break

        print("Current state: ", genom)

    return genom

if __name__ == '__main__':

    #read file
    genom = []

    with open(sys.argv[1], "r") as file:

        for line in file:
            genom.append(int(line))


    #urejanje s preobrati
    # start_time = time.time()

    # result = urejanje_s_preobrati(genom.copy())

    # print("Elapsed time: ", (time.time() - start_time) * 1000)
    

    #preurejanje trakov
    start_time = time.time()

    result = preurejanje_trakov(genom.copy())
    # find_parts(genom.copy())

    print("Elapsed time: ", (time.time() - start_time) * 1000)


    # #lastna resitev
    # start_time = time.time()

    # result3 = custom(genom.copy())

    # print("Elapsed time: ", (time.time() - start_time) * 1000)
    # print("Result: ", result3)

    #write to file
    # with open("output.txt", "w") as output_file:

    #     for value in result:
    #         output_file.write("%i " % value)