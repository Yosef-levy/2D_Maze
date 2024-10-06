import matplotlib.pyplot as plt
import keyboard
import time

from auto_search import AutoSearch
from board import Board
from movement import Movement


board = Board()
board.init()
plt.figure().canvas.mpl_connect('close_event', exit)
fig = plt.imshow(board.im[0:board.view_size, 0:board.view_size])
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.show(block=False)


def refresh():
    if not board.update():
        return
    if board.is_finish_pos():
        fig.set_data(board.im)
        time.sleep(3)
        board.init()
    corner = (min(max(0, board.snake_pos[0] - int(board.view_size/2)), board.size - board.view_size),
              min(max(0, board.snake_pos[1] - int(board.view_size/2)), board.size - board.view_size))
    fig.set_data(board.im[corner[0]:corner[0] + board.view_size, corner[1]:corner[1] + board.view_size])


def map():
    fig.set_data(board.im)
    time.sleep(3)
    refresh()

move = Movement(board, refresh)
auto_search = AutoSearch(board, move)


def clear():
    board.clear()
    time.sleep(0.05)
    refresh()


def init_pressed():
    board.init()
    refresh()


keyboard.add_hotkey('down', move.Down)
keyboard.add_hotkey('up', move.Up)
keyboard.add_hotkey('right', move.Right)
keyboard.add_hotkey('left', move.Left)
keyboard.add_hotkey('i', init_pressed)
keyboard.add_hotkey('c', clear)
keyboard.add_hotkey('a', auto_search.auto)
keyboard.add_hotkey('m', map)


try:
    while True:
        plt.pause(0.03)
except:
    pass
finally:
    auto_search.stop_thread = True
    # if auto_search:
    #     next_move()
    # refresh()
