# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input())
out_list = []
while number > 0:
    out_list.append(str(number % 2))
    number //= 2
out_list.reverse()
print(*out_list, sep='')
