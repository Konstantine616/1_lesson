# Поработайте с переменными, создайте несколько, выведите на экран
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 1
b = 2.1
c = '"three"'
d = True
e = [a, b, c, d]

print(f'{a} is {type(a)}')
print(f'{b} is {type(b)}')
print(f'{c} is {type(c)}')
print(f'{d} is {type(d)}')
print(f'{e} is {type(e)}')

user_var = input('Введите что нибудь:\n')
if user_var.isdigit():
    user_var = int(user_var)
    print(f'{user_var} is class int')
else:
    print(f'{user_var} is {type(user_var)}')

