import loader
import time
import curses


class Maze:

    def __init__(self, grid):
        self.grid = grid
        self.pointer = self.set_pointer()
        self.route = [self.pointer, self.pointer]

    def set_pointer(self):
        for y in range(0, len(self.grid)):
            try:
                return self.grid[y].index("#"), y
            except ValueError:
                pass

    def run(self):
        return self.move(self.select())

    def move(self, selection):
        if self.get_coords(selection) == "#":
            return True
        if selection != self.route[-2]:
            self.pointer = selection
            self.route.append(selection)
            self.set_coords(selection, "*")
        else:
            self.set_coords(self.pointer, ".")
            self.pointer = self.route[-2]
            self.route.pop()

    def select(self):
        variacion = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for x in variacion:
            coords = (self.pointer[0] + x[0], self.pointer[1] + x[1])
            if self.get_coords(coords) in (" ", "*", "#") and coords not in self.route:
                return coords
        return self.route[-2]

    def printea(self, stdscr):
        stdscr.clear()
        for y in self.grid:
            for x in y:
                if x == "*":
                    stdscr.addstr("█", curses.color_pair(curses.COLOR_GREEN))
                elif x == "█":
                    stdscr.addstr(x, curses.color_pair(curses.COLOR_WHITE))
                elif x==".":
                    stdscr.addstr("█", curses.color_pair(curses.COLOR_RED))
                else:
                    stdscr.addstr(x)
            stdscr.addstr("\n")
        stdscr.refresh()

    def get_coords(self, coords):
        return self.grid[coords[1]][coords[0]]

    def set_coords(self, coords, objeto):
        self.grid[coords[1]][coords[0]] = objeto


def main(stdscr, debugging=False):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i, i, -1)
    maze = Maze(loader.load())
    salir = False
    while not salir:
        salir = maze.run()
        if debugging:
            maze.printea(stdscr)
            time.sleep(0.1)
    maze.printea(stdscr)
    stdscr.getch()

curses.wrapper(main)

