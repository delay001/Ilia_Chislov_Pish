
number = input("Введите целое число: ")

is_increasing = True
for i in range(len(number) - 1):
    if number[i] >= number[i + 1]:  
        is_increasing = False
        break

if is_increasing:
    print("Цифры числа расположены в порядке возрастания.")
else:
    print("Цифры числа не расположены в порядке возрастания.")
