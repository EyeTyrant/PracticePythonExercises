# Exercise 6 String Lists alt

a = input('Enter a palindrome: ').lower()
a = a.replace(' ', '')

if a == a[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')
