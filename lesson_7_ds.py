from defs import *

file = open('/files/article.txt', 'r', encoding='utf-8')
f = []
file = (file.read()).split('\n')

line_num = number_test()

if line_num < len(file):
    for n in range(line_num):
        print(file[-line_num+n])



world = []
max_world_len = 0

for i in file:
    f = i.split(' ')
    for g in f:
        n = g
        if max_world_len < len(n):
            max_world_len = len(n)
            world = [n]
        elif max_world_len == len(n):
            world.append(n)
            max_world_len = len(n)


print(f'Слово с максимальной длинной в {max_world_len} символов: {world[0]}')



name = input(f'Введите название файла:\n')
new_file = open(f'E:/reprisitoriy/reprisitoriy/reprisitoriy/files/{name}.txt', 'w')


a = input(f"Файл редактируется. Введите что-то:\n")

while a != "":
    new_file.write(f"{a}\n")
    a = input()
    for i in '!@#$%^&()_-=+':
        if a == i:
            a = ""
