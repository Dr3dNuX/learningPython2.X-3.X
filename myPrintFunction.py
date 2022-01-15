import sys

def print_two(object):
    FILE = sys.stdout
    FILE.write(str('{}\n'.format(object)))
    FILE.close()

print_two("Hello World")