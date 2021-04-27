count = 0

try:
    with open('forHomeWork02.txt') as reading:
        for line in reading.readlines():
            count += 1
            print(
                'Строка {}: "{}". Количество слов в строке: {}'.format(count, line.replace('\n', ''),
                                                                       len(line.split())))
    print(f'Итого в файле {count} строк')

except IOError:
    print('Где-то закралась ошибка')
