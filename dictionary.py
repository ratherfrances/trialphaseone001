# pb = {}

#another way to write info to make a dictionary 
#{'John': 91859827356, 'Mark': 91869827396, 'Cynthia Mouse': 91889827306}

#keys        #values 
# pb["John"] = 91859827356
# pb["Mark"] = 91869827396
# pb["Cynthia"] = 91889827306

# print(pb)
# print(pb[Cynthia])



# fe = {}
# fe["pomme"] = "apple"
# fe["chat"] = "cat"
# # fe["bonhomme de neige"] = "snowman"
# # print(fe["pomme"]) 


# # df = []
# # df ["math"] = [600,500,400]
# # df ["verbal"] = [700,600,800]
# # #print(df["math"])

# # the MENU: 


# # menu = {}
# # menu["hamburger"] = 8.95 
# # menu["po boy"] = 11.95 
# # menu["water"] = 1.00 
# # menu[ "rose"] = 12.00


# # food_order = "hamburger"
# # drink_order = "water"


# # total_cost = menu[food_order] + menu[drink_order]
# # print(total_cost)




# # from teacher ---- 
# # menu = {}
# # menu["hamburger"] = 8.95
# # menu["water"] = 1.00
# # menu["pterodactyl"] = 5.95

# #2) Try getting food_order from input and drink_order from input
# # and calculating total cost of those orders.

# # food_order = input("Whatcha wanna eat?  ")
# # drink_order = input("Whatcha wanna drink?  ")
# # total_cost = menu[food_order] + menu[drink_order]
# # print(total_cost) 
















# scrabble 


# letter_vals = {'E': 1, 'A': 1, 'O': 1, 'T': 1,
#                'I': 1, 'N': 1, 'R': 1, 'S': 1,
#                'L': 1, 'U': 1, 'D': 2, 'G': 2,
#                'C': 3, 'M': 3, 'B': 3, 'P': 3,
#                'H': 4, 'F': 4, 'W': 4, 'Y': 4, 'V':4,
#                'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10} 


# word = 'APPLE'
# total = 0
# for i in word:
# 	#print(i, letter_vals[i])
#     total = total + letter_vals[i]
# print(total)



# #total += letter_vals["A"]
# #total += letter_vals["P"]
# #total += letter_vals["P"]
# #total += letter_vals["L"]
# #total += letter_vals["E"]













# def word_scorer(word):
# 	letter_vals = {'E': 1, 'A': 1, 'O': 1, 'T': 1,
# 	               'I': 1, 'N': 1, 'R': 1, 'S': 1,
# 	               'L': 1, 'U': 1, 'D': 2, 'G': 2,
# 	               'C': 3, 'M': 3, 'B': 3, 'P': 3,
# 	               'H': 4, 'F': 4, 'W': 4, 'Y': 4, 'V':4,
# 	               'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10} 


# 	total = 0
# 	for i in word:
# 	    total = total + letter_vals[i]
# 	return total

# result = word_scorer("COOL")
# print(result)



# SCRABBLE 
# def word_scorer(word):  
# word = word.upper()

# 	letter_vals = {'E': 1, 'A': 1, 'O': 1, 'T': 1,
# 	               'I': 1, 'N': 1, 'R': 1, 'S': 1,
# 	               'L': 1, 'U': 1, 'D': 2, 'G': 2,
# 	               'C': 3, 'M': 3, 'B': 3, 'P': 3,
# 	               'H': 4, 'F': 4, 'W': 4, 'Y': 4, 'V':4,
# 	               'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10} 


# 	word = 'APPLE'
# 	total = 0
# 	for i in word:
# 		#print(i, letter_vals[i])
# 	    total = total + letter_vals[i]
# 	return total 
# print (word_scorer("apple"))


# d= "apple"

# d = {}
# d ["a"] = 1 
# d ["p"] = 2 
# d ["d"] = 1 
# d ["e"] = 2 

# print(d["p"])


# PRINT A DICTIONARY (counter)

# word = "apple"

# d = {}
# for char in word: 
# 	# print(i)
# 	if char not in d: 
# 		d[char] = 1 
# 	else: 
# 		d[char] += 1 
# print(d) 




# word_one = "life" 
# word_two = "file" 

# d_1= {}
# d_2= {}
# for char in word_one: 
# 	if char not in d_1: 
# 		d_1[char] =1 
# 	else: 
# 		d_1[char] +=1 

# for char in word_two: 
# 	if char not in d_2: 
# 		d_2[char] =1 
# 	else: 
# 		d_2[char] +=1 

