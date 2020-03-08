# # x = 10 
# # print(x < 5000)
# # print(type(True))
# # x = 10 
# # print (x >= 0 and x <= 9)

# # age = 25 
# # if age >= 21:
# #   print("Welcome!") #must be nested and tab 

# # age = 18 
# # if age >= 21:
# #   print("Welcome!")
# # elif age >= 0 and age <21: 
# #   print("You're too young!")

# # age = -2
# # if age >= 21:
# #   print("Welcome!")
# # elif age >= 0 and age <21: 
# #   print("You're too young!")
# # else: 
# #   print("Invalid age.")

# # TEST SCORE CAL

# # test_score >= 0 and score <100 
# # test_score = 600
# # if test_score>= 90:
# #     print("A")
# # elif test_score >= 80 and test_score <= 89:
# #     print("B")
# # elif test_score >= 70 and test_score <= 79:
# #     print("C")
# # elif test_score >= 65 and test_score <= 69:
# #     print("D")
# # else:
# #     print("F")
        

# # help(str.lower)

# # weather = input("What's the weather like? (sunny or rainy)  ")
# # weather = weather.lower()
# # if weather == "sunny":
# #     print("Go for it!")
# # elif weather == "rainy":
# #     print("Maybe another day.")
# # else:
# #     print("Not sure about that weather.") 


# # values = [3,6,71,2,2,5]

# # words = ["apple", "cat", "snowman"]

# # names = ["Tim", "Bryan", "Frances"]

# # for i in names: 
# #   print("Hello",i)

# # print("hello", "Tim")
# # print("hello", "bryan")
# # print("hello", "Frances")



# # names = ["Tim", "Bryan", "Frances"]

# # for i in names: 
# #   print("Hello",i)


# # name_list = ["Tim","Bryan","Frances"]
# # for i in name_list:
# #     print("Hello",i)   


# #     i = "Tim"
# # print("Hello",i)
# # i = "Bryan"
# # print("Hello",i)
# # i = "Frances"
# # print("Hello",i) 


# # name_list = ["Tim","Bryan","Frances"]
# # for i in name_list:
# #     if i != "Tim":
# #         print("Hello",i) 



# # values = [1,2,3]
# # total = 0 
# # for i in values:
# #   total = total + i 
# #   print(total)


# # values = [1,2,3]
# # total = 0
# # for i in values:
# #     total = total + i
# # print(total) 


# # values = [2,2,4,5,2]
# # total = 0 
# # for i in values: 
# #   if i == 2: 
# #       total = total + 1 

# # print(total)


# # values = [2,2,4,5,2] 
# # total = values.count(2)
# # print(total)

# # string = "apple123"

# # for i in string: 
# #   print(i)

# #str.isalpha 
# #str.isdigit 
# #print(letters)
# #print(numbers)


# # Exercise 2.

# # Write a Python program that accepts a string 
# # and calculate the number of digits and letters. use: 
# # help() to learn how to use isalpha() and isdigit()

# #if the character is alphabetical, you've found another letter 
# #if the character is numeric, you've found another number 



# # for i in string: 
# #   print (letters)

# # 4 LOOP 

# # string = "apple123"

# # letters = 0 
# # numbers = 0 

# # for char in string:
# #   if char.isalpha():
# #       letters = letters + 1 
# #   elif char.isdigit():
# #       numbers = numbers + 1 


# # print(letters, numbers)


# # Exercise 4.

# # Create a Temperature converter, Celsius to Fahrenheit:
# # 0 degrees Celsius is equal to 32 degrees Fahrenheit:
# # 0 °C = 32 °F
# # The temperature T in degrees Fahrenheit (°F) is 
# # equal to the temperature T in degrees Celsius (°C) times 9/5 plus 32:
# # T(°F) = T(°C) × 9/5 + 32

# # Example:
# # Convert 20 degrees Celsius to degrees Fahrenheit:
# # T(°F) = 20°C × 9/5 + 32 = 68 °F

