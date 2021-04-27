from json import dump

profitFirmList = {}
averageList = {}
sumProfit = 0
count = 0

try:
    with open('forHomeWork07.txt') as dictionary:
        for subject in dictionary.readlines():
            firmProfit = int(subject.split()[2]) - int(subject.split()[3])
            firmName = subject.split()[1] + ' ' + subject.split()[0]
            profitFirmList[firmName] = firmProfit
            if firmProfit >= 0:
                sumProfit += firmProfit
                count += 1
                print(f'{firmName} получила прибыль в сумме {firmProfit} Пиастров')
            else:
                print(
                    f'{firmName} получила убытки в сумме {abs(firmProfit)} Пиастров и в расчет средней прибыли включена не будет')
    averageList['average_profit'] = int(sumProfit / count)
    listTotal = [profitFirmList, averageList]
    print(f'\nОкончательный список: {listTotal}')

except IOError:
    print('Где-то закралась ошибка')

try:
    with open('newHomeWork07.json', 'w') as final:
        print('Создаем json-объект в файле newHomeWork07.json')
        dump(listTotal, final)

except IOError:
    print('Где-то закралась ошибка')
