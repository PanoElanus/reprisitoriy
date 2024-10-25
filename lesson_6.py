import random
from defs import masif_random


# masif = []
# a = []

# for n in range(3):
#     for i in range(3): a.append(random.randint(0, 100))
#     masif.append(a)
#     a=[]

# max_a = max(masif[2])
# print(masif, max_a)





# # m, n = input().split()
# # m, n = int(m), int(n)
# # mn1, mn2 = [], []

# # mn = masif_random(m, n)
# # print(mn)

# # for i in range(m):
# #     for j in range(n):
# #         if (mn[i][j]) >= 0:
# #             p = 1
# #         else: p = 0
# #         mn1.append(p)
# #     mn2.append(mn1)
# #     mn1 = []

# # print(mn2)



# # a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]



# n = int(input())
# a = masif_random(n, n)
# c, num = 0, 0

# for i in range(len(a)):
#     c += a[i][i]

# for i in range(len(a)):
#     b = 0
#     for j in range(len(a[i])):
#         b += a[i][j]
#     if b != c:
#         print('Не магическая')
#         break
#     else: 
#         num += 1
#         if num == n:
#             print('Магическая')





a = [[1, 0, 3], [0, 6, 4], [3, 4, 8]]
n = 3

for i in range(n):
    for j in range(i+1, len(a[i])):
        if a[i][j] != a[j][i]:
            print(f'Матрица {a} не симметрична')
            n = False

if n:
    print(f'Матрица {a} симметрична')
    
    