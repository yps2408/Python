#2 – Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности.
#Пример:
#[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

#список уникальных элементов
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
def get_unique(lst):
    result_list = list(filter(lambda x: (lst.count(x) == 1), lst))
    return result_list
print(f'Список уникальных элементов:\n{get_unique(my_list)}')

# Получаем список повторяемых элементов
def get_double(lst):
    result_list = sorted([x for i, x in enumerate(lst) if i != lst.index(x)])
    return result_list


print(f'Список повторяемых элементов:\n{get_double(my_list)}')

# Убираем дубликаты из заданной последовательности.
def delete_double(lst):
    result_list = []
    [result_list.append(x) for x in lst if x not in result_list]
    return result_list


print(f'Список без дубликатов:\n{delete_double(my_list)}')