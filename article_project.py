# unwanted = [".","!","?","-","*","—"]
# for i in unwanted:
#     if i in text:
#         text = text.replace(i,"")
# print(text)




# -----



# acc_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9"]
# text= text.lower()
# for let in text:
#     if let not in acc_char:
#         text= text.replace (let," ")


# --------


import collections
#read in article
file = open("article.txt")
text = file.read() #string
file.close() 
#clean up the string (lowercase everything) (remove unwanted punctuation)
text = text.lower()
for let in text:
    if let.isalnum() == False:
        text= text.replace(let," ")
#print(text) 
word_list = text.split()


#print(word_list) 
#manually counting everything
# d = {}
# for word in word_list:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d) 


# d = collections.Counter(word_list)
# print(d) 






# file = open("icecream_file.txt", mode="w")
# file.write("Hello World!")
# file.close()





