a, b = input("Введите два числа: \n").split()

a, b = map(int, (a, b))

if b !=0:
    print(f"{a}/{b}={a/b}")
else:
    print("Ошибка. На ноль делить нельзя.")



sum = int(input("Введите стоимость покупки: \n"))

if sum >= 20:
    sum_sk = round(sum*0.35, 2)
    sum = sum - sum_sk

print(f"Итоговая сумма покупки: {sum_sk} \n Скидка: {sum}")



#Напишите скрипт, который по введенному пользователем числу от 1 до 12, будет выводить на экран сообщение в виде названия месяца и времени года. Если пользователь введет недопустимое число, программа должна выдавать сообщение об ошибке.

month = int(input(f"Введите номер месяца: /n"))

#for i in range(12):

print("январь - 1")
print("февраль - 2")
print("март - 3")
print("апрель - 4")
print("май - 5")
print("июнь - 6")
print("июль - 7")
print("август - 8")
print("сентябрь - 9")
print("октябрь - 10")
print("ноябрь - 11")
print("декабрь - 12")

if month//3 == 1:
    season = "весна"
elif month//3 == 2:
    season = "лето"
elif month//3 == 3:
    season = "осень"
else:
    season = "зима"