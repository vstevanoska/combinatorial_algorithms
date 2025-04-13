import sys
import time
from itertools import product

def greedy_method(n_meri, n, t, l):

    matrika_poravnave = []

    for combination in product(range(n - l + 1), repeat=t):
        matrika_poravnave.append(combination)

    best_score = 0
    best_con = ""

    #ACTG

    for poravnava in matrika_poravnave:

        profil = []

        for i in range(l):

            temp_profil = [0] * 4

            for j in range(t):

                if n_meri[j][i + poravnava[j]] == 'A':
                    temp_profil[0] += 1
                elif n_meri[j][i + poravnava[j]] == 'C':
                    temp_profil[1] += 1
                elif n_meri[j][i + poravnava[j]] == 'T':
                    temp_profil[2] += 1
                elif n_meri[j][i + poravnava[j]] == 'G':
                    temp_profil[3] += 1

            profil.append(temp_profil)

        cons_score = 0

        for i in range(l):
            cons_score += max(profil[i])

        if (cons_score > best_score):

            best_score = cons_score
            best_con = ""

            idx = 0

            for i in range(l):

                for j in range(4):
                    if profil[i][j] > profil[i][idx]:
                        idx = j

                if (idx == 0):
                    best_con += "A"
                elif (idx == 1):
                    best_con += "C"
                elif (idx == 2):
                    best_con += "T"
                elif (idx == 3):
                    best_con += "G"

    return best_con, best_score

if __name__ == '__main__':

    file = open(sys.argv[1])

    text = file.read()

    file.close()

    n = int(input("Vnesite velikost n-merov: "))
    t = int(input("Vnesite velikost t-merov: "))
    l = int(input("Vnesite velikost l-merov: "))

    # n = 15
    # t = 5
    # l = 5

    n_meri = []

    n_count = 0

    for i in range(t):
        n_meri.append(text[n_count : (n + n_count)])
        n_count += n


    start_time = time.time()

    sequence, score = greedy_method(n_meri, n, t, l)

    print("Cas izvajanja: ", time.time() - start_time)
    print("Rezultat pozresne metode: ", sequence, " (", score, ")"),

    
