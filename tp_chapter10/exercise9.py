import os
from time import time

## Read a file .txt and arrange each word in a list using append method
# @param file_path the file path .txt string
# @return a t list with one element per word
def list_builder(file_path):
    fin = open(os.path.abspath(file_path))
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t
    
## Read a file .txt and arrange each word in a list using t = t + [x] idiom
# @param file_path the file path .txt string
# @return a t list with one element per word
def list_builder2(file_path):
    fin = open(os.path.abspath(file_path))
    t = []
    for line in fin:
        word = line.strip()
        t += [word]
    return t

# Compute time list_builder function takes to run
start_time = time()
t = list_builder('../tp_chapter8/words.txt')
elapsed_time = time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

# Compute time the list_builder2 function takes to run
start_time = time()
t = list_builder2('../tp_chapter8/words.txt')
elapsed_time = time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')