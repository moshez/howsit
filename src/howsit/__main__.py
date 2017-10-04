import sys

import seashore

from howsit import main

if __name__ != '__main__':
    raise ImportError('this module cannot be imported')

executor = seashore.Executor(seashore.Shell())
main.main(executor, sys.stdout, sys.argv)
