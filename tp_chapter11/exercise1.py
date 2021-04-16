## Create a dictionary with words of file .txt as keys
# @param None
# @return d
#
def word2key():
    fin = open("C:/Users/loren/Desktop/Informatica/tomorrowDevs/learn_python/python_exercises/tp_chapter8/words.txt")
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = ""
    return d

# Print the dictionary
print(word2key())

