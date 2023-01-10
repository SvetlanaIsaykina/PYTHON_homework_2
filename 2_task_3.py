# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй

line_one = input('Введите первую строку: ')
line_two = input('Введите вторую строку: ')

for l in range(len(line_one)):
  count = 0
  for el in range(len(line_two)):
    if line_one[l] == line_two[el]:
      count += 1
  print(f'{line_one[l]} - {count}')

