import unittest

from howsit import parse

class ProblemTest(unittest.TestCase):

    def test_empty(self):
        output = ""
        l = list(parse.get_problems(output))
        ok = l.pop(0)
        self.assertEquals(l, [])
        self.assertEquals(ok.name, 'OK')

    def test_no_upstream(self):
        output = "## v1\n"
        l = list(parse.get_problems(output))
        ok = l.pop()
        problem = l.pop(0)
        self.assertEquals(l, [])
        self.assertEquals(ok.name, 'OK')
        self.assertEquals(problem.name, 'NO_UPSTREAM')

    def test_no_push(self):
        output = "## v1...origin/v1 [ahead 1]\n"
        l = list(parse.get_problems(output))
        ok = l.pop()
        problem = l.pop(0)
        self.assertEquals(l, [])
        self.assertEquals(ok.name, 'OK')
        self.assertEquals(problem.name, 'UNPUSHED')

    def test_untracked(self):
        output = "?? fff\n"
        l = list(parse.get_problems(output))
        ok = l.pop()
        problem = l.pop(0)
        self.assertEquals(l, [])
        self.assertEquals(ok.name, 'OK')
        self.assertEquals(problem.name, 'UNTRACKED')

    def test_uncommitted(self):
        output = " M src/howsit/test/test_parse.py\n"
        l = list(parse.get_problems(output))
        ok = l.pop()
        problem = l.pop(0)
        self.assertEquals(l, [])
        self.assertEquals(ok.name, 'OK')
        self.assertEquals(problem.name, 'UNCOMMITTED')


