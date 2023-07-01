from random import randint

def valid(a):
    if a < 101 and a > 0:
        return True
    else:
        return False
    
cnum = randint(1, 100)
score = 0

while True:
    n = int(input("Введите число от одного до ста: "))
    if not valid(n):
        print ('А может быть все-таки введем целое число от 1 до 100?')
        continue
    
    elif n > cnum:
        print ('Ваше число больше загаданного, попробуйте еще разок')
        score += 1
        continue
        

    elif n < cnum:
        print ('Ваше число меньше загаданного, попробуйте еще разок')
        score += 1
        continue

    elif n == cnum:
        print ('Вы угадали, поздравляем!')
        print (f'Ваш счет: {score}')
        choice = input('Хотите начать игру заного? Y/N: ')
        
        if choice == 'Y' or choice == 'y':
            cnum = randint(1, 100)
            continue

        else:
            print ('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break