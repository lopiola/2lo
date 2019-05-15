# -*- coding: utf-8 -*-

# Program otrzymuje listę zbiorów liczb,
# następnie wypisuje listę sum liczb w każdym zbiorze.
# Dla podanego przykładu (list1) program powinien wypisać: [10, 22, 38]
#
# W programie popełniono jednak 2 błędy.
# Znajdź je żeby otrzymać poprawny wynik!

if __name__ == '__main__':
    list1 = [(1, 2, 3, 4), (4, 5, 6, 7), (8, 9, 10, 11)]

    list2 = []

    list_sum = 0

    for t in list1:
        for i in range(len(t)):
            list_sum = list_sum + t[i]
            list2.append(list_sum)

    print(list2)

