'''Для проверки работоспособности можно "поиграть" с перемещением строк в файле с английскими числительными'''
import os

engFile = 'forHomeWork04.txt'
rusFile = 'newHomeWork04.txt'

if os.path.exists(rusFile):
    os.remove(rusFile)

engToRus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шеть',
            'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}

print(f'Преобразуем английские числительные в файле {engFile} в русские')
try:
    with open(engFile) as numbering:
        for line in numbering.readlines():
            for key in engToRus:
                if key == (line.split('-')[0]):
                    newString = line.replace(key, engToRus.get(key))
                    print(newString.replace('\n', ''))
                    with open(rusFile, 'a') as added:
                        print(newString.replace('\n', ''), file=added)

except IOError:
    print('Где-то закралась ошибка')

print(f'\nПреобразование завершено. Проверьте файл {rusFile}')
