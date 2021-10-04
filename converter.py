# prime
import math
from printd import printd


def convert_to_number(text):
    input = text
    output = ""
    i = 0
    for character in input:
        i += 1
        # a is 96, so we take of 96, but we need everything to
        # be 2 digits so I add 9 and a becomes 10
        number = ord(character) + 100 - 32
        output += str(number)
        if(i % 10 == 0):
            output += "\n"
    if(i % 10 != 0):
        for j in range(10 - (i % 10)):
            output += "000"
    print(output)
    return output


def convert_to_text(number_as_text):
    input = number_as_text
    n = 3
    output = [input[i:i+n] for i in range(0, len(input), n)]
    text = ""
    for charnum in output:
        if(charnum != "000"):
            text += chr(int(charnum) + 32 - 100)
    print(text)
    return text
