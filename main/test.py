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
        self.assertEqual(minesweeper("*..*.*..*....*"), "*11*2*11*1001*")
        self.assertEqual(minesweeper("*..\n..*"), "*21\n12*")

    # def final_test(self):
    #     self.assertEqual(minesweeper("*...\n....\n.*..\n...."), "*100\n2210\n1*10\n1110")
    #     self.assertEqual(minesweeper("**...\n.....\n.*..."), "**100\n33200\n1*100")


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
            if is_mine(lines, x, y):
                solved_line += "*"
            else:
                nb_mine = count_mines_around(x, y, lines)
                solved_line += str(nb_mine)

        solved_lines.append(solved_line)
    return solved_lines


def count_mines_around(x, y, lines):
    nb_mine = 0
    if is_mine(lines, x + 1, y + 1):
        nb_mine += 1
    if is_mine(lines, x - 1, y + 1):
        nb_mine += 1
    if is_mine(lines, x + 1, y - 1):
        nb_mine += 1
    if is_mine(lines, x - 1, y - 1):
        nb_mine += 1
    if is_mine(lines, x - 1, y):
        nb_mine += 1
    if is_mine(lines, x + 1, y):
        nb_mine += 1
    if is_mine(lines, x, y + 1):
        nb_mine += 1
    if is_mine(lines, x, y - 1):
        nb_mine += 1
    return nb_mine


def is_mine(lines, x, y):
    if y < 0 or y >= len(lines):
        return False
    line = lines[y]
    if x < 0 or x >= len(line):
        return False
    return line[x] == "*"