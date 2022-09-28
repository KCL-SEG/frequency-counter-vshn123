"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for el in items:
        try:
            frequencies[str(el)] += 1
        except KeyError:
            frequencies[str(el)] = 1

    return frequencies
