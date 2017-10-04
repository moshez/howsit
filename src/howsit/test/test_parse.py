import unittest

from howsit import parse

class ProblemTest(unittest.TestCase):

    def test_empty(self):
        output = ""
        l = list(parse.get_problems(output))
        ok = l.pop(0)
        self.assertEquals(l, [])
        self.assertEquals(ok.name, 'OK')