# # Add:
# # if Fahrenheit is more than 90, print statement 
# # "a heat warning", if Fahrenheit is less than 30, print 
# # statement "a cold warning"



# # celsius = input ("enter celsius: ")
# # celsius = float(celsius)

# # fahrenheit = celsius * 1.8 + 32 
# # print ("fahrenheit:", fahrenheit)
# # if fahrenheit >= 90: 
# #   print ("a heat warning")
# # elif fahrenheit <= 30: 
# #   print ("a cold warning")








# # fahrenheit = fahrenheit.lower()
# # if fahrenheit == "sunny":
# #     print("a heat warning")
# # elif weather == "rainy":
# #      print("a cold warning")









# # letter= input("enter a character, i'll tell you if it's a vowel:  ")
# # vowels = ["a","e","i","o","u"]
# # if letter in vowels:
# #     print ("vowel")
# # elif letter == "y":
# #     print ("maybe a vowel")
# # else:
# #     print ("consonant")


# # r = range(0,101,1)
# # for i in r:
# #     if i%3 == 0 and i%5 == 0:
# #         print ("Fizzbuzz")
# #     elif i%3 == 0:
# #         print ("Fizz")
# #     elif i% 5== 0:
# #         print ("Buzz")
# #     else:
# #         print (i)

# # celsius = input ("enter celsius: ")
# # celsius = float(celsius)

# # fahrenheit = celsius * 1.8 + 32 
# # print ("fahrenheit:", fahrenheit)
# # if celsius <= 0: 
# #   print ("a cold warning")
# # elif celsius == 10: 
# #   print ("a little cold")
# # elif celsius == 20: 
# #   print ("just right")
# # elif celsius == 30: 
# #   print ("a little hot")
# # elif celsius >= 40: 
# #   print ("a heat warning")
# # else: 
# #   print ("unknown")

# # cels = [0,10,20,30,40]
# # for i in cels: 
# #   print(i, i * (9/5)) + 32) 





# # values = [1,2,3,4,5]
# #add them all together and divide how n=many numbers there are 
# # total = 0 
# # for i in values: 
# #   total = total + i 
# # print(total) 

# # lenght = len(values)

# # average = total / length 
# # print(average)


# # values = []







# #add them all together and divide by how many numbers there are
# # values = [1,2,3,4,5]
# # total = 0
# # for i in values:
# #     total = total + i
# # #print(total)  
# # length = len(values) 
# # average = total / length
# # print(average) 




# # values = [1,2,3,4,5]
# # average = sum(values) / len(values)
# # print(average) 





# # values = [1,4,2,5,8]

# # total = values.count(2)
# # print(total)


# # values = [1,4,2,5,8]
# # new_list = []

# # for i in values: 
#     #square the number 
#     # i = i ** 2 
#     #put in the new list 
# #   new_list.append(i)

# # print(new_list) 

# # values.append(10)
# # print(values)
# # values.append(3) 
# # print(values)


# # values = [1,4,2,5,8]
# # new_list = []

# # for i in values: 
# #   new_list.append(i**2)
# # print(new_list)



# # cels = [0,10,20,30,40]
# # fars = []

# # for i in cels: 
# #   fars.append(i * (9/5) + 32 )
# # print(fars) 


# # F = C * (9/5) + 32 


# # values [4,23,41,5,8]
# # new_list = []

# # for i in values: 
# #   if i <
#     #if it's a single digit number
#     # new_list.append()
# #[0,49,82,0,0]


# # values = [4,23,41,5,8]
# # new_list = []

# # for i in values: 
# #   if i < 10: 








# #       values = [4,23,41,5,8]
# # new_list = [] 
# # for i in values:
# #     if i < 10:
# #         new_list.append(0)
# #     elif i >= 10:
# #         new_list.append(i*2)
# # print(new_list)







# # values = [4,23,41,5,8]
# # new_list = []

