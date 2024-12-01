from random import randint
rn_min = 1
rn_max = 100
turns = 10
rn = randint(rn_min,rn_max)

print('Я загадал число от 1 до 10')
print('Угадай его за',turns, 'попыток')

for i in range(turns):
    try:
        n = int(input(f'Какое число загадано({rn_min}...{rn_max}?)\n'))
        if n == rn:
            print('Точно,вы угадали с',(i + 1), 'попытки')
            break
    except:
        print('вы ввели не число')
    print('У вас осталось',turns - (i + 1), 'попыток')
