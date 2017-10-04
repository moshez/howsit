import enum

import seashore


@enum.unique
class _Status(enum.IntEnum):
    UNTRACKED = 0
    UNCOMMITTED = 1
    UNPUSHED = 2
    NO_UPSTREAM = 3
    NOT_GIT = 4
    OK = 5


_indicator = {
    _Status.UNTRACKED: '!',
    _Status.UNCOMMITTED: 'C',
    _Status.UNPUSHED: 'P',
    _Status.NO_UPSTREAM: 'U',
    _Status.NOT_GIT: 'G',
    _Status.OK: 'K',
}


def get_problems(output):
    lines = output.splitlines()
    for line in lines:
        if line.startswith(b'#'):
            if b'...' not in line:
                yield _Status.NO_UPSTREAM
            if b'[' not in line:
                continue
            line = line.split(b'[')[1]
            if b'ahead' in line:
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
        problem = _Status.NOT_GIT
    else:
        problem = min(get_problems(out))
    return _indicator[problem]
