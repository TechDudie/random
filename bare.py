# This file is the bare version, everything is as short and there are no comments. Not recommended for beginners.
#---SENSITIVITY SETTINGS---
# These weights are what I have found that works best.
score_threshold=5
score_trigger=7
zero_trigger=17
one_trigger=20
#---SENSITIVITY SETTINGS---
import random
# num = 38563919364836273485827934683747283748362946584658264857384729485629475629485636287498385638294658374728019182084730719384659381628749484628637352761838452629573518385638293846338563936593846295758365
num=random.randint(int("1"+"0"*199),int("9"*200))
num=str(num)
num=''.join([char*2 for char in num])
num=num[1:-1]
num=[num[i:i + 2] for i in range(0,len(num),2)]
x=0
for i in num:
    num[x]=int(i)
    x+=1
freq=[]
for i in range(0,100):freq.append(0)
for i in num:freq[i-1]+=1
score = 0
for i in freq:
  if i>score_threshold:score+=i-score_threshold
zeros=0
ones=0
for i in freq:
    if i==0:zeros+=1
    if i==1:ones+=1
checks=0
if score>=score_trigger:checks+=1
if zeros>=zero_trigger:checks+=1
if ones<=one_trigger:checks+=1
if checks>=2:print("This number is not random.")
else:
    if score>=score_trigger:print("This number is probably not random.")
    else:print("This number is random.")
print("Data:")
print("Number: {}".format(num))
print("Frequency: {}".format(freq))
print("Score: {}".format(score))
print("Zeros: {}".format(zeros))
print("Ones: {}".format(ones))
print("Checks Passed: {}".format(checks))
print("Settings:")
print("Score Threshold: {}".format(score_threshold))
print("Score Trigger: {}".format(score_trigger))
print("Zero Trigger: {}".format(zero_trigger))
print("One Trigger: {}".format(one_trigger))
