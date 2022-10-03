"""Count words in file."""

# with open('test.txt') as file:
#     phrase = file.read()

phrase = open("test.txt")

def word_count(phrase):

    word_counts = {}
    #list_of_strings = []

    # for line in phrase:
    #     list_of_strings.append(line.split(" "))

    for line in phrase:

        line = line.rstrip('\n')
        list_of_words = line.split(" ")

        for word in list_of_words:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

    #print(phrase)