# # for i in values: 
# #   i = str(i)
# #   length = len(i)




# # values = [4,23,41,5,8]
# # new_list = [] 
# # for i in values:
# #     i = str(i) #"4"
# #     length = len(i) #1
# #     if length == 1:
# #         new_list.append(0)
# #     elif length == 2:
# #         i = int(i) 
# #         new_list.append(i*2) 



# # values = [4,23,41,5,8]
# # new_list = [] 
# # for i in values:
# #     if len(str(i)) == 1:
# #         new_list.append(0)
# #     elif len(str(i)) == 2: 
# #         new_list.append(i*2) 
# # print(new_list)

# # word= "1-555-567-8231"

# # country_code = [0] 
# # area_code = [ 2 : 5 : 1]
# # prefix = [6 : 9 : 1]
# # line_number = [10 : : 1]

# # print (country_code)
# # print (area_code)
# # print (prefix)
# # pint (line_number)



# # word_list = ["cats", "apple", "snowman"]
# # new_list = []

# # new_list = [word_list.upper() for new_list in input] 
# # print (new_list)
# # for i in word_list: 
# #   i = i.upper() 
# #   i = i [0:3:1]
# #   new_list.append(i)
# # print(new_list)



# # for i in range(0,9,2):
# #   print(i) 




# # word_list = ["apple", "cat", "snowman"]

# # for i in range (o,3,1): 
# #   word_list[i] = "WATERMELON"

# #   print(word_list)


# # word_list = ["apple","cat","snowman"]
# # #               0      1       2
# # for i in range(0,len(word_list),1):
# #      word_list[i] = "WATERMELON"
# # print(word_list)  


# # word_list = ["apple","cat","snowman"]
# # #               0      1       2
# # for i in range(0,len(word_list),1):
# #      word_list[i] =  word_list[i].upper()
# # print(word_list)  


# # word_list = ["apple","cat","snowman"]
# # #               0      1       2 
# # for i in range(0,len(word_list),1):
# #      word_list[i] = word_list[i].upper()
# # print(word_list) 








# # values = [0,10,20,30,40]
# # (cel to fahrenheit) 
# # for i in range (0,len(word_list),1):
# #   values[i] = values[i] * (9/5) + 32 
# # print(values)









# # values = [4,24,41,6,3]
# # for i in range (0,len(values),1):
# #   values[0] = "0"
# #   values[3] = "0"
# #   values[4] = "0"
# # for i in range (1,3,1):
# #   values[i] = values[i] * 2
# # print(values)


# # values = [4,24,41,6,3]

# # for i in range (0,len(values),1):
# #     if i < 10:
# #         values[i] = values[i] * 0 
# #     elif i >= 10:
# #         values[i] = values[i] * 2
# # print(values)


# # correct below!! 
# # values = [4,24,41,6,3]
# # #         0 1  2  3 4
# # for i in range (0,len(values),1):
# #     if values[i] < 10:
# #         values[i] = 0
# #     elif values[i] >= 10:
# #         values[i] = values[i] * 2
# # print(values) 





# #         


# # values = [4,24,41,6,3]


# # word_list[0] = "WATERMELON"
# # word_list[2] = "WATERMELON"
# # word_list[3] = "WATERMELON"
# # print(word_list)




# # word_list2 = ["apple", "cats", "snowman"]
# # #>>> ["APP, "CAT", "SNO"]
# # for i in range (0,len(word_list2),1):
# #     word_list2[i]= word_list2[i].upper()
# #     word_list2[i] = word_list2[i][0:3:1]
# # print(word_list2)

# # values = [2,3,4]
# # prod = 1 
# # for val in vlaues: 
# #     prod = pod * val 
# # print (prod)










# # maze = ["m","_","_","_","_","c","_","c"]
# # #        0   1   2   3   4   5   6   7
# # for i in range(0,len(maze),1):
# #     #print(i,maze[i]) 
# #     if maze[i] == "c":
# #         loc = i
# #         break
# # print(loc) 



