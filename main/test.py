import unittest

from main.minesweeper import minesweeper


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

    def final_test(self):
        self.assertEqual(minesweeper("*...\n....\n.*..\n...."), "*100\n2210\n1*10\n1110")
        self.assertEqual(minesweeper("**...\n.....\n.*..."), "**100\n33200\n1*100")


