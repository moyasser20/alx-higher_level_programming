#!/usr/bin/python3
"""Print alphabet lowercase except q and e,not followed by new line."""

for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
