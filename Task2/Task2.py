# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

some_list = [1, 2, 3, 4, 5, 6, 7, 8]
newlist = []
for i in range(len(some_list)//2):
    newlist.append(some_list[i]*some_list[-i-1])
print(newlist)
