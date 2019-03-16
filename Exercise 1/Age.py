# Exercise 1 Character Input

import datetime

name = input('What is your name? ')
age = input('What is your age? ')
new_age = int(age)
x = datetime.datetime.now()
new_year = (x.year)
future = new_year - new_age + 100
message = ('Hello ' + name +
           ' your 100th birthday will occur in the year ' + str(future) + '!\n')
print(message)

# Extras


def getNumber():
    number = int(input('Enter a number between 1 and 10: '))
    if number > 10:
        print('Number entered must be less than 11')
        getNumber()
    else:
        print(message * number)


getNumber()
