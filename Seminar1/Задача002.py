from ast import For

a=int(input("Введите A:"))
b=int(input("Введите B:"))
c=int(input("Введите C:"))
d=int(input("Введите D:"))
e=int(input("Введите E:"))
max = a
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
if e > max:
    max = e
print(max)