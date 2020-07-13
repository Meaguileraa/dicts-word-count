def separated(file):
    poem = open(file)

    word_count = {}

    for line in poem: 
        line = line.strip()
        words = line.split(' ')

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else: 
                word_count[word] = 1

                for key, value in word_count.items():


                    print(key, value)
    poem.close()
separated("test.txt")
separated("twain.txt")