n = int(input("Введите натуральное число (не больше 100): "))

if n > 100 or n < 1:
    print("Число должно быть натуральным и не превышать 100.")
else:
    for i in range(1, n + 1):
        square = i ** 2
        cube = i ** 3
        print(f"{i}: квадрат = {square}, куб = {cube}")