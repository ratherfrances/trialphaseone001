#count the numbers of numbers in a list 
def count(values):
    counter = 0
    for i in values:
        if i == 2:
            counter += 1
    return counter
some_list = [7,7,2,4,2,2,2,2]
how_many = count(some_list)
print(how_many) 