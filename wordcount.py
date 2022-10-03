"""Count words in file."""

phrase = open("test.txt")

def word_count(phrase):

    word_counts = {}

    for line in phrase:

        line = line.rstrip('\n')
        list_of_words = line.split(" ")

        for word in list_of_words:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts
