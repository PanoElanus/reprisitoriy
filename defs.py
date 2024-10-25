import random


def int_two_number_test(a, b):
    while not(a.isdigit()) or not(b.isdigit()):
        # print("Введите число.")
        a, b = input(f"Введите числа:\n").split()
    a, b = map(int, (a, b))
    return a, b



def number_test():
    a = input(f"Введите число:\n")
    while not(a.isdigit()):
        a = input(f"Введите ЧИСЛО:\n")
    return a


def many_number_test(n):
    a = []
    for i in range(n):
        a.append(input(f'Введите число:\n'))
    for i in range(len(a)):
        c = a[i]
        while not(c.isdigit()):
            i = input(f"Введите ЧИСЛО:\n")
        a[i] = int(c)
    return a




def two_system(N):
    N3 = ""
    while N//2 != 0:
        N2 = N%2
        N = N//2
        N3 = str(N2) + N3
    N3 = str(N%2) + N3
    return N3



# x - столбцы, y - строки 

def masif_random(x, y):
    masif = []
    a = []

    for n in range(x):
        for i in range(y): a.append(random.randint(-100, 100))
        masif.append(a)
        a=[]
    return masif