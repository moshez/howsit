import os
import sys

def run_me(executor):
    me = [sys.executable, '-m', 'howsit']
    return executor.command(me).batch()

def self_test(executor, output, cwd):
    executor = executor.chdir(cwd)
    executor.command(['git', 'init']).batch()
    output, error = run_me(executor)
    if error != b'':
        raise ValueError('stderr not empty', error)
    if output != b'U':
        raise ValueError('output not U', output)
    with open(os.path.join(cwd, 'not_in_git'), 'w') as fp:
        fp.close()
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
