import random
import tkinter
from tkinter import messagebox

CELL_SIZE = 50
FIELD_SIZE = 10
WIDTH = 500
HEIGHT = 500
GEOM = f'{WIDTH}x{HEIGHT}'


def main():
    root = tkinter.Tk()
    root.geometry(GEOM)
    root.title("Игра 'Пять в ряд, наоборот!'")
    root.resizable(width=False, height=False)
    window = Window(root)
    window.grid()
    game = Game()

    def position(event):
        x = event.x
        y = event.y
        if game.click_position(x, y, window):
            game.computer_move(window)

    root.bind("<Button-1>", position)
    root.mainloop()


class Window:
    def __init__(self, root):
        self.game_window = tkinter.Canvas(root, width=WIDTH, height=WIDTH, bg='white')
        self.game_window.pack()

    def grid(self):
        self.game_window.create_rectangle(2, 2, WIDTH - 3, WIDTH)
        for i in range(FIELD_SIZE):
            self.game_window.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, WIDTH)
            self.game_window.create_line(0, i * CELL_SIZE, HEIGHT, i * CELL_SIZE)

    def draw_square(self, x, y, color):
        self.game_window.create_rectangle(CELL_SIZE * x, CELL_SIZE * y,
                                          CELL_SIZE * x + CELL_SIZE, CELL_SIZE * y + CELL_SIZE, fill=color)


class Game:
    def __init__(self):
        self.grid_field = [[i * CELL_SIZE, (i + 1) * CELL_SIZE] for i in range(FIELD_SIZE)]
        self.dot_field = [[0 for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]
        self.player = 1

    def check_win(self, window, color):
        for i in range(FIELD_SIZE):
            for j in range(FIELD_SIZE - 4):
                if self.dot_field[i][j] == self.dot_field[i][j + 1] == self.dot_field[i][j + 2] == \
                        self.dot_field[i][j + 3] == self.dot_field[i][j + 4] != 0:
                    messagebox.showinfo("ПОБЕДА!!!", f"{color} win!")
                    break
        for i in range(FIELD_SIZE - 4):
            for j in range(FIELD_SIZE):
                if self.dot_field[i][j] == self.dot_field[i + 1][j] == self.dot_field[i + 2][j] == \
                        self.dot_field[i + 3][j] == self.dot_field[i + 4][j] != 0:
                    messagebox.showinfo("ПОБЕДА!!!", f"{color} win!")
                    break
        for i in range(FIELD_SIZE - 4):
            for j in range(FIELD_SIZE - 4):
                if self.dot_field[i][j] == self.dot_field[i + 1][j + 1] == self.dot_field[i + 2][j + 2] == \
                        self.dot_field[i + 3][j + 3] == self.dot_field[i + 4][j + 4] != 0:
                    messagebox.showinfo("ПОБЕДА!!!", f"{color} win!")
                    break
        for i in range(FIELD_SIZE - 4):
            for j in range(5, FIELD_SIZE):
                if self.dot_field[i][j] == self.dot_field[i + 1][j - 1] == self.dot_field[i + 2][j - 2] == \
                        self.dot_field[i + 3][j - 3] == self.dot_field[i + 4][j - 4] != 0:
                    messagebox.showinfo("ПОБЕДА!!!", f"{color} win!")
                    break

    def computer_move(self, window):
        y = random.randint(0, 9)
        x = random.randint(0, 9)
        if self.dot_field[y][x] == 0:
            self.dot_field[y][x] = 2
            color = 'red'
            window.draw_square(x, y, color)
            self.check_win(window, color)
        else:
            return self.computer_move(window)

    def click_position(self, x, y, window):
        for i in range(FIELD_SIZE):
            if self.grid_field[i][0] <= x <= self.grid_field[i][1]:
                x = i
            if self.grid_field[i][0] <= y <= self.grid_field[i][1]:
                y = i
        if self.dot_field[y][x] == 0:
            self.dot_field[y][x] = 1
            color = 'blue'
            window.draw_square(x, y, color)
            self.check_win(window, color)
            return True
        else:
            return False


if __name__ == "__main__":
    main()
