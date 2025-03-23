import sys
from math import sqrt
from itertools import combinations
import time

def brute_force(multiset):

    # calculate n
    # no need for second root to be calculated, because multiset is always positive.
    n = int((1 + sqrt(1 + 4 * (2 * len(multiset)))) // 2)

    # max element in multiset
    M = max(multiset)

    result = []

    for combination in combinations(multiset, n - 2):
        X = [0] + list(combination) + [M]
        delta_x = delta(X)

        if delta_x == multiset and X not in result:
            result.append(X)

    return result



def partial_digest(multiset):

    width = max(multiset)

    multiset.pop()

    X = [0, width]

    results = []

    place(multiset, X, results, width)

    return results



def place(multiset, X, results, width):

    if (len(multiset) == 0):
        results.append(sorted(X))
        return
    
    y = max(multiset)

    y_set = set(find_distances(y, X))

    if (y_set.issubset(multiset)):

        X.append(y)
        for i in y_set:
            multiset.remove(i)

        place(multiset, X, results, width)

        X.remove(y)
        for i in y_set:
            multiset.append(i)

    width_set = set(find_distances(width - y, X)) # width is always larger than y

    if (width_set.issubset(multiset)):

        X.append(width - y)
        for i in width_set:
            multiset.remove(i)

        place(multiset, X, results, width)

        X.remove(width - y)
        for i in width_set:
            multiset.append(i)

    return



def delta(indexes):

    resulting_set = []

    for i in range(len(indexes)):
        resulting_set += find_distances(indexes[i], indexes[i + 1:])

    resulting_set.sort()

    return resulting_set



def find_distances(number, set):
    
    result = []

    for i in set:
        result.append(abs(i - number))

    return result


if __name__ == '__main__':

    #read file
    file = open(sys.argv[1])

    text = file.read()

    file.close()


    #declare restriction cuts
    # restriction_cuts = ["GTGTG"]                                  #DNK1
    # restriction_cuts = ["TTCC", "CTCTCT"]                         #DNK1
    # restriction_cuts = ["AAAA", "CCCC", "TTTT", "GGGG"]           #DNK1
    # restriction_cuts = ["ACTACT", "GGAGGA", "GAGGCC", "CTCTCT"]   #DNK2
    restriction_cuts = ["TTTTTTT", "GTGTCGT", "ACACACA"]            #DNK3


    #find indexes of each cut
    indexes = []
    occurrence_frequencies = []

    for cut in restriction_cuts:

        found_index = -1
        freq = 0

        while True:
            found_index = text.find(cut, found_index + 1)

            if (found_index == -1):
                occurrence_frequencies.append(freq)
                break

            indexes.append(found_index)
            freq += 1

        if (len(indexes) == 0):
            print("Restriction cut couldn't be found!")
            sys.exit()
    
    indexes.append(0)
    indexes.append(len(text) - 1)

    indexes.sort()


    #find multiset

    multiset = delta(indexes)

    print("Found multiset: ", multiset)
    
    for i in range(len(restriction_cuts)):
        print("Frequency of ", restriction_cuts[i], ": ", occurrence_frequencies[i] / len(text))

    #brute force
    # start_time = time.time()
    
    # X_final = brute_force(multiset.copy())

    # print("Elapsed time for brute force: ", (time.time() - start_time) * 1000)
    # print("Result: ", X_final)

    # razveji in omeji
    start_time = time.time()

    X_final = partial_digest(multiset.copy())

    print("Elapsed time for divide and conquer: ", (time.time() - start_time) * 1000)
    print("Result: ", X_final)


    #write to file
    output_file = open("cuts_output.txt", "w")

    output_file.write(''.join(str(value) for value in X_final))

    output_file.close()

    # avg = 0

    # for i in range(10):

    #     start_time = time.time()
    #     brute_force(multiset.copy())
    #     avg += (time.time() - start_time) * 1000

    # print("Average time for brute force is: ", avg / 10)

    # avg = 0

    # for i in range(100):

    #     start_time = time.time()
    #     partial_digest(multiset.copy())
    #     avg += (time.time() - start_time) * 1000

    # print("Average time for divide and conquer is: ", avg / 100)



