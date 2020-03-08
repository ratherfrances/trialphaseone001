
#PIGLATIN_PIGLATIN

def pig_latin(word):
    vowels = ['a','e','i','o','u']

    for i in range(0,len(word),1):
        if word[i] in vowels:
            idx = i
            break

    if idx == 0:
        word = word + 'yay'
    else:
        part_2 = word[0:idx:1]
        part_1 = word[idx::1]

        word = part_1 + part_2 + "ay"

    return word

plw = pig_latin("scratch")
print(plw) 