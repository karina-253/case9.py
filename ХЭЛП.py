import turtle
import math
import time
import webcolors


def translate_color(color):
    """Перевод русских названий цветов на английские для turtle"""
    colors = {
        'красный': 'red',
        'оранжевый': 'orange',
        'желтый': 'yellow', 'жёлтый': 'yellow',
        'зеленый': 'green', 'зелёный': 'green',
        'синий': 'blue',
        'голубой': 'lightblue',
        'фиолетовый': 'purple',
        'розовый': 'pink',
        'черный': 'black', 'чёрный': 'black',
        'серый': 'gray',
        'коричневый': 'brown',
    }

    if color.lower() in colors.values() or color.startswith('#'):
        return color.lower()

    if color.lower() in colors:
        return colors[color.lower()]

    return color.lower()


def is_valid_color_name(color_name: str) -> bool:
    """Проверяет, существует ли цвет с таким названием в стандарте CSS"""
    try:
        webcolors.name_to_hex(color_name)
        return True
    except ValueError:
        return False


def get_color_choice(prompt: str):
    """Функция для выбора цвета с поддержкой русского, английского ввода и выбора по номеру"""

    print('\n' + '=' * 50)
    print('ДОСТУПНЫЕ ЦВЕТА:')

    available_colors = [
        (1, 'красный', '\U0001F48B'),
        (2, 'синий', '\U0001F499'),
        (3, 'зеленый', '\U0001F49A'),
        (4, 'желтый', '\U0001F49B'),
        (5, 'фиолетовый', '\U0001F49C'),
        (6, 'голубой', '\U0001F4A6'),
        (7, 'черный', '\U0001F5A4'),
        (8, 'серый', '\U0001F47D'),
        (9, 'розовый', '\U0001F495'),
        (10, 'оранжевый', '\U0001F9E1'),
        (11, 'коричневый', '\U0001F90E'),
        (12, 'Свой цвет (HEX) или название (на английском)', '\U0001F916')
        ]
    mid = len(available_colors) // 2
    available_colors_1 = available_colors[:mid]
    available_colors_2 = available_colors[mid:]

    max_width = max(len(color[1]) for color in available_colors_1) + 3

    print(" Выберите цвет по номеру или введите название:")
    print("-" * 50)

    for i in range(len(available_colors_1)):
        col1 = available_colors_1[i]
        col2 = available_colors_2[i] if i < len(available_colors_2) else None

        line = f"{col1[0]:>2}. {col1[2]} {col1[1]:<{max_width}}"
        if col2:
            line += f" {col2[0]:>2}. {col2[2]} {col2[1]}"
        print(line)

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Ошибка: введите номер или название цвета!\n")
            continue

        if user_input.isdigit():
            num = int(user_input)
            if 1 <= num <= len(available_colors):

                for color_num, ru_name, emoji in available_colors:
                    if color_num == num:
                        print(f"Выбран цвет: {emoji} {ru_name}")

                        if num == 12:
                            custom_color = input("Введите свой цвет (HEX или английское название): ").strip()
                            if custom_color.startswith('#') or is_valid_color_name(translate_color(custom_color)):
                                return translate_color(custom_color)
                            else:
                                print(" Неверный цвет! Попробуйте снова.\n")
                                continue
                        return translate_color(ru_name)
            else:
                print(f" Ошибка: номер должен быть от 1 до {len(available_colors)}!\n")
                continue

        if user_input.startswith('#'):
            if len(user_input) == 7 and all(c in '0123456789ABCDEFabcdef' for c in user_input[1:]):
                return user_input
            else:
                print("Ошибка: неверный формат HEX-кода! Используйте #RRGGBB\n")
                continue

        english_color = translate_color(user_input)

        if is_valid_color_name(english_color):
            print(f" Выбран цвет: {english_color}")
            return english_color
        else:
            print(f" Ошибка: цвета '{user_input}' нет в списке")


def get_num_hexagons() -> int:
    """Функция для ввода количества шестиугольников с валидацией"""
    while True:
        try:
            quantity = int(input('Введите количество шестиугольников '
                                 'в ряду (от 4 до 20): '))
            if 4 <= quantity <= 20:
                return quantity
            else:
                print('Число шестиугольников должно быть в '
                      'диапазоне от 4 до 20.')
        except ValueError:
            print('Пожалуйста, введите числовое значение от 4 до 20.')


def calculate_side_length(number, size):
    """Вычисление длины стороны шестиугольника для равномерного заполнения."""
    side = size / (number + 0.5)
    return side


