# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

while True:
    user_num = input('Введите число:\n')
    if user_num.isdigit():
        user_num = int(user_num)
        break
    else:
        print('Необходимо ввести число.')

print(f'{user_num} + {user_num}{user_num} + {user_num}{user_num}{user_num} = {user_num}{user_num * 2}{user_num * 3}')
