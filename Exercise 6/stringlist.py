# Exercise 6 String Lists

a = input('Enter a palindrome: ').lower()
a = a.replace(' ', '')
letters = []

for c in a:
    letters.append(c)

print(letters)

for i in letters:         # This is flawed somehow and does not print through all of the iterations
    if letters[0] == letters[-1]:
        letters.pop(0)
        letters.pop()
    else:
        print('not a palindrome')
    print('palindrome')
