import time


class Movement:
    def __init__(self, board, refresh):
        self.board = board
        self.refresh = refresh

    def move(self, y, x):
        for _ in range(self.board.cell_size):
            self.board.move_snake(y, x)
            self.refresh()
            time.sleep(0.05)

    def Down(self):
        self.move(1, 0)

    def Up(self):
        self.move(-1, 0)

    def Right(self):
        self.move(0, 1)

    def Left(self):
        self.move(0, -1)
