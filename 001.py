#read in string
# example = "This is a sentence. this is another sentence, too!"
#clean up string
# example = example.replace(".","")
# example = example.replace("!","")
# example = example.replace(",","")
# print(example) 
#split to get a list of words
# word_list = example.split() 
# print(word_list)  
#count everything (using dictionary)
# "this" : 2
# "a" : 1


# word_counter = {}

# file = open("article.txt")
# text = file.read()
# file.close()

# text = text.replace(".","")
# text = text.replace(",","")
# text = text.replace("'","")
# text = text.replace("[","")
# text = text.replace("]","")
# text = text.replace("–","")
# text = text.replace("’","")
# text = text.replace('"',"")
# text = text.replace('"',"")


# # print(text)
# word_counter = text.split() 

# print(word_counter)



unwanted = [".","!","?","-","*","—"]
for i in unwanted:
    if i in text:
        text = text.replace(i,"")
print(text)





acc_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9"]
text= text.lower()
for let in text:
    if let not in acc_char:
        text= text.replace (let," ")










