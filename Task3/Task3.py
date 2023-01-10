# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

lisst = [1.1, 1.2, 3.1, 5, 10.01]
newLisst = []
for i in lisst:
    newLisst.append(i-int(i))
result = max(newLisst)-min(newLisst)
print(format(result, '.2f'))