# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


from datetime import datetime
import time

def Random_number (min, max):
    if abs(max) > abs (min):
        check = min - 1
        max_abs = max + 1
    else:
        check = max + 1
        max_abs = min - 1
    random_number = check
    while random_number < min or random_number > max:
        temp_number = (float(time.time()) * float(datetime.now().time().microsecond)) / 1000000
        sign = -1
        if int(temp_number) % 2 != 0:
            sign = 1
        temp_number = temp_number - int(temp_number)
        random_number = abs(max_abs) * temp_number * sign
        random_number = int(random_number)
        time.sleep(0.000001)
    return random_number

def Creat_file(str, k):
    with open(str, 'w') as file:
        for i in range(k, -1, -1):
            temp = Random_number (-10, 10)
            if i == k:
                if temp < 0:
                    file.write(f'{temp}x**{i} ')
                if temp > 0:
                    file.write(f'{temp}x**{i} ')
            elif i == 0:
                if temp < 0:
                    file.write(f'- {-temp} ')
                if temp > 0:
                    file.write(f'+ {temp} ')
            elif i == 1:
                if temp < 0:
                    file.write(f'- {-temp}x ')
                if temp > 0:
                    file.write(f'+ {temp}x ')
            elif temp != 0:
                if temp < 0:
                    file.write(f'- {-temp}x**{i} ')
                if temp > 0:
                    file.write(f'+ {temp}x**{i} ')
        file.write('= 0')

def String_to_list(str):
    str = str.replace('- ','-')
    str = str.replace('+ ','+')
    str = str.replace('+','')
    str = str.replace(' = 0','')
    list = str.split(' ')
    return list

def List_to_dict(list):
    new_dict = {}
    for i in list:
        if i.find('x**') != -1:
            i = i.replace('x**', ' ')
            temp_list = i.split(' ')
            new_dict[temp_list[1]] = int(temp_list[0])
        elif i.find('x') != -1:
            i = i.replace('x', ' ')
            temp_list = i.split(' ')
            new_dict['1'] = int(temp_list[0])
        else:
            new_dict['0'] = int(i)
    return new_dict
        


print('Введите натуральную степень k:')
k = int(input())
print('Введити имя первого файла:')
Creat_file(name_first := input() + '.txt', k)
print('Введити имя второго файла:')
Creat_file(name_second := input() + '.txt', k)

with open(f'{name_first}') as file:
    text_first = file.read()

with open(f'{name_second}') as file:
    text_second = file.read()

list_first = String_to_list(text_first)

list_second = String_to_list(text_second)

dict_first = List_to_dict(list_first)
dict_second = List_to_dict(list_second)


result_dict = {}
for i in range(k, -1, -1):
    if dict_first.get(str(i)) != None and dict_second.get(str(i)) != None:
        result_dict[str(i)] = dict_first[str(i)] + dict_second[str(i)]
    elif dict_first.get(str(i)) != None:
        result_dict[str(i)] = dict_first[str(i)]
    elif dict_second.get(str(i)) != None:
        result_dict[str(i)] = dict_second[str(i)]

result_string = ''
for i in result_dict:
    if i == '1':
        if result_dict[i] > 0:
            result_string += f'+ {result_dict[i]}x '
        elif result_dict[i] == 0:
            result_string += ''
        else:
            result_string += f'- {-(result_dict[i])}x '
    elif i != "0":
        if result_dict[i] > 0:
            result_string += f'+ {result_dict[i]}x**{i} '
        elif result_dict[i] == 0:
            result_string += ''
        else:
            result_string += f'- {-(result_dict[i])}x**{i} '
    else:
        if result_dict[i] > 0:
            result_string += f'+ {result_dict[i]} '
        elif result_dict[i] == 0:
            result_string += ''
        else:
            result_string += f'- {-(result_dict[i])} '

result_string += '= 0'

if result_string.find('+', 0, 1) != -1:
    result_string = result_string.replace('+', '', 1)


with open('result.txt', 'w') as file:
   file.write(result_string)


with open(f'{name_first}') as file:
    print(f'файл "{name_first}" содержит многочлен:\n{file.read()}')

with open(f'{name_second}') as file:
    print(f'файл "{name_second}" содержит многочлен:\n{file.read()}')

with open('result.txt') as file:
    print(f'файл "result.txt" содержит результирующий многочлен:\n{file.read()}')