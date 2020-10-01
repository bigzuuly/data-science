'''
Created on Oct 01, 2020

@author: ThomasC
'''
import random

def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()

    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print ("P(both):", both_girls)
print ("P(older):", older_girl)
print ("P(either):", either_girl)

print ("P(both | older):", both_girls / older_girl)
print ("P(both | either):", both_girls / either_girl)

