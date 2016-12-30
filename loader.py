
def load(file="./mapa.txt"):
    grid = []
    with open(file, "r") as f:
        arch = list(f.readlines())
        for y in range(0, len(arch)):
            grid.append([])
            for x in range(0, len(arch[y])-1):
                character = arch[y][x]
                if (x in (0, len(arch[y])-2) or y in (0, len(arch)-1)) and character == " ":
                    grid[y].append("#")
                else:
                    if character in ("+", "-", "|", "#", "█"):
                        grid[y].append("█")
                    elif character == " ":
                        grid[y].append(" ")
    return grid

load()
