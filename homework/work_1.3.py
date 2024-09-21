
a = int(input("Введите число a (не больше 100): "))
b = int(input("Введите число b (не больше 100): "))


if a > b or abs(a) > 100 or abs(b) > 100:
    print("Ошибка: a должно быть меньше или равно b, а оба числа по модулю не должны превышать 100.")
else:

    sum_of_squares = sum(i ** 2 for i in range(a, b + 1))
    print(f"Сумма квадратов от {a} до {b} = {sum_of_squares}")