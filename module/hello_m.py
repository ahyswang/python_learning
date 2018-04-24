__author__ = 'wangys'

import sys

# public method
def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world!')
    elif len(args) == 2:
        print('Hello, %s!'% args[1])
    else:
        print('Too many arguments!')
# private method
def __private_method():
    print('private method')

# unittest
if __name__=='__main__':
    test()