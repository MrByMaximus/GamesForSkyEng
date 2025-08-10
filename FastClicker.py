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

    # Счетчик игры
    points: int = 0

    # Таймер игры
    timer: int = 5

    # Настройки шрифта
    # main_font = Font()
    main_font = pg.font.SysFont('times new roman', SIZE_FONT)
    other_font = pg.font.Font(None, SIZE_FONT+10)
    
    catch_text = main_font.render('Попал', True, TEXT_COLOR, None)
    click_text = other_font.render('CLICK', True, TEXT_COLOR, None)

    timer_text = main_font.render('Таймер:', True, TEXT_COLOR, None)
    points_text = main_font.render('Счёт:', True, TEXT_COLOR, None)

    timer_value_text = main_font.render(str(timer), True, TEXT_COLOR, None)
    points_value_text = main_font.render(str(points), True, TEXT_COLOR, None)

    # Игровой цикл
    isRunning = True
    isGameOver = False
    isClicked: bool | None = None

    # Последний зафиксированный тик (в мс)
    last_ticks: int = pg.time.get_ticks()

    # Номер прямоугольника, где появляется надпись
    num: int = 1

    # Текущий текст отрисовки
    text: pg.Surface = click_text

    # Номер прямоугольника, по которому кликнули
    card_clicked: int = 1

    while isRunning:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                isRunning = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    isRunning = False
            # Проверка нажатия левой кнопки мыши
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and not isGameOver:
                x, y = event.pos
                # Проверка, что нажали на прямоугольник
                for i in range(1, RECT_COUNT+1):
                    if rects[i-1].collidepoint(x, y):
                        if i == num: # Попали
                            isClicked = True
                            text = catch_text
                            points += 1
                        else: # Промазали
                            isClicked = False
                            points -= 1
                            if points < 0:
                                points = 0

                        # Очистка экрана
                        window.fill(LIGHT_BLUE)
                        
                        # Изменение текста счетчика
                        points_value_text = main_font.render(str(points), True, TEXT_COLOR, None)
                        card_clicked = i

                        break

        # Отрисовка прямоугольников
        for i in range(1, RECT_COUNT+1):
            color = YELLOW
            if i == card_clicked and isClicked != None:
                if isClicked == True:
                    color = GREEN
                elif isClicked == False:
                    color = RED
            
            pg.draw.rect(window, color, rects[i-1].rect)

        # Отрисовка текста
        window.blit(source=text, dest=(
            (RECT_WIDTH*(num-1) + RECT_POS_X*num) + 10,
            FONT_POS_Y))
        window.blit(timer_text, (20, 15))
        window.blit(points_text, (MAX_WIDTH-100, 15))
        window.blit(timer_value_text, (50, 45))
        window.blit(points_value_text, (MAX_WIDTH-75, 45))

        # Проверка что прошла секунда
        now_ticks = pg.time.get_ticks()
        if now_ticks - last_ticks >= DELAY and not isGameOver:
            num = randint(1, RECT_COUNT)
            last_ticks = now_ticks

            if isClicked != None:
                isClicked = None
                text = click_text
            
            # Очистка экрана
            window.fill(LIGHT_BLUE)

            # Изменение таймера
            timer -= 1
            timer_value_text = main_font.render(str(timer), True, TEXT_COLOR, None)

            if timer <= 0:
                isGameOver = True

        pg.display.update()

if __name__ == '__main__':
    main()