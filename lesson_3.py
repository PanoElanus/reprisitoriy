s = int(input(f"Введите стоимость 1 кг конфет \n"))
summ = 0

for i in range(1,11):
    print(f"Цена {i} кг конфет: {s*i}")


# (ctrl+/) ставит #
# format

a=1
sum = 0
num = 0

while a != 0:
    a=int(input(f"Введите число \n"))
    num += 1
    sum += a

print(f"Сумма последовательности: {sum} \nКоличество элементов: {num}")


list = [1, '2', 3, 4, '5', '!', 'FF', '5', '7!']
suma = 0

for n in list:
    if str(n).isdigit(): #or int(n, 16):
        suma += int(n)
print(f"Сумма всех элементов списка: {suma}")




o = int(input(f"Введите число овечек\n"))
k = [12, 13, 14]

for number in range(1, o+1):
    ost = number % 100

    if number % 10 == 1 and ost != 11:
        ovechka = "овечка"
    elif 2 <= number % 10 <= 4 and 14 < ost and ost > 12:
        ovechka = "овечки"
    else:
        ovechka = "овечек"
    print(number, ovechka)


