from howsit import parse

def main(executor, output, args):
    output.write(parse.get_indicator(executor))

