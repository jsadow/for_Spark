# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

# initialize global variables used in your code here

secret_number = random.randint(0,100)
remaining_guesses = 7
game_type = 100


guess = 'sth'
    
# helper function to start and restart the game
def new_game():
    global game_type, remaining_guesses

    if game_type == 100:
        remaining_guesses = 7
      
        print 'New game 0 - 100 Remaing guesses', remaining_guesses, '\n'
 
    elif game_type == 1000:
        remaining_guesses = 10
       
        print 'New game 0 - 1000 Remaing guesses', remaining_guesses, '\n'

    else:
        print 'sth is wrong'
        



# define event handlers for control panel
def range100():
    global secret_number, game_type
    game_type = 100
    secret_number = random.randint(0,100)
    new_game()

def range1000():
    global secret_number, game_type
    game_type = 1000
    secret_number = random.randint(0,1000)
    new_game()
    
    
def input_guess(guess):
    global secret_number, remaining_guesses
    remaining_guesses = remaining_guesses - 1
    
    if secret_number > int(guess) and remaining_guesses > 0:
        print 'Guess was',guess,'\nSecret number is higher'
        print 'Remaining guesses ', remaining_guesses, "\n"
    
    elif secret_number < int(guess) and remaining_guesses > 0:
        print 'Guess was',guess,'\nSecret number is lower'
        print 'Remaining guesses ', remaining_guesses, "\n"
    
    elif secret_number == int(guess) and remaining_guesses >= 0:
        print "Correct - you win! The secret number is ", secret_number, "\n"
    
    elif remaining_guesses == 0:
        print 'You lose \n'
        new_game()
    
    else:
        print 'something iswrong number'
   
    
    # main game logic goes here	
    
    # remove this when you add your code
    

    
# create frame

frame = simplegui.create_frame("Game",200,200,500)
frame.add_button('Random number 1 - 100', range100,200)
frame.add_button('Random number 1 - 1000', range1000,200)
frame.add_input('Guess',input_guess, 100)


# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
