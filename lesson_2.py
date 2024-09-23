a, b, c = input('Введите три числа:').split()

if (a+b+c).isdigit():

    a, b, c = map(int, (a, b, c))

    if a>b and c>b:
        print(f"min: {b}")
    elif c>a and b>a:
      print(f"min: {a}")
    else:
      print(f"min: {c}")
else:
    print("Ошибка, вводи целые!")

for a in range(3):
    a=input("Введите число:")
    if a.isdigit():
        if 1 <= int(a) <= 3:
            print(f"Число {a} преданделит интервалу [1;3]")
        else:
            print(f"Число {a} не преданделит интервалу [1;3]")
    else:
        print("Ошибка, вводи целые!")