# if d_1 == d_2: 
#     print(True)
# else:
#     print(False)


# ----------------------------


#     word_one = "life" 
# word_two = "file" 

# d_1= {}
# d_2= {}
# for char in word_one: 
#     if char not in d_1: 
#         d_1[char] =1 
#     else: 
#         d_1[char] +=1 

# for char in word_two: 
#     if char not in d_2: 
#         d_2[char] =1 
#     else: 
#         d_2[char] +=1 

# if d_1 == d_2: 
#     print(True)
# else:
#     print(False)



# PRINT A DICTIONARY (counter)





# def anagrams(word1, word2):

# d_1= {}
# for char in word_one: 
#     if char not in d_1: 
#         d_1[char] =1 
#     else: 
#         d_1[char] +=1 

# for char in word_two: 
#     if char not in d_2: 
#         d_2[char] =1 
#     else: 
#         d_2[char] +=1 

# if d_1 == d_2: 
#     print(True)
# else:
#     print(False)



# THEN MAKE ANAGRAM A FUNCTION: 


# def anagrams(word1,word2):
#     d1 = {}
#     for char in word1:
#         if char not in d1:
#             d1[char] = 1
#         else:
#             d1[char] += 1 
#     #print(d1)
#     d2 = {}
#     for char in word2:
#         if char not in d2:
#             d2[char] = 1
#         else:
#             d2[char] += 1 
#     #print(d2)
#     if d1 == d2:
#         return True
#     else:
#         return False 
# outcome = anagrams("add","dad")
# print(outcome) 



# ANOTHER ANAGRAM WAY: 

# def anagrams(word1,word2):
#     d1 = {}
#     for char in word1:
#         if char not in d1:
#             d1[char] = 1
#         else:
#             d1[char] += 1 
#     #print(d1)
#     d2 = {}
#     for char in word2:
#         if char not in d2:
#             d2[char] = 1
#         else:
#             d2[char] += 1 
#     #print(d2)
#     if d1 == d2:
#         return True
#     else:
#         return False 
# outcome = anagrams("add","dad")
# print(outcome) 



# ANOTHER ANAGRAM WAY: 

# def letter_counter(word):
#     d = {}
#     for char in word:
#         if char not in d:
#             d[char] = 1
#         else:
#             d[char] += 1 
#     return d
# def anagram_finder(word1,word2):
#     if letter_counter(word1) == letter_counter(word2):
#         return True
#     else:
#         return False
# print(anagram_finder("add","dad"))  



# ANOTHER ANAGRAM WAY USING INPUT: 

# def letter_counter(word):
#     d = {}
#     for char in word:
#         if char not in d:
#             d[char] = 1
#         else:
#             d[char] += 1 
#     return d
# def anagram_finder(word1,word2):
#     if letter_counter(word1) == letter_counter(word2):
#         return True
#     else:
#         return False
# def main():
#     print("Welcome to anagram solver!  Enter two words")
#     print("and I'll tell you whether or not they're anagrams!")
#     print("May fortune follow you wherever you go!")
#     word1 = input("First word:  ")
#     word2 = input("Second word:  ")
#     if anagram_finder(word1,word2):
#         print("Wow! They're anagrams!")
#     else:
#         print("Wow! They're not anagrams!") 
# main() 



# ARTICLE EX: 

# file = open ("article.txt")
# # print(dir(file))

# # print(file.read())
# text = file.read()

# file.close()

# print(text)






# TO OVERWRITE: 
# def ad(a,b=1000):
#     total = a + b 
#     return total 

# print(add(3,b=3))

# same idea: 



# def add(a,b=1000):
#     total = a + b
#     return total
# print(add(3,b=10)) 




# example = "this is stuff"

# # print(example.split())


# word_list = example.split()
# print(word_list)








        #read in string
# example = "This is a sentence. this is another sentence, too!"
#         #clean up string
# example = example.replace(".","")
# example = example.replace("!","")
# example = example.replace(",","")
# print(example) 
#         #split to get a list of words
# word_list = example.split() 
# print(word_list)  
        #count everything (using dictionary)
        # "this" : 2
        # "a" : 1


def count(values,what_to_count):
#     values = [7,7,2,4,2,2,2,2]
#     what_to_count = 2
    counter = 0
    for i in values:
        if i == what_to_count:
            counter += 1
    return counter
some_list = [7,7,7,1,5,1]
how_many = count(some_list,7)
print(how_many) 







