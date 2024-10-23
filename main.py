# Output an intro of the program 
print('Welcome to the game of sticks! In this game, there will be 3 players: you, your friend, and the computer.')
print('The goal of this game is to not be the one to take the last stick!')

# Import random module
import random 

# Create variables to track wins
player_1_loss = 0
player_2_loss = 0
player_3_loss = 0
repeat = 'yes'

# Create a while loop to repeat when the user wants to play again
while repeat == 'yes':
    # Randomly select a number of sticks between 10 and 100
    total_sticks = random.randint(10, 100)
    print(f'The game starts with {total_sticks} sticks.')
    
    while total_sticks > 0:
        # Player 1's turn
        choice_1 = int(input('Player 1, choose a number between 1 and 3: '))
        while choice_1 < 1 or choice_1 > 3:
            choice_1 = int(input('Player 1, choose a valid number between 1 and 3: '))
        total_sticks -= choice_1
        if total_sticks <= 0:
            player_1_loss += 1
            print('Player 1 has taken the last stick and lost the game!')
            break

        # Player 2's turn
        choice_2 = int(input('Player 2, choose a number between 1 and 3: '))
        while choice_2 < 1 or choice_2 > 3:
            choice_2 = int(input('Player 2, choose a valid number between 1 and 3: '))
        total_sticks -= choice_2
        if total_sticks <= 0:
            player_2_loss += 1
            print('Player 2 has taken the last stick and lost the game!')
            break

        # Player 3 (Computer)'s turn
        choice_3 = random.randint(1, 3)
        print(f'Player 3 (Computer) chooses: {choice_3}')
        total_sticks -= choice_3
        if total_sticks <= 0:
            player_3_loss += 1
            print('Player 3 (Computer) has taken the last stick and lost the game!')
            break

    # Ask if the players want to play again
    print('player 1 lost:',player_1_loss)
    print('player 2 lost:',player_2_loss)
    print('player 3 lost:',player_3_loss)
    repeat = input('Do you want to play again (yes or no)? ').lower()
    while repeat != 'no' and repeat != 'yes':
        repeat = input('Please enter yes or no: ').lower()

