import random
import curses

def draw_box(win, row, col, char):
    win.addch(row, col, char)
    win.addch(row, col + 1, char)
    win.addch(row + 1, col, char)
    win.addch(row + 1, col + 1, char)

def draw_tetromino(win, tetromino, offset, char):
    for pos in tetromino:
        draw_box(win, pos[0] + offset[0], pos[1] + offset[1], char)

def rotate_tetromino(tetromino):
    return [(y, -x) for x, y in tetromino]

def move_tetromino(tetromino, offset):
    return [(y + offset[0], x + offset[1]) for x, y in tetromino]

def check_collision(board, tetromino, offset):
    for pos in tetromino:
        row, col = pos[0] + offset[0], pos[1] + offset[1]
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != ' ':
            return True
    return False

def merge_tetromino(board, tetromino, offset):
    for pos in tetromino:
        row, col = pos[0] + offset[0], pos[1] + offset[1]
        board[row][col] = '[ ]'

def clear_lines(board):
    lines_to_clear = [i for i, row in enumerate(board) if ' ' not in row]
    for line in reversed(lines_to_clear):
        del board[line]
        board.insert(0, [' '] * len(board[0]))

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    height, width = stdscr.getmaxyx()
    board = [[' '] * width for _ in range(height)]

    tetrominos = [
        [(0, 0), (0, 1), (1, 0), (1, 1)],  # Square
        [(0, 0), (1, 0), (2, 0), (3, 0)],  # Line
        [(0, 0), (1, 0), (1, 1), (1, 2)],  # L
        [(0, 2), (1, 0), (1, 1), (1, 2)],  # Reverse L
        [(0, 1), (0, 2), (1, 0), (1, 1)],  # S
        [(0, 0), (0, 1), (1, 1), (1, 2)],  # Reverse S
        [(0, 1), (1, 0), (1, 1), (1, 2)]   # T
    ]

    tetromino = random.choice(tetrominos)
    tetromino_offset = [0, width // 2 - 2]

    while True:
        stdscr.clear()

        if check_collision(board, tetromino, tetromino_offset):
            merge_tetromino(board, tetromino, tetromino_offset)
            clear_lines(board)
            tetromino = random.choice(tetrominos)
            tetromino_offset = [0, width // 2 - 2]

        draw_tetromino(stdscr, tetromino, tetromino_offset, '[ ]')

        for row in range(height):
            for col in range(width):
                stdscr.addch(row, col * 2, board[row][col])

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == curses.KEY_LEFT and not check_collision(board, tetromino, [0, -1]):
            tetromino_offset[1] -= 1
        elif key == curses.KEY_RIGHT and not check_collision(board, tetromino, [0, 1]):
            tetromino_offset[1] += 1
        elif key == curses.KEY_DOWN and not check_collision(board, tetromino, [1, 0]):
            tetromino_offset[0] += 1
        elif key == ord('r'):
            rotated_tetromino = rotate_tetromino(tetromino)
            if not check_collision(board, rotated_tetromino, tetromino_offset):
                tetromino = rotated_tetromino

if __name__ == "__main__":
    curses.wrapper(main)
