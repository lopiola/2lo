import sys

def longest_non_dec_seq(numbers):
    # TODO Funkcja powinna znalezc najdluzszy niemalejacy podciag w zadanym
    # ciagu liczb. Podciag nie musi byc spojny, tzn kolejne wartosci nie
    # musza wystepowac kolo siebie w tablicy wejsciowej, natomiast
    # musi byc zachowana ich kolejnosc. Przyklad:
    #
    # wejscie: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    # wyjscie: [0,    4,            6,        9,    13,           15]
    #
    # Zatem odpowiedzia na powyzsze jest podciag o dlugosci 6, 
    # przykladowo: [0, 4, 6, 9, 13, 15]
    #
    # Moze byc wiecej niz jeden poprawny podciag (liczy sie, zeby byl
    # najdluzszy). Funkcja check_lnds sprawdza, czy otrzymana dlugosc
    # jest zgodna z oczekiwana i czy rzeczywiscie znaleziony podciag jest
    # niemalejacy.
    #
    # Funkcja powinna zwrocic przykladowy znaleziony najdluzszy podciag.
    return []


def check_lnds(counter, expected_length, input):
    result = longest_non_dec_seq(input)
    if len(result) != expected_length:
        print(
            "{} Error! The correct result length should be {} (got {}: {})".format(
                counter, expected_length, len(result), result))
        sys.exit(1)

    for i in range(1, len(result)):
        if result[i-1] > result[i]:
            print(
                "{} Error! This is not a non-decreasing sequence: {}".format(
                    counter, result))
            sys.exit(1)

    print("{} Ok! {}".format(counter, result))


if __name__ == "__main__":
    check_lnds(1, 6, [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    check_lnds(2, 5, [12, 44, 90, 42, 86, 62, 62, 61, 9, 41, 66])
    check_lnds(3, 2, [69, 86, 50, 55, 51, 12, 13])
    check_lnds(4, 6, [22, 1, 2, 28, 49, 18, 37, 65, 14, 24, 62, 98, 10, 7, 84])
    check_lnds(5, 6, [16, 72, 23, 48, 29, 59, 88, 80, 33, 80, 33, 38])
    check_lnds(6, 4, [40, 74, 68, 49, 74, 13, 73, 30, 98, 21, 32, 2, 67, 47])
    check_lnds(7, 6, [7, 9, 58, 95, 19, 14, 99, 100, 60, 46, 15])
