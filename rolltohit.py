#This simulates rolling to hit in Warhammer 40,000
#Prompt the user how many dice are being rolled, and what the hit target is
#Roll the correct number of dice, then display the results
#This is a guided practice. Either follow with the video or your instructor will
#go over this in class.

import random

random.randint(1,6)
num_dice = int(input("How many d6s are you rolling?: "))
hit_target = int(input("And what number to hit?: "))
total = 0

for i in range(1, num_dice + 1):
    roll = random.randint(1,6)
    total = roll + total
    
if total >= hit_target:
    print(str(total) + " You Hit!")
else:
    print(str(total) + " You Miss!")