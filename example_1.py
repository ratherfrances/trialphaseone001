# import example 
# # print(dir(example))

# word = "apple"
# d = example.letter_counter(word)
# print(d)


# import random

# # print(dir(random))
# help(random.randint)

# x = random.randit(1,10)
# print(x)

# import example_2
# help(example_2)


# import collections 
# d = collections.Counter("apple")
# print(d)
















# methods for dictionarys 
     #keys      #values
# d = {} 
# d["Harry"] = "vanilla"
# d["Ron"] = "strawberry"
# d["hermione"] = "strawberry"
# d["Hagrid"] = "chocolate"

#print(dir(d))


# for k in d.keys(): 
# 	print(k,d[k])


# or v in d.values(): 
# 		print(v)

# print (d.items())

# for i in d.items(): 
# 	print(i[0],i[1])


# for k,v in d.items():
# 	print(k,v)



















# methods for dictionarys 
     #keys      #values
# d = {} 
# d["Harry"] = "vanilla"
# d["Ron"] = "strawberry"
# d["hermione"] = "strawberry"
# d["Hagrid"] = "chocolate"

#print(dir(d))


# for k in d.keys(): 
# 	print(k,d[k])


# or v in d.values(): 
# 		print(v)

# print (d.items())

# for i in d.items(): 
# 	print(i[0],i[1])


# for k,v in d.items():
# 	print(k,v)


# for k in d.keys(): 
# 	print(k,d[k])


# for v in d.items():
#         if v == "strawberry":



FIND WHO LIKES STRAWBERRY 

d = {}
d["Harry"] = "vanilla"
d["Ron"] = "strawberry"
d["Hermione"] = "strawberry"
d["Hagrid"] = "chocolate"
ice_cream = "strawberry"
people = []
for k,v in d.items():
    if v == ice_cream:
        people.append(k) 
print(people) 




