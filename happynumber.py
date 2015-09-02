
# Check if the number is happy or not
#
# 
# Created by: Dr.Akshay P
# Last modified: 08/31/15
# Copyright (c) 2015 Dr. Akshay P. All rights reserved.
# Please contact me at github for questions
#

def happy(num):
    """
    This fx returns whether the input int number is happy(true) or not(False).
    Happy numbers
 
 
    1 => Sum ( digits ^ 2 )  = 1
    1 => 1^2 = 1
 
    10 => 1^2 + 0^2 = 1
 
    68 => 6^2 + 8^2 = 100 => 1
 
    Unhappy numbers
    0 => 0^2 = 0
 
    4, 16, 37, 58, 89, 145, 42, 20, 4
    2, 4, ..., 4
 
    IsHappyNumber (number) => true if number is happy
    
    num: int; input number
    returns: True if number is happy, False if number is unhappy
    """
    sumSet=set()
    while 1:
        sum=adDigits(num)
        if (sum==1):
            return True
        elif (sum in sumSet):
            return False
        sumSet.add(sum)
        num=sum
            
def adDigits(num):
    """
    This fx returns the sum of each digit squared inside the num.
    
    num: int; input number
    returns: int; sum of digit(s)**2
    """
    sum=0
    div=0
    rem=0
    while (num>=10):
        div=num/10
        rem=num%10
        sum+=rem **2
        num=div
    sum+=num**2
    return sum        
