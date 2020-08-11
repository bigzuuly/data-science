'''
Created on Nov 29, 2016

@author: ThomasC
'''

import re
import random
from collections import Counter
from collections import defaultdict
from functools import partial
from functools import reduce


my_regex = re.compile("[0-9]+", re.I)


for i in [1,2,3,4,5]:
    print (i)
    
    for j in [1,2,3,4,5]:
        print (j)
        print (i+j)
        
print ("Done")

print (Counter([1,2,3,4,5]))


print (5/2)
print (5//2)


def double(x = 0):
    """ multiplies input by 2 """
    return x * 2

def apply_to_one(f):
    """takes function as an argument"""
    return f(1)


print ("\n\n")
print (apply_to_one(double))


print (apply_to_one(lambda x: x+4))

print (r"\t")

multiline_string = """this is a bunch of lines with double quotes \"
second line here"""

print (multiline_string)

integer_list = [1,2,3]
hetero_list = ["string", 1, 2.43]
list_of_lists = [integer_list, hetero_list, []]

print (len(integer_list))
print (sum(integer_list))

x = list(range(10))

print(x[1])

print(x[:3])
print(x[1:5])
print(x[3:])

print (x[:])

print (-1 in x)

x.extend([10,11])

print (x[:])

print (x + [12,13])
print (x[:])

a, b, c = integer_list

print(b)

def sum_and_product(x,y):
    return (x+y), (x*y)

s, p = sum_and_product(5, 10)

print (s, p)

s,p = p, s

print (s, p)

print ("\n\n")

grades = {"Joel": 80, "Tim": 95}

print(grades["Joel"])

print ("Kate" in grades)

grades["Kate"] = 100

print ("Kate" in grades)
print (len(grades))

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags" : ["#data", "#science", "#science", "#awesome", "#yolo"]
    }


print ("#data" in tweet["hashtags"])

print (tweet.values())
print (tweet.keys())

print ("user" in tweet)

print ("\n\n")

dd_pair = defaultdict(lambda: [0,0])
dd_pair[2][0] = 3
dd_pair[2][1] = 1
print ("dd_pair", dd_pair)
#dd_pair["2"][1] = 1

print (dd_pair)

document = "Match 1 game 1, is there any merit to chumping with the goyf instead of 1 of the lingering soul tokens? That leaves you with 3 lethal power in fliers, while also eliminating your opponent's out of playing a chump blocker for your goyf. All their removal is burn based so if they had any you were dead regardless.".split()

document_counter = Counter(document)

for word, c in document_counter.most_common(10):
    print (word, c)

s = set()
s.add(1)
s.add(2)
s.add(2)

print (s)
print (3 in s)

print ("\n\n")
x = None
print (x, "is None")

print (all([]))
print (any([]))

print (sorted(document, key=lambda word: document_counter.get(word), reverse=True))

even_numbers = [x for x in range(10) if x % 2 ==0]

print (even_numbers)
print (x*x for x in even_numbers)

for i in range(10):
    """lazy version"""
    print (i)
    
    

print ("\n\n")

four_uniform_randoms = [random.random() for _ in range(4)]
print (four_uniform_randoms)



print (random.randrange(3,6))

names = ["Alice", "Thomas", "Tim", "Brad", "Cindy"]
random.shuffle(names)

print (names)

print (random.sample(names, 2))

four_with_replacement = [random.choice(names) for _ in range(4)]
print (four_with_replacement)


print ("\n\n")

def exp(base,power):
    return base ** power

two_to_the_power = partial(exp, 2)

print (two_to_the_power(10))

square_of = partial(exp, power=2)
print (square_of(3))

print ("\n\n")

xs = [1,2,3,4]
print (double(x) for x in xs)
print (map(double, xs))

def multiply(x,y):
    return x * y

print (map(multiply, [1,2], [4,10]))

def is_even(x):
    return x % 2 == 0

print (x for x in xs if is_even(x))
print (*filter(is_even, xs), sep=" ")

print (reduce(multiply, xs))

for i,name in enumerate(names):
    print (i, name)
    
print ("\n\n")

list1 = ['a','b','c']
list2 = [1,2,3]

print (*zip(list1, list2), sep=" ")
print (*zip(*zip(list1, list2)), sep=" ")

print ("\n\n")

def doubler(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g
    
def f1(x):
    return x + 1

g = doubler(f1)

print (g(3))
print (g(-1))

def f2(x,y):
    return x + y

g = doubler(f2)

print (g(3,2))


