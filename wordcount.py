def separated(file):
    poem = open(file)

    word_count = {}

    for line in poem: 
        line = line.strip()
        words = line.split(' ')


#need to count word 
#need to return key and value 

    poem.close()
separated("test.txt")
separated("twain.txt")