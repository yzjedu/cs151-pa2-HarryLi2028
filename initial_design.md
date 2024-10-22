# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 
# 1) Set player_1 to 0
# 2) Set player_2 to 0
# 3) Set player_3 to 0
# 4) Store yes into repeat 
# 5) While repeat equals yes
#		A) Set total_sticks to a random number from 10 to 100
#		B) While total_sticks are more than 0 
#      		A) If total_sticks are more than 0
#				a) Prompt player 1 to input a value from 1 to 3
#				b) subtract the input of player 1 from total_sticks
#				c) If total_stiks is less than or equal to 0
#					a) add 1 to player_1 
#      		B) If total_sticks are more than 0
#				a) Prompt player 2 to input a value from 1 to 3
#				b) subtract the input of player 2 from total_sticks
#				c) If total_sticks is less than or equal to 0
#					a) add 1 to player_2
#      		C) If total_sticks are more than 0
#				a) choose a random number from 1 to 3 for player 3
#				b) subtract the random number generated from total_sticks
#				c) If total_sticks is less than or equal to 0
#					a) add 1 to player_3
#		C) Output the losses of player_1, player_2, player_3
#		D) Prompt user to input yes or no if they want to play again
# 		E) While user does not input yes or no 
#			A) Prompt user to input a valid input between yes or no
# 		F) Set repeat to user input
# 		G) Set repeat to lowercase
# 		H) If repeat equals no 
#			A) output 'thanks for playing!'0


import random 

player_1 = 0
player_2 = 0
player_3 = 0
repeat = str(yes)

while repeat == yes:
    total_sticks = random.randint(10,100)
    while total_sticks > 0:
        if total_sticks > 0:
            choice_1 = int(input('Choose a number between 1 and 3:'))
            while choice_1 < 1 and choice_1 > 3:
                choice_1 = int(input('Choose a number between 1 and 3:'))
            total_sticks -= choice_1
            if total_sticks <= 0:
                player_1 += 1
                print('player one has taken the last stick.')
        if total_sticks > 0:
            choice_2 = int(input('Choose a number between 1 and 3:'))
            while choice_2 < 1 and choice_2 > 3:
                choice_2 = int(input('Choose a number between 1 and 3:'))
            total_sticks -= choice_2