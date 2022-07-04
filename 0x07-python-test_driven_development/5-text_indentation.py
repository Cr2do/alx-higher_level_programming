#!/usr/bin/python3
"""
text_indentation module
"""


def text_indentation(text):
    """
    text_indentation module
    """
    charPrinted = False
    if type(text) != str:
        raise TypeError("text must be a string")
    for letter in text:
        if charPrinted and letter == ' ':
            charPrinted = False
        else:
            if letter == '.' or letter == '?' or letter == ':':
                print(letter, end='')
                print()
                print()
                charPrinted = True
            else:
                print(letter, end='')
