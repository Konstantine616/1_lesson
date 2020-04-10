# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    num = input('Введите число любой длинны:\n')
    if num.isdigit():
        num = int(num)
        break
    else:
        print('Необходимо ввести целое число.')

n = 0
while num > 1:
    if n < num%10:
        n = int(num%10)
    num = num/10
    print(f'{n}, {num:.2f}')

print(int(n))
