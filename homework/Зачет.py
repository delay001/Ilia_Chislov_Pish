# Считываем массив с клавиатуры
while True:
    try:
        user_input = input("Введите 10 чисел через пробел: ").strip()
        user_input = " ".join(user_input.split())  # Удаляем лишние пробелы
        array = list(map(int, user_input.split()))
        if len(array) != 10:
            raise ValueError("Должно быть введено ровно 10 чисел.")
        break
    except ValueError as e:
        print(f"Ошибка ввода: {e}. Попробуйте снова.")

# Определяем середину массива
mid = len(array) // 2

# Инвертируем первую и вторую половины массива
array[:mid] = array[:mid][::-1]
array[mid:] = array[mid:][::-1]

# Выводим результирующий массив
for element in array:
    print(element, end=' ')
