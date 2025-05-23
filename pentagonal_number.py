'''Write a function that takes a positive integer num and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.
In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. On the third, there are 16 dots, and on the fourth there are 31 dots.
alt text
Return the number of dots that exist in the whole pentagon on the Nth iteration.
Examples
pentagonal(1) ➞ 1
pentagonal(2) ➞ 6
pentagonal(3) ➞ 16
pentagonal(8) ➞ 141'''
def pentagonal(num):
    pikat = 1
    for i in range(num):
        pikat += 5*i
    return pikat


print(pentagonal(1))