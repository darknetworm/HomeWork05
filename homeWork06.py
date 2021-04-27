subjectDict = {}

try:
    with open('forHomeWork06.txt') as dictionary:
        for subject in dictionary.readlines():
            subjectDict[subject.split(':')[0]] = sum(map(int, ((((((subject.split(':')[1].replace(' ', '')).replace('-',
            '')).replace('(л)', ' ')).replace('(пр)', ' ')).replace('(лаб)', ' ')).replace('\n', '')).split()))
    print(f'Словарь, полученный из файла forHomeWork06.txt: {subjectDict}')

except IOError:
    print('Где-то закралась ошибка')