# # OR 

# # maze = ["m","_","_","_","_","c","_","c"]
# # #        0   1   2   3   4   5   6   7
# # cheese_locs = []
# # for i in range(0,len(maze),1):
# #     #print(i,maze[i]) 
# #     if maze[i] == "c":
# #         cheese_locs.append(i)
# # print(cheese_locs)  

# # for i in values:
# #     if word[0] == "a","e", "i", "o", "u":


# # vowels = ["a","e","i","o","u"]
# # #if word start with a vowel, add yay 
# # if word [0] in vowels: 
# #     word = word + "yay"
# # else: 
# #     #finding index location of first vowel 
# #     for i in range (0,len(values),1):
# #     for i in range(0,len(word),1):
# #         if word[i] in vowels:
# #             loc = i 






























# # word = "cool"
# # #       012345678
# # vowels = ["a","e","i","o","u"]
# # #if word starts with vowel, add yay
# # if word[0] in vowels:
# #     word = word + "yay"
# # else:
# #     #finding index location of first vowel
# #     for i in range(0,len(word),1):
# #         if word[i] in vowels:
# #             loc = i
# #             break
# #     #Slicing word into parts
# #     red_part = word[0:loc:1]
# #     green_part = word[loc: :1]
# #     #Recombining into pig latin word
# #     word = green_part + red_part + "ay"
# # print(word) 




# # word = "scratch"
# # vowels = ["a","e","i","o","u"]
# # #finding index location of first vowel
# # for i in range(0,len(word),1):
# #     if word[i] in vowels:
# #         loc = i
# #         break
# # #if first vowel is at beginning, add "yay
# # if loc == 0:
# #     word = word + "yay"
# # else:
# #     red_part = word[0:loc:1]
# #     green_part = word[loc::1]
# #     word = green_part + red_part + "ay"
# # print(word) 





































# # values = [3,62,7,8,3]
# # total = 0 
# # for i in values:
# #     if i == 3:
# #         total = total + 1 
# #         # total += 1
# # print(total)



# grades = [93,87,65,76,95,100]
# total = 0 
# for i in grades: 
#     if i >= 90:
#         total = total + 1 
# print("there are", total, "A's")


# scores = [93,87,65,76,95,100]
# grades = [] 
# for i in scores: 
#     if i >= 90: 
#         grades.append("A")
#     elif i <= 90 and i >= 80: 
#         grades.append("B")
#     elif i < 80: 
#         grades.append("C")
#     elif i < 70: 
#         grades.append("D")
# print(grades)



# word = "scratch"
# vowels = ["a","e","i","o","u"]
# #finding index location of first vowel
# for i in range(0,len(word),1):
#     if word[i] in vowels:
#         loc = i
#         break
# #if first vowel is at beginning, add "yay
# if loc == 0:
#     word = word + "yay"
# else:
#     red_part = word[0:loc:1]
#     green_part = word[loc::1]
#     word = green_part + red_part + "ay"
# print(word) 




# # On Friday, the kids in Mrs. Conda's class split into two teams
# # to play a word game against each other!
# # Children whose names start with a letter A through M go in one
# #group, and those whose names start with N-Z go in another.
# #It just so happens that this splits the class evenly!
# # Given a list of names:
# #example list:
# name_list = ["Olivia","Andrew","Bob","Rebecca","Amy","Xavier"]
# # you need to get 2 separate lists that represent the two teams!
# #example output:
# print(am_team) #>>> ["Andrew","Bob","Amy"]
# print(nz_team) #>>> ["Olivia","Rebecca","Xavier"] 





# import string
# string.ascii_uppercase




# #bonus -- 
# # The students got tired of being on the same teams every time!
# # Mrs. Conda then implemented a script that would pick
# # random teams with a size difference of no more than 1 member!
# # Write a script like this!
# #import random
# #help(random.shuffle)









