import pygame as pg

# Цвета
LIGHT_BLUE = (127, 79, 194)
YELLOW = (240, 221, 1)
TEXT_COLOR = (0, 0, 0)

# Размеры
MAX_WIDTH, MAX_HEIGHT = 500, 500
RECT_WIDTH, RECT_HEIGHT = 100, 150

# Позиции
RECT_POS_X, RECT_POS_Y = 20, (MAX_HEIGHT // 2) - 75
FONT_POS_Y = RECT_POS_Y + (RECT_HEIGHT // 3)

#Кол-во прямоугольников
RECT_COUNT = 4

#Настройки шрифта
SIZE_FONT = 30

class Area(pg.Rect):
    def __init__(self, x = RECT_POS_X, y = RECT_POS_Y, width = RECT_WIDTH, height = RECT_HEIGHT):
        self = super().__init__(x, y, width, height)

class Font(Area):
    def __init__():
        ...

if __name__ == '__main__':
    pg.init()

    # Настройки счетчика кадров
    clock = pg.time.Clock()
    clock.tick(40)

    # Создание окна
    window = pg.display.set_mode(size=(MAX_WIDTH, MAX_HEIGHT))
    window.fill(color=LIGHT_BLUE)

    # Создание прямоугольника
    rects = list()
    for i in range(1, RECT_COUNT+1):
        rects.append(Area(x=RECT_WIDTH*(i-1) + RECT_POS_X*i))

    # Настройки шрифта
    main_font = pg.font.SysFont('times new roman', SIZE_FONT)
    caption = main_font.render('Попал', True, TEXT_COLOR, None)

    # Игровой цикл
    isRunning = True

    while isRunning:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                isRunning = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    isRunning = False

        # Отрисовка элементов
        
        for i in range(1, RECT_COUNT+1):
            pg.draw.rect(window, YELLOW, rects[i-1])
            window.blit(source=caption, dest=(
                (RECT_WIDTH*(i-1) + RECT_POS_X*i) + 10,
                FONT_POS_Y))

        pg.display.update()