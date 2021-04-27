import os
from random import randint

stringToPut = ''
numStrFile = 'forHomeWork05.txt'

if os.path.exists(numStrFile):
    os.remove(numStrFile)

print(f'Первая часть: создаем файл {numStrFile} и заполняем его числами в виде строки')
try:
    numCount = int(input('Введите количество чисел для записи в файл (будут сгенерированы автоматически от 0 до 99): '))

except ValueError:
    exit('Вы ввели не число')

for i in range(0, numCount):
    stringToPut = (stringToPut + str(randint(0, 100)) + ' ')

try:
    with open(numStrFile, 'w') as added:
        print(stringToPut, file=added)
    print(f'Числа {stringToPut} сгенерированы и записаны в файл {numStrFile}')

except IOError:
    print('Где-то закралась ошибка')

print(f'\nВторая часть: открываем файл {numStrFile} и выполняем суммирование чисел из строки')
try:
    with open(numStrFile) as reading:
        print(f'Сумма чисел из строки в файле {numStrFile} равна {sum(map(int, (reading.read()).split()))}')

except IOError:
    print('Где-то закралась ошибка')
