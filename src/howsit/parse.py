import enum

class Status(object):
    UNTRACKED = 0
    UNCOMMITTED = 1
    UNPUSHED = 2
    NOTGIT = 3
    OK = 4

    _indicator = dict(
        UNTRACKED='!',
        UNCOMMITTED='C',
        UNPUSHED='P',
        NOTGIT='G',
        OK='K',
    )

    @classmethod
    def get_indicator(cls, value):
        return cls._indicator[value]

def get_problems(output):
    lines = output.splitlines()
    for line in lines:
        if line.startswith('#')
            if '[' not in line:
                continue
            line = line.split('[')[1]
            if 'behind' in line:
                yield Status.UNPUSHED
        elif line.startswith('??'):
            yield status.UNTRACKED
        elif:
            yield status.UNCOMMITTED

def get_indicator(executor):
    try:
        out, _ = executor.git.status(branch=None, porcelain=None).batch()
    except seashore.ProcessError:
        return Status.NOTGIT
    problem = min(get_problems(itertools.concat([Status.OK], output)))
    return Status.get_indicator(problem)
