import time
from threading import Thread


class AutoSearch:
    def __init__(self, board, move):
        self.board = board
        self.move = move
        self.direction = 2
        self.stop_thread = False
        self.auto_search = False
        thread = Thread(target=self.auto_search_thread)
        thread.start()

    def auto(self):
        self.auto_search = not self.auto_search

    def auto_search_thread(self):
        while True:
            if self.stop_thread:
                return
            if self.auto_search:
                self.next_move()
            time.sleep(0.0001)

    def move_in_direction(self):
        if self.direction == 0:
            self.move.Up()
        if self.direction == 1:
            self.move.Right()
        if self.direction == 2:
            self.move.Down()
        if self.direction == 3:
            self.move.Left()

    def next_move(self):
        if self.board.is_clear((self.direction + 1) % 4):
            self.direction = (self.direction + 1) % 4
        elif self.board.is_clear(self.direction):
            pass
        elif self.board.is_clear((self.direction - 1) % 4):
            self.direction = (self.direction - 1) % 4
        elif self.board.is_clear((self.direction - 2) % 4):
            self.direction = (self.direction - 2) % 4
        self.move_in_direction()
