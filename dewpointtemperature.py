#!/usr/bin/env python

num = input("Enter your input: ");
if num >= 75:
    print ("The temperature is %d, and I feel Extremely uncomrtable" % num)

if num >= 70 and num <= 74:
    print ("The temperature is %d, and I feel Extremely uncomrtable"% num)
    
if num >= 65 and num <= 69:
    print ("The temperature is %d, and I fell Somewhat uncomfortable" % num)
    
if num >= 60 and num <= 64:
    print ("The temperature is %d, and I fell OK" % num)
    
if num >= 50 and num <= 59:
    print ("The temperature is %d, and I fell Very comfortable" %  num)
    
if num <= 49:
    print ("The temperature is %d, and I fell A bit dry" % num)
    

    
