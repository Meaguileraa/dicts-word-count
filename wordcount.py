import sys
from collections import Counter

def separated(file):

    """Returns a dictionary with a count of how many times each word duplicates in file """
    poem = open(file)
    print(sys.argv)

    word_count = {}

    for line in poem: 
        line = line.strip()
        words = line.split(' ')

