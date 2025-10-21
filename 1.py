import turtle
import math
import time


def translate_color(color_ru):
    """Перевод русских названий цветов на английские для turtle"""
    color_map = {
        'красный': 'red',
        'оранжевый': 'orange',
        'желтый': 'yellow',
        'зеленый': 'green',
        'синий': 'blue',
        'фиолетовый': 'purple',
        'розовый': 'pink',
        'черный': 'black',
        'серый': 'gray',
        'белый': 'white'
    }
    return color_map.get(color_ru.lower(), 'black')  # по умолчанию черный


def draw_hexagon(x: float, y: float, side_len: float, color: str):
    """Отрисовка одного шестиугольника с заливкой"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Преобразуем цвет в английский
    english_color = translate_color(color)
    turtle.fillcolor(english_color)
    turtle.begin_fill()

    # Поворачиваем для правильной ориентации шестиугольника
    turtle.setheading(30)
    for _ in range(6):
        turtle.forward(side_len)
        turtle.right(60)

    turtle.end_fill()
    turtle.setheading(0)  # Возвращаем ориентацию


def draw_hexagon_border(x: float, y: float, side_len: float):
    """Отрисовка границы шестиугольника"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Устанавливаем цвет и толщину границы
    turtle.pencolor("black")
    turtle.pensize(2)

    # Рисуем границу
    turtle.setheading(30)
    for _ in range(6):
        turtle.forward(side_len)
        turtle.right(60)

    turtle.setheading(0)
    turtle.pensize(1)  # Возвращаем стандартную толщину


def animate_drawing(centers: list, colors: list, side: float):
    """Анимированное рисование узора"""
    turtle.tracer(0, 0)  # Отключаем автоматическое обновление для плавной анимации

    for i, (center, color) in enumerate(zip(centers, colors)):
        x, y = center

        # Рисуем шестиугольник с заливкой
        draw_hexagon(x, y, side, color)

        # Добавляем границу
        draw_hexagon_border(x, y, side)

        # Обновляем экран после каждого шестиугольника для анимации
        turtle.update()

        # Небольшая задержка для визуализации процесса рисования
        time.sleep(0.05)

    turtle.tracer(1, 10)  # Включаем обратно автоматическое обновление


def get_num_hexagons():
    while True:
        input_str = input("Введите количество шестиугольников, располагаемых в ряд: ").strip()
        if input_str.isdigit():
            num = int(input_str)
            if 4 <= num <= 20:
                return num
        print("Пожалуйста, введите число от 4 до 20.")


def get_color_choice(prompt):
    available_colors = ['красный', 'оранжевый', 'желтый', 'зеленый',
                        'синий', 'фиолетовый', 'розовый', 'черный',
                        'серый', 'белый']

    print('Доступные цвета: красный, оранжевый, желтый, '
          'зеленый, синий, фиолетовый, розовый, черный, серый, белый')

    while True:
        color = input(prompt).strip().lower()
        if color in available_colors:
            return color
        print('Ошибка ввода цвета. Пожалуйста, повторите попытку.')


def main():
    # Настройка окна turtle
    turtle.setup(800, 800)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")

    # Получаем параметры от пользователя
    N = get_num_hexagons()
    color_first = get_color_choice('Выберите первый цвет из предложенных выше: ')
    color_second = get_color_choice('Выберите второй цвет из предложенных выше: ')

    # Вычисляем размеры
    size = 500  # Уменьшил размер для лучшего отображения
    side_length = size / (N * 1.5)
    diagonal = math.sqrt(3) * side_length

    # Вычисляем начальное положение
    start_x_0 = -diagonal * N / 2
    start_y_0 = side_length * (N / 2)

    # Собираем центры и цвета для анимации
    centers = []
    colors = []

    for row in range(N):
        y_offset = start_y_0 - row * side_length * 1.5
        if row % 2 == 0:
            x_offset = start_x_0
        else:
            x_offset = start_x_0 + diagonal / 2

        color = color_first if row % 2 == 0 else color_second

        for col in range(N):
            x = x_offset + col * diagonal
            y = y_offset
            centers.append((x, y))
            colors.append(color)

    # Запускаем анимированное рисование
    animate_drawing(centers, colors, side_length)

    # Сообщение о завершении
    turtle.penup()
    turtle.goto(0, -size / 2 - 30)
    turtle.color("black")

    turtle.done()


if __name__ == "__main__":
    main()
