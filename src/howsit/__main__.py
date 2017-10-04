import sys

import seashore

from howsit import main

if __name__ != '__main__':
    raise ImportError('this module cannot be imported')

EXECUTOR = seashore.Executor(seashore.Shell())
main.main(EXECUTOR, sys.stdout, sys.argv)
