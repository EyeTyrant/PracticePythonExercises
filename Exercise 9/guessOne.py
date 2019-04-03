# Exercise 9 Guessing Game One

# Import module
import random
# Get guess from player and store it in a variable
guess = int(input('Guess a number between 1 and 9: '))
# Generate random number and store it in a variable
number = random.randint(2, 8)
# Validate player guess
while guess <= 1 or guess >= 9:
    guess = int(
        input('That is NOT a number BETWEEN 1 and 9, guess again!!: '))
# Compare guess to number generated and display hint to player
if guess < number:
    print('Too low!')
elif guess > number:
    print('Too high!')
else:
    print('You win!')
# Display outcome
print('Your guess is ' + str(guess) +
      '. The correct number is ' + str(number) + '.')
