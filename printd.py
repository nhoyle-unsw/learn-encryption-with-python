# -*- coding: utf-8 -*-
# printd is used to print out debug statements
from __future__ import print_function
from inspect import getframeinfo, stack
import sys
import os

# https://stackoverflow.com/questions/38246928/using-global-variable-in-python-among-modules-in-different-packages
is_debug = False
is_verbose = False

# https://www.w3schools.com/python/gloss_python_function_arbitrary_keyword_arguments.asp


def printd(*args, **kwargs):
    if is_verbose:
        caller = whoCalledThisFunction()
        print_verbose(caller, *args, **kwargs)
    elif is_debug:
        print_to_console(*args, **kwargs)


def printv(*args, **kwargs):
    if is_verbose:
        caller = whoCalledThisFunction()
        print_verbose(caller, *args, **kwargs)


def print_verbose(caller, *args, **kwargs):

    print_to_console(debuginfo(caller), *args, **kwargs)


def print_to_console(*args, **kwargs):
    print(*args, file=sys.stdout, **kwargs)


# https://stackoverflow.com/questions/24438976/python-debugging-get-filename-and-line-number-from-which-a-function-is-called

def whoCalledThisFunction():
    return getframeinfo(stack()[2][0])


def debuginfo(caller):
    # https://www.codegrepper.com/code-examples/python/remove%20path%20from%20filename%20python
    return "%s - %s:%d - " % (caller.function, os.path.basename(caller.filename), caller.lineno)
