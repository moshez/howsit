from howsit import parse
from howsit.test import self_test

def main(executor, output, args):
    if '--self-test' in args:
        self_test.self_test(executor, output, args[-1])
    output.write(parse.get_indicator(executor))

