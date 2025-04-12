import sys
import time
from itertools import product

def greedy_method(n_meri, n, t, l):

    matrika_poravnave = []

    for combination in product(range(n - l + 1), repeat=t):
        matrika_poravnave.append(combination)

    print(matrika_poravnave)


    return

if __name__ == '__main__':

    file = open(sys.argv[1])

    text = file.read()

    file.close()

    # n = int(input("Vnesite velikost n-merov: "))
    # t = int(input("Vnesite velikost t-merov: "))
    # l = int(input("Vnesite velikost l-merov: "))

    n = 10
    t = 2
    l = 3

    n_meri = []

    n_count = 0

    for i in range(t):
        n_meri.append(text[n_count : (n + n_count)])
        n_count += 1


    start_time = time.time()

    regulatory_sequence = greedy_method(n_meri, n, t, l)

    print("Cas izvajanja: ", time.time() - start_time)
    print("Rezultat pozresne metode: ", regulatory_sequence)

    # start_time = time.time()

    # regulatory_sequence = branch_and_bound()

    # print("Cas izvajanja: ", time.time() - start_time)
    # print("Rezultat razveji in omeji: ", regulatory_sequence)

    
