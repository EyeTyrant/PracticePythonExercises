# Exercise 4 Divisors

num = int(input("Enter a number between 1 and 1,000,000: "))
divisors = range(1, num + 1)
yourDivisors = []

if num % 2 == 0:
    for n in divisors:
        if num % n == 0:
            yourDivisors.append(n)
    print(yourDivisors)
else:
    print("Your number has no divisor!")
