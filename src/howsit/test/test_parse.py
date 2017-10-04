import unittest

import seashore

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

class DummyShell(object):

    is_git = True

    def clone(self):
        return self

    def batch(self, cmd, *args, **kwargs):
        if (cmd[:2] == ['git', 'status'] and
            set(cmd[2:]) == set(['--porcelain', '--branch'])):
             if self.is_git:
                 return '', ''
             else:
                 raise seashore.ProcessError(2, '', 'not a git directory\n')
        raise ValueError("unknown command", cmd, args, kwargs)


class IndicatorTest(unittest.TestCase):

    def setUp(self):
        self.shell = DummyShell()
        self.executor = seashore.Executor(self.shell)

    def test_simple_get_indicator(self):
        ret = parse.get_indicator(self.executor)
        self.assertEquals(ret, 'K')

    def test_not_git_get_indicator(self):
        self.shell.is_git = False
        ret = parse.get_indicator(self.executor)
        self.assertEquals(ret, 'G')
