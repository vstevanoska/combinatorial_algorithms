import sys
import time

obrat = 0

def obrni(genom, start, end):

    while (start < end):

        temp_value = genom[start]
        genom[start] = genom[end]
        genom[end] = temp_value

        start += 1
        end -= 1

    global obrat
    obrat += 1

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

            # print("Current state: ", genom)

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

    merge_sort(descending, temp_list_index_des, 0, len(descending) - 1)

    return temp_list_index_asc, temp_list_index_des


def merge_sort(arr, arr_idx, low, high):

    if (low < high):

        m = low + (high - low) // 2

        merge_sort(arr, arr_idx, low, m)
        merge_sort(arr, arr_idx, m + 1, high)
        merge(arr, arr_idx, low, m, high)


def merge(arr, arr_idx, low, m, high):
    n1 = m - low + 1
    n2 = high - m

    L = [0] * (n1)
    R = [0] * (n2)

    L_idx = [0] * (n1)
    R_idx = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[low + i]
        L_idx[i] = arr_idx[low + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R_idx[j] = arr_idx[m + 1 + j]

    i = 0    
    j = 0    
    k = low

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr_idx[k] = L_idx[i]
            i += 1
        else:
            arr[k] = R[j]
            arr_idx[k] = R_idx[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        arr_idx[k] = L_idx[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        arr_idx[k] = R_idx[j]
        j += 1
        k += 1


def preurejanje_trakov(genom):

    genom = [0] + genom + [len(genom) + 1]

    breakpoints = count_breakpoints(genom)
    
    while (breakpoints > 0):

        print("Breakpoints: ", breakpoints)

        ascending, descending = find_parts(genom)

        if (len(descending) > 0):
            obrat = descending[0]
        
        else:

            for i in range(len(ascending)):

                if ascending[i][0] != 0:

                    obrni(genom, ascending[i][0], ascending[i][1])
                    obrat = ascending[i]

                    if (genom[ascending[i][1]] + 1 == genom[ascending[i][1] + 1]):
                        breakpoints -= 1

                    if (genom[ascending[i][0] - 1] + 1 == genom[ascending[i][0]]):
                        breakpoints -= 1

                    break

        for i in range(len(genom)):

            if (genom[i] + 1 == genom[obrat[1]]) and (i < obrat[1]):

                obrni(genom, i + 1, obrat[1])

                breakpoints -= 1

                if (genom[obrat[1]] + 1 == genom[obrat[1] + 1]):
                    breakpoints -= 1

                break

            elif (genom[i] + 1 == genom[obrat[1]]) and (i > obrat[1]):

                obrni(genom, obrat[1] + 1, i)

                breakpoints -= 1

                if (genom[obrat[1]] + 1 == genom[obrat[1] + 1]):
                    breakpoints -= 1

                break

        # print("Current state: ", genom)

    return genom


def find_parts_lastna_resitev(genom):

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

    merge_sort(descending, temp_list_index_des, 0, len(descending) - 1)

    return temp_list_index_asc, temp_list_index_des

def lastna_resitev(genom):

    genom = [0] + genom + [len(genom) + 1]
    # print("Start: ", genom)

    breakpoints = count_breakpoints(genom)
    
    index = 0

    while (breakpoints > 0):

        # print("Breakpoints: ", breakpoints)

        ascending, descending = find_parts_lastna_resitev(genom[index:])

        if (len(descending) > 0):
            obrat = descending[0]
        
        else:

            for i in range(len(ascending)):

                if ascending[i][0] != 0:

                    obrni(genom, ascending[i][0] + index, ascending[i][1] + index)

                    if (genom[ascending[i][1] + index] + 1 == genom[ascending[i][1] + index + 1]):
                        breakpoints -= 1

                    if (genom[ascending[i][0] + index - 1] + 1 == genom[ascending[i][0] + index]):
                        breakpoints -= 1

                    obrat = ascending[i]

                    break

        for i in range(index, len(genom) - 1):

            if (genom[i] + 1 == genom[obrat[1] + index]) and (i < obrat[1] + index):

                obrni(genom, i + 1, obrat[1] + index)

                breakpoints -= 1

                if (genom[obrat[1] + index] + 1 == genom[obrat[1] + index + 1]):
                    breakpoints -= 1

                break

            elif (genom[i] + 1 == genom[obrat[1] + index]) and (i > obrat[0] + index):

                obrni(genom, obrat[1] + 1 + index, i)

                breakpoints -= 1

                if (genom[i] + 1 == genom[i + 1]):
                    breakpoints -= 1

                break

        for i in range(index, len(genom) - 1):

            if (genom[i] + 1 == genom[i + 1]):
                index += 1

                if (index == len(genom) - 1):
                    breakpoints = 0
                    break

            else:
                break

        # print("Current state: ", genom, "\n")

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
    # print(result)
    

    #preurejanje trakov
    # start_time = time.time()

    # result = preurejanje_trakov(genom.copy())

    # print("Elapsed time: ", (time.time() - start_time) * 1000)
    # print(result)


    #lastna resitev
    start_time = time.time()

    result = lastna_resitev(genom.copy())

    print("Elapsed time: ", (time.time() - start_time) * 1000)
    # print("Result: ", result)
    
    print("Stevilo preobratov: ", obrat)

    # avg = 0

    # for i in range(100):
    #     start_time = time.time()

    #     result = lastna_resitev(genom.copy())

    #     avg += (time.time() - start_time)

    # print("Average time: ", avg * 10)

    # write to file
    with open("output.txt", "w") as output_file:

        for value in result:
            output_file.write("%i " % value)