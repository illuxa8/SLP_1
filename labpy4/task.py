import art
from termcolor import colored

def generate_ascii_art(user_input, width, height, alignment, art_style, color):
    try:
        # Створіть ASCII-арт на основі введення, стилю та кольору
        ascii_art = art.text2art(user_input, font=art_style)

        # Розділіть ASCII-арт на рядки
        lines = ascii_art.splitlines()
        
        # Визначте розмір ASCII-арту
        ascii_height = len(lines)
        ascii_width = max(len(line) for line in lines)

        # Підготовка до вирівнювання
        aligned_ascii = []
        for line in lines:
            if alignment == 'left':
                aligned_line = line.ljust(width)
            elif alignment == 'center':
                aligned_line = line.center(width)
            elif alignment == 'right':
                aligned_line = line.rjust(width)
            aligned_ascii.append(aligned_line)

        # Визначте розмір фінального ASCII-арту
        final_ascii = '\n'.join(aligned_ascii[:height])

        # Застосуйте кольори до ASCII-арту
        if color == 'чорно-білий':
            colored_ascii = final_ascii
        elif color == 'відтінки сірого':
            colored_ascii = colored(final_ascii, 'grey')
        else:
            colored_ascii = final_ascii  # За замовчуванням, без кольору

        return colored_ascii
    except Exception as e:
        return "Помилка при створенні ASCII-арту: " + str(e)

def save_ascii_art_to_file(ascii_art, filename):
    try:
        with open(filename, 'w') as file:
            file.write(ascii_art)
        print(f"ASCII-арт збережено у файлі '{filename}'")
    except Exception as e:
        print(f"Помилка при збереженні ASCII-арту: {e}")

def preview_ascii_art(ascii_art):
    print("\nПопередній перегляд ASCII-арту:")
    print(ascii_art)
    print("\n")

# Головна функція для введення та операцій
def create_ascii_art():
    while True:
        # Запитайте користувача про слово або фразу
        user_input = input("Введіть слово або фразу: ")

        # Запитайте у користувача розмір ASCII-арту
        while True:
            try:
                width = int(input("Введіть ширину ASCII-арту (1-100): "))
                if 1 <= width <= 100:
                    break
                else:
                    print("Ширина повинна бути в межах від 1 до 100.")
            except ValueError:
                print("Будь ласка, введіть ціле число для ширини.")

        while True:
            try:
                height = int(input("Введіть висоту ASCII-арту (1-100): "))
                if 1 <= height <= 100:
                    break
                else:
                    print("Висота повинна бути в межах від 1 до 100.")
            except ValueError:
                print("Будь ласка, введіть ціле число для висоти.")

        # Запитайте користувача про опцію вирівнювання
        alignment = input("Виберіть вирівнювання (left, center, right): ")

        # Запитайте користувача про стиль ASCII-арту
        art_style = input("Виберіть стиль ASCII-арту: ")

        # Запитайте користувача про опцію кольору
        color = input("Виберіть кольори (чорно-білий, відтінки сірого): ").strip().lower()

        # Генеруйте ASCII-арт
        result = generate_ascii_art(user_input, width, height, alignment, art_style, color)

        # Попередній перегляд ASCII-арту
        preview_ascii_art(result)

        # Запитайте користувача, чи він задоволений результатом перед збереженням
        if input("Задоволені результатом? (Так/Ні): ").strip().lower() == 'так':
            # Запитайте користувача, чи він бажає зберегти ASCII-арт у файл
            save_to_file = input("Бажаєте зберегти ASCII-арт у файл? (Так/Ні): ").strip().lower()
            if save_to_file == 'так':
                filename = input("Введіть ім'я файлу для збереження (наприклад, 'ascii_art.txt'): ")
                save_ascii_art_to_file(result, filename)
            break

create_ascii_art()
