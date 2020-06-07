"""
Functional test
"""
import os
import sys


def run_me(executor):
    """
    Run ourselves
    """
    howsit = [sys.executable, '-m', 'howsit']
    return executor.command(howsit).batch()


def self_test(executor, output, cwd):
    """
    Functional test function
    """
    executor = executor.chdir(cwd)
    executor.command(['git', 'init']).batch()
    output, error = run_me(executor)
    if error != b'':
        raise ValueError('stderr not empty', error)
    if output != b'U':
        raise ValueError('output not U', output)
    with open(os.path.join(cwd, 'not_in_git'), 'w') as filep:
        filep.close()
    output, error = run_me(executor)
    if error != b'':
        raise ValueError('stderr not empty', error)
    if output != b'!':
        raise ValueError('output not !', output)
    executor.command(['git', 'add', 'not_in_git']).batch()
    output, error = run_me(executor)
    if error != b'':
        raise ValueError('stderr not empty', error)
    if output != b'C':
        raise ValueError('output not C', output)
