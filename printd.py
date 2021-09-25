# printd is used to print out debug statements
from __future__ import print_function
import sys

# https://stackoverflow.com/questions/38246928/using-global-variable-in-python-among-modules-in-different-packages
is_debug = False


def printd(*args, **kwargs):
    # print("is_debug_iteration:", is_debug_iteration)
    if is_debug:
        input()
        print(*args, file=sys.stdout, **kwargs)
    else:
        pass
