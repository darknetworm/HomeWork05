import os

string = ' '
fileName = 'forHomeWork01.txt'

if os.path.exists(fileName):
    print(f'Создаваемый файл {fileName} уже существует. Он будет удален.')
    os.remove(fileName)

print(f'Для записи в файл {fileName} вводите данные (для окончания ввода нажмите два раза Enter)')

try:
    with open(fileName, 'a') as added:
        while string != '':
            string = input('>>>')
            print(string, file=added)
    print(f'Ввод закончен. Проверьте файл {fileName}')

except IOError:
    print('Где-то закралась ошибка')
