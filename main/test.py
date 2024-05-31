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
        # self.assertEqual(minesweeper("*..\n..*"), "*21\n12*")

    # def final_test(self):
    #     self.assertEqual(minesweeper("*...\n....\n.*..\n...."), "*100\n2210\n1*10\n1110")
    #     self.assertEqual(minesweeper("**...\n.....\n.*..."), "**100\n33200\n1*100")


def minesweeper(field):
    lines = field.split('\n')
    solved_lines = solve_lines(lines)

    return "\n".join(solved_lines)


def solve_lines(lines):

    solved_lines = []
    for line in lines:
        solved_line = ""
        for x in range(len(line)):
            if is_mine(line, x):
                solved_line += "*"
            else:
                nb_mine = count_mines_around(x, line)

                solved_line += str(nb_mine)
        solved_lines.append(solved_line)
    return solved_lines


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