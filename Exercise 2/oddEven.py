# Exercise 2 Odd or Even

number = int(input('Enter a number: '))
if number % 4 == 0:
    print('Your number is EVEN and a multiple of 4!')  # Extra 1
elif number % 2 == 0:
    print('Your number is EVEN!')
else:
    print('Your number is ODD!')
