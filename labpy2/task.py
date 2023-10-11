import math

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        try:
            self.result = x / y
            return self.result
        except ZeroDivisionError:
            return "Помилка: Неможливо поділити на нуль"
        except Exception as e:
            return f"Помилка: {str(e)}"

    def power(self, x, y):
        self.result = x ** y
        return self.result

    def square_root(self, x):
        if x < 0:
            return "Помилка: Квадратний корінь від від'ємного числа"
        self.result = math.sqrt(x)
        return self.result

    def modulus(self, x, y):
        try:
            self.result = x % y
            return self.result
        except ZeroDivisionError:
            return "Помилка: Неможливо обчислити залишок від ділення на нуль"
        except Exception as e:
            return f"Помилка: {str(e)}"

    def get_user_input(self):
        x = float(input("Введіть перше число: "))
        operator = input("Введіть операцію (+, -, *, /, ^, √, %): ")

        if operator in ['+', '-', '*', '/', '^', '√', '%']:
            if operator in ['+', '-', '*', '/', '^', '%']:
                y = float(input("Введіть друге число: "))
                return x, operator, y
            else:
                return x, operator
        else:
            return "Помилка: Недійсний оператор"

    def perform_calculation(self, x, operator, y=None):
        if operator == '+':
            return self.add(x, y)
        elif operator == '-':
            return self.subtract(x, y)
        elif operator == '*':
            return self.multiply(x, y)
        elif operator == '/':
            return self.divide(x, y)
        elif operator == '^':
            return self.power(x, y)
        elif operator == '√':
            return self.square_root(x)
        elif operator == '%':
            return self.modulus(x, y)
        else:
            return "Помилка: Недійсний оператор"

    def run_calculator(self):
        print("Ласкаво просимо до калькулятора!")
        while True:
            user_input = self.get_user_input()

            if isinstance(user_input, tuple):
                x, operator, y = user_input
                result = self.perform_calculation(x, operator, y)
                print(f"Результат: {x} {operator} {y} = {result}")
            else:
                print(user_input)

            another_calculation = input("Бажаєте виконати ще одне обчислення? (так/ні): ")
            if another_calculation.lower() != 'так':
                break


calc = Calculator()
calc.run_calculator()
