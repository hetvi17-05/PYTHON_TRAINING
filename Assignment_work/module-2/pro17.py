#Write a Python function that takes a list of words and returns the length of the longest one.
def fing_longest_word(word_list):
    word_len = []
    for n in word_list:
     word_len.append(len(n), n)
    word_len.sort()
    