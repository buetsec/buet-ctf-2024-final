#!/usr/local/bin/python

import socket
import string
import threading
import time


class Maze:
    def __init__(self):
        self.grid = [
            ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
            ['W',' ','W',' ',' ',' ','W',' ','W',' ','W',' ','W',' ','W',' ',' ',' ','W',' ',' ',' ','W',' ',' ',' ','W',' ',' ',' ','W',' ','W',' ',' ',' ',' ',' ',' ','W'],
            ['W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W','W'],
            ['W',' ',' ',' ','W',' ','W',' ',' ',' ','W',' ','W',' ',' ',' ','W',' ',' ',' ',' ',' ','W',' ',' ',' ',' ',' ',' ',' ',' ',' ','W',' ',' ',' ','W',' ','W','W'],
            ['W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W','W'],
            ['W',' ',' ',' ','W',' ','W',' ',' ',' ','W',' ',' ',' ',' ',' ','W',' ','W',' ',' ',' ',' ',' ',' ',' ','W',' ','W',' ',' ',' ',' ',' ','W',' ','W',' ',' ','W'],
            ['W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W','W'],
            ['W',' ',' ',' ','W',' ','W',' ',' ',' ','W',' ',' ',' ',' ',' ','W',' ',' ',' ',' ',' ',' ',' ','W',' ','W',' ',' ',' ','W',' ','W',' ',' ',' ','W',' ',' ','W'],
            ['W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W','W'],
            ['W',' ',' ',' ',' ',' ','W',' ','W',' ','W',' ','W',' ','W',' ',' ',' ',' ',' ','W',' ','W',' ','W',' ','W',' ','W',' ',' ',' ','W',' ','W',' ',' ',' ',' ','W'],
            ['W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W','W'],
            ['W',' ','W',' ','W',' ','W',' ',' ',' ','W',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','W',' ',' ',' ',' ',' ','W',' ','W',' ',' ',' ','W',' ',' ',' ',' ','W'],
            ['W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W','W'],
            ['W',' ',' ',' ','W',' ',' ',' ',' ',' ',' ',' ','W',' ',' ',' ',' ',' ','W',' ',' ',' ',' ',' ',' ',' ','W',' ','W',' ',' ',' ','W',' ',' ',' ','W',' ','W','W'],
            ['W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W','W'],
            ['W',' ','W',' ','W',' ',' ',' ','W',' ',' ',' ',' ',' ','W',' ',' ',' ','W',' ',' ',' ','W',' ',' ',' ','W',' ','W',' ','W',' ',' ',' ',' ',' ','W',' ',' ','W'],
            ['W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W','W'],
            ['W',' ','W',' ',' ',' ','W',' ','W',' ',' ',' ','W',' ','W',' ','W',' ',' ',' ','W',' ','W',' ','W',' ',' ',' ','W',' ','W',' ',' ',' ',' ',' ','W',' ',' ','W'],
            ['W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','W',' ','E','W'],
            ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W']
        ]
        self.player_pos = (1, 1)
        self.exit_pos = (18, 38)
        self.grid[self.player_pos[0]][self.player_pos[1]] = '+'
        self.grid[self.exit_pos[0]][self.exit_pos[1]] = 'E'

    def print_maze(self):
        return '\n'.join([''.join(row) for row in self.grid])

    def move_player(self, direction):
        x, y = self.player_pos
        if direction == 'U':
            new_pos = (x - 1, y)
        elif direction == 'D':
            new_pos = (x + 1, y)
        elif direction == 'R':
            new_pos = (x, y + 1)
        elif direction == 'L':
            new_pos = (x, y - 1)
        else:
            return False, False

        if self.is_valid_move(new_pos):
            self.grid[x][y] = ' '
            self.player_pos = new_pos
            self.grid[new_pos[0]][new_pos[1]] = '+'
            return True, self.check_exit()
        return False, False

    def is_valid_move(self, pos):
        x, y = pos
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] != 'W'

    def check_exit(self):
        return self.player_pos == self.exit_pos



def flag(team_code):
    key1 = "5F7D9YB4Q3H5Z4V9A3Q2XZLW9MBH5N8R"
    key2 = "3N5X8ACB2ZJ4M2W5F7Q9Y6PL0RTQ7E1S"

    result = list(team_code)
    for i in range(len(team_code)):

        xored_char = ord(team_code[i]) ^ ord(key1[i % len(key1)]) ^ ord(key2[i % len(key2)])


        if chr(xored_char) in string.ascii_letters + string.digits:
            result[i] = chr(xored_char)
        else:

            if xored_char < ord('0'):
                result[i] = chr(ord('0') + (abs(xored_char) % 10))  # 0-9
            elif xored_char < ord('A'):
                result[i] = chr(ord('A') + (abs(xored_char) % 26))  # A-Z
            elif xored_char < ord('a'):
                result[i] = chr(ord('A') + (abs(xored_char) % 26))  # A-Z
            elif xored_char < ord('0') + 10:
                result[i] = chr(ord('0') + (abs(xored_char) % 10))  # 0-9
            elif xored_char < ord('A') + 26:
                result[i] = chr(ord('A') + (abs(xored_char) % 26))  # A-Z
            else:
                result[i] = chr(ord('a') + (abs(xored_char) % 26))  # a-z


    return ''.join(result)




def main():
    print("Enter your team code: ", end="")
    team_code = input().strip()

    maze = Maze()
    print(f"\nWelcome to the Maze!\nEscape the maze to get the flag!\n\n(W) represents wall.\n(+) represents your location.\n(E) represents Exit.\n\nYou have 30 seconds to escape!\nHurry up!\n\n{maze.print_maze()}")

    while True:
        print("\nEnter your move (U/D/R/L): ", end="")
        move = input().strip().upper()
        success, escaped = maze.move_player(move)
        if success:
            if escaped:
                print("\nCongratulations! You've escaped the maze!\n")
                print(f"BUETCTF{{G00D_Work!_Y0u_35c4p3d_Th3_Maz3_Amazingly_{flag(team_code)}}}")
                break
            else:
                print("\nMoved successfully!\n")
                print(maze.print_maze())
        else:
            print("\nYou hit a wall!\nConnection closed.\n")
            break




if __name__ == "__main__":
    main()
