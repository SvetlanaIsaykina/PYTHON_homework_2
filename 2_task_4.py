# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.

num_n = int(input('Введите число N: '))
num_x = - num_n
numbers = []

while num_x <= num_n:
    numbers.append(num_x)
    num_x += 1
print(numbers)

numbers = numbers[-2:] + numbers[:-2]

print(numbers)
