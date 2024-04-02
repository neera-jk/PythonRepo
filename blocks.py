# a=2
# b=3
# if a>b:
#     print('A is greater')
# else:
#     print('B is greater')
#
# name = input('Please enter your name')
# age = input('Please enter you age')
# print('Hello {0}, welcome and your age is {1}'.format(name, age)



# day = "Saturday"
# temperature = 29
# raining = True
#
# if day == "Saturday" and temperature >=28 or not raining:
#     print('You can go out')
# else:
#     print('Stay at home')


import random
answer = random.randint(1,10)
print('Please guess a number from 1 to 10')
guess=0
while guess != answer:
    guess = int(input())
    if guess == answer:
        print('It is the right guess')
    elif guess<answer:
        print('Guess higher')
    else:
        print('Guess lower')



