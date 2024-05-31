def minesweeper(field):
    lines = field.split('\n')
    solved_lines = solve_lines(lines)
    return "\n".join(solved_lines)


def solve_lines(lines):
    solved_lines = []
    for y in range(len(lines)):
        solved_line = ""
        line = lines[y]
        for x in range(len(line)):
            if is_mine(x, y, lines):
                solved_line += "*"
            else:
                nb_mine = count_mines_around(x, y, lines)
                solved_line += str(nb_mine)
        solved_lines.append(solved_line)
    return solved_lines


def count_mines_around(x, y, lines):
    nb_mine = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if is_mine(x + i, y + j, lines):
                nb_mine += 1
    return nb_mine


def is_mine(x, y, lines):
    if y < 0 or y >= len(lines):
        return False
    line = lines[y]
    if x < 0 or x >= len(line):
        return False
    return line[x] == "*"
