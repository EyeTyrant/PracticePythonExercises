# Exercise 2 Odd or Even
# Extra 2

num = float(input('Enter a number: '))
check = float(input('Enter another number: '))
if num % check == 0:
    print('Your number divides evenly ' + str(num / check) + ' times!')
else:
    print('You have a remainder of ' + str(num % check))
