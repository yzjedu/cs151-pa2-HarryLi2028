# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 
 1. Set player_1 to 0
 2. Set player_2 to 0
 3. Set player_3 to 0
 4. Store yes into repeat 
 5. While repeat equals yes
    1. Set total_sticks to a random number from 10 to 100
    1. While total_sticks are more than 0 
      1. If total_sticks are more than 0
          1. Prompt player 1 to input a value from 1 to 3
          1. subtract the input of player 1 from total_sticks
          1. If total_stiks is less than or equal to 0
              1. add 1 to player_1 
      1. If total_sticks are more than 0
          1. Prompt player 2 to input a value from 1 to 3
          1. subtract the input of player 2 from total_sticks
          1. If total_sticks is less than or equal to 0
              1. add 1 to player_2
      1. If total_sticks are more than 0
          1. choose a random number from 1 to 3 for player 3
          1. subtract the random number generated from total_sticks
          1. If total_sticks is less than or equal to 0
              1. add 1 to player_3
    1. Output the losses of player_1, player_2, player_3
    1. Prompt user to input yes or no if they want to play again
    1. While user does not input yes or no 
       1. Prompt user to input a valid input between yes or no
    1. Set repeat to user input
    1. Set repeat to lowercase
    1. If repeat equals no 
        1.  output 'thanks for playing!'0
