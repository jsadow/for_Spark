import random

def name_to_number(name):
    if name=="rock":
        number=0
    elif name=="Spock": number=1
    elif name=="paper": number=2
    elif name=="lizard": number=3
    elif name=="scissors": number=4
    else: number="inapropriate_name"
    return number

    
def number_to_name(number):
    if number==0: 
        name="rock"
    elif number==1: 
        name="Spock"
    elif number==2: 
        name="paper"
    elif number==3: 
        name = "lizard"
    elif number==4: 
        name = "scissors"
    else: 
        name="inapropriate_number"
    return name
    

def rpsls(player_choice): 
    print ""
    print "Player chose " + player_choice
    
    computer_number = random.randrange(0,5)
    
    print "Computer chose " + number_to_name(computer_number)
    
    player_number = name_to_number(player_choice)
    
    difference = player_number - computer_number
    modulo_difference = (5 + difference)%5
    
    
    if modulo_difference == 1 or modulo_difference == 2 :
        result = "Player win! :)"
    elif modulo_difference == 3 or modulo_difference == 4:
        result = "Computer win! :("
    elif modulo_difference == 0:
        result = "Draw!"
    else:
        result = "blad"
   
    print result 

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


