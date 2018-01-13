import sys

class Item:
    def __init__(self, name, val, weight, limit): 
        self.name = name
        self.val = val
        self.weight = weight
        self.limit = limit


def coin_change(amount, coins):
    # TODO
    return 0


def knapsack(capacity, weights, values):
    # TODO
    return 0


def knapsack_advanced(capacity, items):
    # TODO
    return 0, {}


def check(counter, expected, actual):
    if expected == actual:
        print("{} Ok!".format(counter))
    else:
        print("{} Error!".format(counter))
        print("   expected: {}".format(expected))
        print("        got: {}".format(actual))
        sys.exit(1)


def check_zad1():
    print("Problem wydawania reszty")

    check(1,  2, coin_change(  10, [1, 2, 5]))
    check(2,  3, coin_change(   9, [1, 2, 5]))

    check(3, 10, coin_change( 250, [1, 3, 7, 100]))
    check(4, 17, coin_change( 196, [1, 3, 7, 100]))

    check(5,  2, coin_change( 501, [1, 2, 5, 10, 20, 50, 100, 200, 500]))
    check(6,  6, coin_change( 758, [1, 2, 5, 10, 20, 50, 100, 200, 500]))
    check(7,  5, coin_change(1035, [1, 2, 5, 10, 20, 50, 100, 200, 500]))
    

def check_zad2():
    print("Problem plecakowy")

    check(1, 220, knapsack(50, [10, 20, 30],      [60, 100, 120]))
    check(2, 160, knapsack(30, [10, 20, 30],      [60, 100, 120]))

    check(3,  18, knapsack(20, [3, 7, 9, 20, 40], [3, 5, 10, 15, 44]))
    check(4,  25, knapsack(30, [3, 7, 9, 20, 40], [3, 5, 10, 15, 44]))
    check(5,  44, knapsack(40, [3, 7, 9, 20, 40], [3, 5, 10, 15, 44]))
    check(6,  54, knapsack(50, [3, 7, 9, 20, 40], [3, 5, 10, 15, 44]))
    check(7,  62, knapsack(60, [3, 7, 9, 20, 40], [3, 5, 10, 15, 44]))


def check_zad3():
    print("Problem plecakowy - wersja rozszerzona")

    cukier =    Item("cukier",    val=2, weight=10, limit=3)
    maslo =     Item("maslo",     val=4, weight=2,  limit=2)
    czekolada = Item("czekolada", val=3, weight=1,  limit=2)
    jajka =     Item("jajka",     val=8, weight=5,  limit=2)
    szynka =    Item("szynka",    val=3, weight=1,  limit=1)
    ser =       Item("ser",       val=6, weight=2,  limit=3)

    check(1,             (6, {'czekolada': 2}), 
        knapsack_advanced(2,  [cukier, maslo, czekolada, jajka, szynka, ser]))

    check(2,             (12, {'czekolada': 2, 'ser': 1}), 
        knapsack_advanced(4,  [cukier, maslo, czekolada, jajka, szynka, ser]))

    check(3,             (15, {'czekolada': 2, 'szynka': 1, 'ser': 1}), 
        knapsack_advanced(5,  [cukier, maslo, czekolada, jajka, szynka, ser]))

    check(4,             (27, {'czekolada': 2, 'szynka': 1, 'ser': 3}), 
        knapsack_advanced(9,  [cukier, maslo, czekolada, jajka, szynka, ser]))

    check(5,             (35, {'maslo': 2, 'czekolada': 2, 'szynka': 1, 'ser': 3}), 
        knapsack_advanced(13, [cukier, maslo, czekolada, jajka, szynka, ser]))

    check(6,             (39, {'maslo': 1, 'czekolada': 2, 'jajka': 1, 'szynka': 1, 'ser': 3}), 
        knapsack_advanced(16, [cukier, maslo, czekolada, jajka, szynka, ser]))

    check(7,             (44, {'maslo': 1, 'czekolada': 2, 'jajka': 2, 'ser': 3}), 
        knapsack_advanced(20, [cukier, maslo, czekolada, jajka, szynka, ser]))

    check(8,             (53, {'cukier': 1, 'maslo': 2, 'czekolada': 2, 'jajka': 2, 'szynka': 1, 'ser': 3}), 
        knapsack_advanced(33, [cukier, maslo, czekolada, jajka, szynka, ser]))



if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Podaj numer zadania: zad1 | zad2 | zad3")
    else:
        if (sys.argv[1] == "zad1"):
            check_zad1()
        elif (sys.argv[1] == "zad2"):
            check_zad2()
        elif (sys.argv[1] == "zad3"):
            check_zad3()
        else:
            print("Podaj numer zadania: zad1 | zad2 | zad3")