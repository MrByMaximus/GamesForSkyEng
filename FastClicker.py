import pygame as pg
from random import randint

pg.init()

# Цвета
LIGHT_BLUE = (127, 79, 194)
YELLOW = (240, 221, 1)
RED = (158, 0, 0)
GREEN = (114, 223, 0)
TEXT_COLOR = (0, 0, 0)

# Размеры
MAX_WIDTH, MAX_HEIGHT = 500, 500
RECT_WIDTH, RECT_HEIGHT = 100, 150

# Позиции
RECT_POS_X, RECT_POS_Y = 20, (MAX_HEIGHT // 2) - 75
FONT_POS_Y = RECT_POS_Y + (RECT_HEIGHT // 3)

# Кол-во прямоугольников
RECT_COUNT = 4

# Настройки шрифта
SIZE_FONT = 30

# Задержка
DELAY = 1000

class Area():
    def __init__(self, x = RECT_POS_X, y = RECT_POS_Y, width = RECT_WIDTH, height = RECT_HEIGHT):
        self.rect = pg.Rect(x, y, width, height)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

# class Font(pg.font.Font):
#     def __init__(self, name = 'times new roman', size = SIZE_FONT):
#         # self = pg.font.SysFont(name, size)
#         font = super().__init__(None, size)
#         self = font.render()

#     def render_text(self, text):
#         self.render(text, True, TEXT_COLOR, None)

def main():
    # Настройки счетчика кадров
    clock = pg.time.Clock()
    clock.tick(40)

    # Создание окна
    window = pg.display.set_mode(size=(MAX_WIDTH, MAX_HEIGHT))
    window.fill(color=LIGHT_BLUE)

    # Создание прямоугольника
    rects: list[Area] = list()
    for i in range(1, RECT_COUNT+1):
        rects.append(Area(x=RECT_WIDTH*(i-1) + RECT_POS_X*i))

    # Настройки шрифта
    # main_font = Font()
    main_font = pg.font.SysFont('times new roman', SIZE_FONT)
    other_font = pg.font.Font(None, SIZE_FONT+10)
    catch_text = main_font.render('Попал', True, TEXT_COLOR, None)
    click_text = other_font.render('CLICK', True, TEXT_COLOR, None)

    # Игровой цикл
    isRunning = True
    isClicked: bool | None = None

    last_ticks = pg.time.get_ticks()
    num = 1
    card_clicked = 1

    while isRunning:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                isRunning = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    isRunning = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                for i in range(1, RECT_COUNT+1):
                    if rects[i-1].collidepoint(x, y):
                        if i == num:
                            isClicked = True
                        else:
                            isClicked = False
                        card_clicked = i
                        break

        # Отрисовка прямоугольников
        for i in range(1, RECT_COUNT+1):
            color = YELLOW
            if i == card_clicked:
                if isClicked == True:
                    color = GREEN
                if isClicked == False:
                    color = RED
            
            pg.draw.rect(window, color, rects[i-1].rect)

        # Генерация текста в прямоугольнике
        now_ticks = pg.time.get_ticks()
        if now_ticks - last_ticks >= DELAY:
            num = randint(1, RECT_COUNT)
            last_ticks = now_ticks
            if isClicked != None:
                isClicked = None
        
        # Отрисовка текста
        window.blit(source=click_text, dest=(
            (RECT_WIDTH*(num-1) + RECT_POS_X*num) + 10,
            FONT_POS_Y))

        pg.display.update()

if __name__ == '__main__':
    main()