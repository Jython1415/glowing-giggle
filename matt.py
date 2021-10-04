import math
import random
from math import gcd

# a math function you can ignore
# returns the lowest common multiple of an array of integers
# I use it later in the program for cool math
def lcm(array):
    result = 1
    for i in array:
        result = result*i//gcd(result, i)

    return result

# define what an item is (or whatever you're distributing)
class Item:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity # rarity will be like, 1/rarity chance of getting this item
        # add other properties here

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_rarity(self):
        return self.rarity

    def set_rarity(self, rarity):
        self.rarity = rarity


# making the items  
item1 = Item("super cool sword", 1000)
item2 = Item("idk, kinda boring", 10)

# list of items
items = [item1, item2]

# function for making the list of items into a list based on their relative rarity

def make_distribution_array(list_of_items):
    # first, figure out how much rare stuff you have
    total_rarity = 0
    list_of_rarities = []
    for i in list_of_items:
        total_rarity += i.get_rarity()
        list_of_rarities.append(i.get_rarity())
    
    # you need to make sure you have like, even numbers so I'm multiplying everything to get the least common multiple
    list_of_rarities.append(total_rarity)
    # big number is the lowest common multiple of all the important numbers we're working with here
    big_number = lcm(list_of_rarities)

    # now make the final array based on all this
    result_array = []
    for i in list_of_items:
        for j in range(int(big_number / i.get_rarity())):
            result_array.append(i)
    
    return result_array

# you'll have to call this function each time you want to make a new combination of rarities
# so like, if you add an items or change anything at all about the relative frequency of prizes, you have to call the function again
dist_array = make_distribution_array(items)

# draw something from the prize pool!
# the number is how many random items you want
prize = random.sample(dist_array, 5)

# now you can print out your prize
for i in prize:
    print(i.get_name())


# now do this 5 times to see if you get anything interesting
for i in range(5):
    prize = random.sample(dist_array, 100)
    for i in prize:
        print((i.get_name()))

    print("\n")

# if you want to change how rare something is, make sure you make a new dist. array afterwards
item1.set_rarity(100)

dist_array = make_distribution_array(items)

prize = random.sample(dist_array, 100)
for i in prize:
    print((i.get_name()))