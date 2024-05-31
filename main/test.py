import unittest


class TestMinesweeper(unittest.TestCase):

    def test_minesweeper(self):
        self.assertEqual(minesweeper(""), "")
        self.assertEqual(minesweeper("*"), "*")
        self.assertEqual(minesweeper("."), "0")
        self.assertEqual(minesweeper(".."), "00")
        self.assertEqual(minesweeper("**"), "**")
        self.assertEqual(minesweeper("**\n**"), "**\n**")
        self.assertEqual(minesweeper("***\n***\n***"), "***\n***\n***")
        self.assertEqual(minesweeper(".*"), "1*")
        self.assertEqual(minesweeper("*."), "*1")
        self.assertEqual(minesweeper(".*."), "1*1")
        self.assertEqual(minesweeper("*.*"), "*2*")


def minesweeper(field):
    lines = field.split('\n')
    solved_lines = []
    for line in lines:
        solved_lines.append(solve_line(line))

    return "\n".join(solved_lines)


def solve_line(line):
    solved_line = ""
    for x in range(len(line)):
        if is_mine(line, x):
            solved_line += "*"
        else:
            nb_mine = count_mines_around(x, line)

            solved_line += str(nb_mine)
    return solved_line


def count_mines_around(x, line):
    nb_mine = 0
    if is_mine(line, x + 1):
        nb_mine += 1
    if is_mine(line, x - 1):
        nb_mine += 1
    return nb_mine


def is_mine(line, x):
    if x < 0:
        return False
    if x >= len(line):
        return False
    return line[x] == "*"