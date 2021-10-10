# -*- coding: utf-8 -*-
# factors
import math
from printd import printd


def convert_to_numbers(text):
    """[This function converts a string of text into 3 digit numbers in blocks of 10]

    Args:
        text ([type]): [description]

    Returns:
        [type]: [description]
    """
    input = text
    output_as_str = ""
    output_as_int_list = []
    current_number_as_str = ""
    i = 0
    for character in input:
        i += 1
        # We add 100 to the ascii code so that no characters have leading zeros
        char_as_int = ord(character) + 100
        current_number_as_str += str(char_as_int)
        if(i % 10 == 0):
            output_as_str += current_number_as_str + "\n"
            output_as_int_list.append(int(current_number_as_str))
            current_number_as_str = ""
    if(i % 10 != 0):
        # add padding up to 10 characters
        for j in range(10 - (i % 10)):
            current_number_as_str += "000"
        output_as_str += current_number_as_str
        output_as_int_list.append(int(current_number_as_str))
    printd(output_as_str, output_as_int_list)
    return output_as_int_list, output_as_str


def convert_to_text(number_as_text):
    input = number_as_text
    n = 3
    output = [input[i:i+n] for i in range(0, len(input), n)]
    text = ""
    for charnum in output:
        # only include non zero characters (this removes the padding)
        if(charnum != "000"):
            printd("charnum:", charnum)
            text += chr(int(charnum) - 100)
    printd(text)
    return text
