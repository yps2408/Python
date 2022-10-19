#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def sum(list1):
    sum = 0
    for i in range (1, len(list1), 2):
        sum += list1[i]
    return sum

list = [2, 3, 5, 9, 3]

result = sum(list)
print(list)
print(f'Сумма элементов, стоящих на нечетной позиции = {result}')