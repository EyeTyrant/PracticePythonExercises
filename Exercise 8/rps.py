# Exercise 8 Rock Paper Scissors

weps = ['rock', 'paper', 'scissors']
# Get player 1 weapon and validate
p1Weapon = input(
    'Player 1: Enter weapon type Rock, Paper, or Scissors: ').lower()
restart = True
while restart == True:
    for w in weps:
        if p1Weapon == w:
            restart = False
            break
    if not restart:
        break
    else:
        print('Please choose a valid weapon')
        p1Weapon = input(
            'Player 1: Enter weapon type Rock, Paper, or Scissors: ').lower()
# Get player 2 weapon and validate
p2Weapon = input(
    'Player 2: Enter weapon type Rock, Paper, or Scissors: ').lower()
restart2 = True
while restart2 == True:
    for w in weps:
        if p2Weapon == w:
            restart2 = False
            break
    if not restart2:
        break
    else:
        print('Please choose a valid weapon')
        p2Weapon = input(
            'Player 2: Enter weapon type Rock, Paper, or Scissors: ').lower()
# Compare player weapon choices and declare outcome
while p1Weapon == 'rock':
    if p2Weapon == 'paper':
        print('Player 2 wins with Paper!')
        break
    elif p2Weapon == 'rock':
        print('The battle is a Draw!')
        break
    else:
        print('Player 1 wins with Rock!')
    break

while p1Weapon == 'paper':
    if p2Weapon == 'rock':
        print('Player 1 wins with Paper!')
        break
    elif p2Weapon == 'paper':
        print('The battle is a Draw!')
        break
    else:
        print('Player 2 wins with Scissors!')
    break

while p1Weapon == 'scissors':
    if p2Weapon == 'paper':
        print('Player 1 wins with Scissors!')
        break
    elif p2Weapon == 'scissors':
        print('The battle is a Draw!')
        break
    else:
        print('Player 2 wins with Rock!')
    break
# Reveal player weapon choices
print('Player 1 chose: ' + p1Weapon.capitalize() +
      '\n' + 'Player 2 chose: ' + p2Weapon.capitalize())

# Verbose but fits the concepts for the lesson (While loops, Infinite loops, and Break statements).
# Maybe I'll try again later with functions...
