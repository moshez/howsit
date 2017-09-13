import enum

@enum.unique
class _Status(enum.IntEnum):
    UNTRACKED = 0
    UNCOMMITTED = 1
    UNPUSHED = 2
    NOTGIT = 3
    OK = 4

_indicator = {
    _Status.UNTRACKED: '!',
    _Status.UNCOMMITTED: 'C',
    _Status.UNPUSHED: 'P',
    _Status.NOTGIT: 'G',
    _Status.OK: 'K',
}

def _get_indicator(value):
    return _indicator[value]

def get_problems(output):
    lines = output.splitlines()
    for line in lines:
        if line.startswith(b'#'):
            if b'[' not in line:
                continue
            line = line.split(b'[')[1]
            if b'behind' in line:
                yield _Status.UNPUSHED
        elif line.startswith(b'??'):
            yield _Status.UNTRACKED
        else:
            yield _Status.UNCOMMITTED
    yield _Status.OK

def get_indicator(executor):
    try:
        out, _ = executor.git.status(branch=None, porcelain=None).batch()
    except seashore.ProcessError:
        return _Status.NOTGIT
    problem = min(get_problems(out))
    return _get_indicator(problem)
