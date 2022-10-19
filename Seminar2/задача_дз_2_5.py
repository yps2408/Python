#5. Реализуйте алгоритм перемешивания списка.

import random


def fill_list(n=10, min=0, max=100) -> list: 
    new_list = [random.randint(min, max)]
    for i in range(1, n):
        new_list.append(random.randint(min, max))
        i += 1
    return new_list

def shuffling_list(user_list):
    for i in range(len(user_list)-1, 0, -1):
        j = random.randint(0, i + 1)
        user_list[i], user_list[j] =user_list[j], user_list[i]
    return user_list

n = int(input('Количество элементов списка: '))
min = int(input('Граница 1 диапазона значений элементов списка: '))
max = int(input('Граница 2 диапазона значений элементов списка: '))
if max < min:
    max, min = min, max
source_list = fill_list(n, min, max)
print(source_list)
mixed_list = shuffling_list(source_list)
print(mixed_list)