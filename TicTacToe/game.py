# Импортируем необходимые модули и библиотеки
import random
import tkinter
from tkinter import messagebox

# Объявляем глобальные переменные
CELL_SIZE = 50
FIELD_SIZE = 10
WIDTH = 500
HEIGHT = 503
GEOM = f'{WIDTH}x{HEIGHT}'

# Создаём окошко в котором будет отрисовываться сама игра
root = tkinter.Tk()
# Размеры окна
root.geometry(GEOM)
# Название в title
root.title("Игра 'Обратные крестики-нолики!'")
# Запрещаем менять размеры окна
root.resizable(width=False, height=False)


# Создаём главную функцию main
def main():
    window = Window(root)
    window.grid()
    game = Game()

    # Создаём функцию определения координат клика
    def position(event):
        x = event.x
        y = event.y
        # Если человечек тыкнул в пустое поле, то ход переходит к компьютеру
        if game.click_position(x, y, window):
            game.computer_move(window)

    # Определяем клик левой кнопкой мыши
    root.bind("<Button-1>", position)
    # Запускаем цикл обработки событий
    root.mainloop()


# Создаём класс в котором будет работа с графикой
class Window:
    # Создаём поле/холст в окне белым цветом
    def __init__(self, root):
        self.game_window = tkinter.Canvas(root, width=WIDTH, height=WIDTH, bg='white')
        self.game_window.pack()

    # Создаём сетку, сначала внешние линии, потом внутренние
    def grid(self):
        self.game_window.create_rectangle(2, 2, WIDTH - 3, WIDTH)
        for i in range(FIELD_SIZE):
            self.game_window.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, WIDTH)
            self.game_window.create_line(0, i * CELL_SIZE, HEIGHT, i * CELL_SIZE)

    # Рисуем крестик
    def draw_x(self, x, y, color):
        self.game_window.create_line(CELL_SIZE * x, CELL_SIZE * y, CELL_SIZE * x + CELL_SIZE,
                                     CELL_SIZE * y + CELL_SIZE, width=5, fill=color)
        self.game_window.create_line(CELL_SIZE * x + CELL_SIZE, CELL_SIZE * y, CELL_SIZE * x,
                                     CELL_SIZE * y + CELL_SIZE, width=5, fill=color)

    # Рисуем нолик
    def draw_o(self, x, y, color):
        self.game_window.create_oval(CELL_SIZE * x, CELL_SIZE * y, CELL_SIZE * x + CELL_SIZE,
                                     CELL_SIZE * y + CELL_SIZE, width=5, outline=color)


# Создаём класс в котором будет логика игры
class Game:
    def __init__(self):
        # Создаём массив и заполняем его отрезками под клетки нашего поля
        self.grid_field = [[i * CELL_SIZE, (i + 1) * CELL_SIZE] for i in range(FIELD_SIZE)]
        # Создаём массив и заполняем его нулями - это будет наше поле
        self.dot_field = [[0 for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]

    # Создаём функцию проверки победы(горизонт, вертикаль и две диагонали)
    def check_win(self, color):
        for i in range(FIELD_SIZE):
            for j in range(FIELD_SIZE - 4):
                if self.dot_field[i][j] == self.dot_field[i][j + 1] == self.dot_field[i][j + 2] == \
                        self.dot_field[i][j + 3] == self.dot_field[i][j + 4] != 0:
                    # Если обнаружили пять в ряд одного типа, то вызываем мессежбокс
                    # в котором пишем кто проиграл и закрываем игру
                    messagebox.showinfo("GAME OVER", "Человечек lose!" if color == 'blue' else "Компутер lose!")
                    root.destroy()
        for i in range(FIELD_SIZE - 4):
            for j in range(FIELD_SIZE):
                if self.dot_field[i][j] == self.dot_field[i + 1][j] == self.dot_field[i + 2][j] == \
                        self.dot_field[i + 3][j] == self.dot_field[i + 4][j] != 0:
                    messagebox.showinfo("GAME OVER", "Человечек lose!" if color == 'blue' else "Компутер lose!")
                    root.destroy()
        for i in range(FIELD_SIZE - 4):
            for j in range(FIELD_SIZE - 4):
                if self.dot_field[i][j] == self.dot_field[i + 1][j + 1] == self.dot_field[i + 2][j + 2] == \
                        self.dot_field[i + 3][j + 3] == self.dot_field[i + 4][j + 4] != 0:
                    messagebox.showinfo("GAME OVER", "Человечек lose!" if color == 'blue' else "Компутер lose!")
                    root.destroy()
        for i in range(FIELD_SIZE - 4):
            for j in range(4, FIELD_SIZE):
                if self.dot_field[i][j] == self.dot_field[i + 1][j - 1] == self.dot_field[i + 2][j - 2] == \
                        self.dot_field[i + 3][j - 3] == self.dot_field[i + 4][j - 4] != 0:
                    messagebox.showinfo("GAME OVER", "Человечек lose!" if color == 'blue' else "Компутер lose!")
                    root.destroy()

    # Создаём функцию для хода компутера
    def computer_move(self, window):
        y = random.randint(0, 9)
        x = random.randint(0, 9)
        # Рандомно подставляем координаты и проверяем клетку, если она пуста(==0),
        # то ставим 2, выбираем красный цвет, рисуем О, проверяем на победу, иначе повторяем
        if self.dot_field[y][x] == 0:
            self.dot_field[y][x] = 2
            color = 'red'
            window.draw_o(x, y, color)
            self.check_win(color)
        else:
            return self.computer_move(window)

    # Создаём функцию для хода человечека
    def click_position(self, x, y, window):
        # Определяем какой клетке(х, у) принадлежат координаты клика
        for i in range(FIELD_SIZE):
            if self.grid_field[i][0] <= x <= self.grid_field[i][1]:
                x = i
            if self.grid_field[i][0] <= y <= self.grid_field[i][1]:
                y = i
        # Проверяем клетку после клика, если она пуста(==0),то ставим 1, выбираем синий цвет,
        # рисуем Х, проверяем на победу, возвращаем Тру, иначе Фолс
        if self.dot_field[y][x] == 0:
            self.dot_field[y][x] = 1
            color = 'blue'
            window.draw_x(x, y, color)
            self.check_win(color)
            return True
        else:
            return False


if __name__ == "__main__":
    main()
