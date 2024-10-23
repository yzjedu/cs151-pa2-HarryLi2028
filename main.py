# Output an intro of the program 
print('Welecome to the game of sticks, In this game there will be 3 players including you, your friend and the computer.')
print('The goal of this game is to not be the one to take the last stick!')

# Import random module
import random 

# Create variables 
player_1 = 0
player_2 = 0
player_3 = 0
repeat = str('yes')

# Create a while loop to repeat when the user wants to play again
while repeat == 'yes':
    total_sticks = random.randint(10,100)
    while total_sticks > 0:
        if total_sticks > 0:
            choice_1 = int(input('Player 1 choose a number between 1 and 3:'))
            while choice_1 <= 0 and choice_1 >= 4:
                choice_1 = int(input('Player 1, choose a valid number between 1 and 3:'))
            total_sticks -= choice_1
            if total_sticks <= 0:
                player_1 += 1
                print('player one has taken the last stick.')
        if total_sticks > 0:
            choice_2 = int(input('Player 2 choose a number between 1 and 3:'))
            while choice_2 <= 0 and choice_2 >= 4:
                choice_2 = int(input('Player 2, choose a valid number between 1 and 3:'))
            total_sticks -= choice_2
            if total_sticks <= 0: 
                player_2 += 1
                print('player 2 has taken the last stick')
        if total_sticks > 0:
            choice_3 = random.randint(1,3)
            total_sticks -= choice_3
            if total_sticks <= 0:
                player_3 += 1
                print('Player 3 has taken the last stick')
    if total_sticks < 0:
        repeat = str(input('Do you want to play again:'))
        while repeat != 'no' and repeat != 'yes':
            repeat = str(input('Please enter yes or no:'))
            repeat = repeat.lower()
        if repeat == 'no':
            print('Thanks for playing!')
            
