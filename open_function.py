# file = open("icecream_file.txt", mode="w")
# file.write("Hello World!\n")
# file.write("Hello World!")

# file.close()



# file = open("icecream_file.txt", mode="w")
# file.write("Word, frequency/n")
# file.write("Hello World!")

# for k,v in d.items()
# file.write(f'{k},{v}\n")



# file.close()



d = collections.Counter(article_project)
#writing the information
file = open("article_project.txt",mode="w")
file.write("word,frequency\n")
for k,v in d.items():
    file.write(f"{k},{v}\n")
file.close()





#extra stuff -- f-strings
# name = "Laszlo"
# fav_food = "pancakes"
# s = f"Hi, I'm {name}, I like {fav_food}." 
# print(s)



