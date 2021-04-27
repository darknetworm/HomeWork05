users = {}
usersSalary = 0
count = 0

try:
    with open('forHomeWork03.txt') as salary:
        print('Оклад менее 20000 Пиастров имеют следующие сотрудники:')
        for line in salary.readlines():
            userSalary = float(line.split()[1])
            if userSalary < 20000:
                print(line.split()[0])
            usersSalary += userSalary
            count += 1
    print(f'\nСредний оклад {count} сотруднuков составляет {usersSalary / count:.2f} Пиастров')

except IOError:
    print('Где-то закралась ошибка')
