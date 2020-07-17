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

        for word in words:
            word = word.lower()
            word = word.rstrip(',.?;:!#$%^&*()-_')
            if word in word_count:
                word_count[word] += 1
            else: 
                word_count[word] = 1

    for key, value in word_count.items():
        print(key, value)
        word_count = Counter(word_count)
    return sorted(word_count)


separated("test.txt")
#separated("twain.txt")