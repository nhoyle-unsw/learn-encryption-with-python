# prime
import math
from printd import printd


def convert_to_numbers(text):
    input = text
    output = ""
    i = 0
    for character in input:
        i += 1
        # I add 100 to the ascii code so that no characters have leading zeros
        number = ord(character) + 100
        output += str(number)
        if(i % 10 == 0):
            output += "\n"
    if(i % 10 != 0):
        # add padding up to t10 characters
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
        # only include non zero characters (this removes the padding)
        if(charnum != "000"):
            text += chr(int(charnum) - 100)
    print(text)
    return text


def convert_file(filename):
