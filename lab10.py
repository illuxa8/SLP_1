import math

# Функція для додавання
def add(x, y):
    return x + y

# Функція для віднімання
def subtract(x, y):
    return x - y

# Функція для множення
def multiply(x, y):
    return x * y

# Функція для ділення
def divide(x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    return x / y

# Функція для піднесення до степеня
def power(x, y):
    return x ** y

# Функція для квадратного кореня
def square_root(x):
    if x < 0:
        return "Неможливо взяти квадратний корінь від від'ємного числа"
    return math.sqrt(x)

# Функція для залишку від ділення
def modulo(x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    return x % y

# Змінна для зберігання значення пам'яті
memory = None

# Список для зберігання історії обчислень
history = []

# Налаштування за замовчуванням
decimal_places = 2  # Кількість десяткових розрядів
memory_enabled = True  # Функція пам'яті увімкнена

while True:
    # Перевірка дійсності введеного оператора
    while True:
        operator = input("Введіть операцію (виберіть одне з: '+', '-', '*', '/', '^', '√', '%', 'M+', 'MR', 'H', 'S', 'D'): ").lower()
        if operator in ('+', '-', '*', '/', '^', '√', '%', 'm+', 'mr', 'h', 's', 'd'):
            break
        else:
            print("Помилка! Введена операція не є дійсною. Спробуйте ще раз.")

    if operator == 'm+':
        # Зберігання результату в пам'яті
        memory = result if 'result' in locals() else None
    elif operator == 'mr':
        # Отримання значення з пам'яті
        if memory is not None:
            print(f"Значення з пам'яті: {memory}")
        else:
            print("Пам'ять порожня")
    elif operator == 'h':
        # Виведення історії обчислень
        if len(history) > 0:
            print("\nІсторія обчислень:")
            for i, entry in enumerate(history, start=1):
                print(f"{i}. Вираз: {entry['expression']}, Результат: {entry['result']:.{decimal_places}f}")
        else:
            print("Історія порожня")
    elif operator == 's':
        # Налаштування кількості десяткових розрядів
        decimal_places = int(input("Введіть кількість десяткових розрядів: "))
    elif operator == 'd':
        # Налаштування функції пам'яті
        memory_enabled = not memory_enabled
        if memory_enabled:
            print("Функція пам'яті увімкнена.")
        else:
            print("Функція пам'яті вимкнена.")
    elif operator in ('+', '-', '*', '/', '^', '%'):
        # Введення чисел від користувача (десяткові числа)
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        # Вибір операції та виклик відповідної функції
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        elif operator == '^':
            result = power(num1, num2)
        elif operator == '%':
            result = modulo(num1, num2)

        # Збереження запису історії
        history.append({'expression': f"{num1} {operator} {num2}", 'result': result})

        # Виведення результату з налаштуваною кількістю десяткових розрядів
        print(f"Результат: {result:.{decimal_places}f}")

    elif operator == '√':
        # Введення числа для обчислення квадратного кореня
        num1 = float(input("Введіть число для обчислення квадратного кореня: "))

        # Вибір операції та виклик відповідної функції
        result = square_root(num1)
        if isinstance(result, str):
            print(result)
        else:
            # Збереження запису історії
            history.append({'expression': f"√{num1}", 'result': result})

            # Виведення результату з налаштуваною кількістю десяткових розрядів
            print(f"Результат: {result:.{decimal_places}f}")

    # Питання користувачу про продовження
    again = input("Бажаєте виконати ще одне обчислення? (так/ні): ").lower()
    if again != 'так':
        if again != 'ні':
            print("Помилка! Введіть 'так' або 'ні'.")
        else:
            break
