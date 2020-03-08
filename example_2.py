def letter_counter(word):
    '''excpect something cool ok wow 
    '''
    d = {}
    for char in word:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1 
    return d
def anagram_finder(word1,word2):
    if letter_counter(word1) == letter_counter(word2):
        return True
    else:
        return False
