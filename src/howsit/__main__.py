import sys

import seashore

from howsit import parse

if __name__ != '__main__':
    raise ImportError('this module cannot be imported')

executor = seashore.Executor(seashore.Shell())
sys.stdout.write(parse.get_indicator(executor))