def calculate_hexagon_centers(number, size):
    """Рассчет координат центров шестиугольников для центрирования и заполнения."""
    side = calculate_side_length(number, size)
    width_hexagon = math.sqrt(3) * side  # ширина по горизонтали

    total_width = width_hexagon * number
    total_height = side * 1.5 * number

    start_x = - total_width / 2 + width_hexagon / 2
    start_y = total_height / 2 - side / 2

    centers = []

    for row in range(number):
        y = start_y - row * side * 1.5
        for col in range(number):
            x = start_x + col * width_hexagon
            if row % 2 == 1:
                x += width_hexagon / 2  # смещение для нечетных строк
            centers.append((x, y))
    return centers, side


def border_thickness():
    thicknesses = ['тонкий', 'средний', 'толстый']
    size_thickness = {'тонкий': 1, 'средний': 3, 'толстый': 5}

    print('Варианты толщины границы: тонкий, средний, толстый')

    while True:
        thickness = input('Выберите толщину границы:').strip().lower()
        if thickness in thicknesses:
            return size_thickness[thickness]
        print('Ошибка ввода. Пожалуйста, выберите из предложенных вариантов.')


def border_color():
    color_options = ['красный', 'оранжевый', 'желтый', 'зеленый',
                        'синий', 'фиолетовый', 'розовый', 'черный',
                        'серый', 'белый']

    print('Варианты цветов для границы: красный, оранжевый, желтый, '
          'зеленый, синий, фиолетовый, розовый, черный, серый, белый')

    while True:
        color = input("Выберите цвет границы: ").strip().lower()
        if color in color_options:
            return translate_color(color)
        print('Ошибка ввода. Пожалуйста, выберите из предложенных вариантов')


def shadow_brightness():
    shadow_options = ['нет', 'слабый', 'средний', 'сильный']
    shadow_value = {'нет': 0, 'слабый': 5, 'средний': 8, 'сильный': 12}

    print("Варианты интенсивности теней: нет, слабый, средний, сильный")

    while True:
        shadow = input("Выберите интенсивность тени: ").strip().lower()
        if shadow in shadow_options:
            return shadow_value[shadow]
        print("Ошибка ввода. Пожалуйста, выберите из предложенных вариантов.")


def draw_shadow(x: float, y: float, side_len: float, shadow_intensity: int):
    """Отрисовка тени шестиугольника"""
    if shadow_intensity == 0:
        return

    shadow_x = x + shadow_intensity
    shadow_y = y - shadow_intensity

    turtle.penup()
    turtle.goto(shadow_x, shadow_y)
    turtle.pendown()

    turtle.fillcolor("#686868")
    turtle.begin_fill()

    turtle.penup()
    turtle.setheading(30)
    for _ in range(6):
        turtle.forward(side_len)
        turtle.right(60)
    turtle.pendown()

    turtle.end_fill()
    turtle.setheading(0)


def draw_hexagon(x: float, y: float, side_len: float, color: str):
    """Отрисовка одного шестиугольника с заливкой"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.setheading(30)
    for _ in range(6):
        turtle.forward(side_len)
        turtle.right(60)

    turtle.end_fill()
    turtle.setheading(0)


def draw_hexagon_border(x: float, y: float, side_len: float,
                        thickness_bord: int, color_bord: str):
    """Отрисовка границы шестиугольника"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.pencolor(color_bord)
    turtle.pensize(thickness_bord)

    turtle.setheading(30)
    for _ in range(6):
        turtle.forward(side_len)
        turtle.right(60)

    turtle.setheading(0)
    turtle.pensize(1)


def animate_drawing(centers: list, colors: list, side: float,
                    thickness_width: int, color_bord: str, shadow_intensity: int):
    """Анимированное рисование узора"""
    turtle.tracer(0, 0)

    for i in range(len(centers)):
        x, y = centers[i]
        color = colors[i]

        if shadow_intensity > 0:
            draw_shadow(x, y, side, shadow_intensity)

        draw_hexagon(x, y, side, color)
        draw_hexagon_border(x, y, side, thickness_width, color_bord)

        turtle.update()
        time.sleep(0.05)

    turtle.tracer(1, 10)


def main():
    print('=== Гексагональный арт-генератор ===\n')

    # Настройка окна turtle
    turtle.setup(800, 800)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")

    # Получаем параметры от пользователя
    N = get_num_hexagons()

    print("\n" + "=" * 50)
    print("ВЫБОР ЦВЕТОВ ДЛЯ УЗОРА:")

    color_first = get_color_choice('Выберите первый цвет: ')
    color_second = get_color_choice('Выберите второй цвет: ')

    thickness_width = border_thickness()
    color_bord = border_color()

    shadow_intensity = shadow_brightness()

    size = 500

    centers, side_length = calculate_hexagon_centers(N, size)

    colors = []
    for row in range(N):
        for col in range(N):
            color = color_first if (row + col) % 2 == 0 else color_second
            colors.append(color)

    animate_drawing(centers, colors, side_length, thickness_width,
                    color_bord, shadow_intensity)

    turtle.done()


if __name__ == "__main__":
    main()
