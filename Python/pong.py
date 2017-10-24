# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# variable hit increase speed of the ball
hit = 0 

print random.choice([1, 2, 3, 4, 5, 6])

paddle1_pos = [(0+HEIGHT)/2-PAD_HEIGHT/2, PAD_HEIGHT/2 +(HEIGHT)/2]

paddle2_pos = [(0+HEIGHT)/2-PAD_HEIGHT/2, PAD_HEIGHT/2 +(HEIGHT)/2]

score1 = 0

score2 = 0


paddle1_vel = [0,0]

paddle2_vel = [0,0]




# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as 
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    #ball_vel = [-2, 0]
    

    if direction == True:
        ball_vel = [random.randrange(4, 6)/4, random.choice([-1,1]) * random.randrange(3, 9)/4]
    else:
        ball_vel = [-random.randrange(4, 6)/4, random.choice([-1,1]) * random.randrange(4, 9)/4]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos  # these are numbers
    global score1, score2  # these are ints
    global ball_vel
    global hit
    
    hit = 0
    
    
    
    score1, score2 = 0,0
    
    paddle1_pos = [(0+HEIGHT)/2-PAD_HEIGHT/2, PAD_HEIGHT/2 +(HEIGHT)/2]

    paddle2_pos = [(0+HEIGHT)/2-PAD_HEIGHT/2, PAD_HEIGHT/2 +(HEIGHT)/2]
    
    ball_pos = [WIDTH/2,HEIGHT/2]
    
    random_number = random.randint(0,1)
    
    spawn_ball(random_number)
    
    '''
    if random_number == 1:
        ball_vel = [random.randrange(4, 6)/2, random.randrange(3, 9)/4]
    elif random_number == 0:
        ball_vel = [- random.randrange(4, 6)/2, - random.randrange(3, 9)/4]
     '''   

    
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, LEFT, RIGHT
    
    global paddle1_vel, paddle2_vel
    
    global hit
    
    #increase speed
    
    ball_vel[0] = (1.0 + hit * 0.0001) * ball_vel[0]
    ball_vel[1] = (1.0 + hit * 0.0001) * ball_vel[1]
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
       

    # update ball
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] <= BALL_RADIUS and ball_pos[1] >= paddle1_pos[0] and ball_pos[1] <= paddle1_pos[1]:
        ball_vel[0] = -ball_vel[0]
        hit += 1
    
    elif ball_pos[0] >= WIDTH - BALL_RADIUS and ball_pos[1] >= paddle2_pos[0] and ball_pos[1] <= paddle2_pos[1]:
        ball_vel[0] = -ball_vel[0]
        hit +=1
        
    elif ball_pos[0] <= BALL_RADIUS:
        spawn_ball(True)
        score2 += 1
        hit = 0


    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        spawn_ball(False)
        score1 += 1
        hit = 0
        
        
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
            
    # draw ball
    
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")        
    
    # update paddle's vertical position, keep paddle on the screen
    
    
    
    # draw paddles
    
    canvas.draw_line([PAD_WIDTH/2, paddle1_pos[0]], [PAD_WIDTH/2, paddle1_pos[1]], PAD_WIDTH, "Red")
    canvas.draw_line([WIDTH - PAD_WIDTH/2, paddle2_pos[0]], [WIDTH -PAD_WIDTH/2, paddle2_pos[1]], PAD_WIDTH, "White")
    
    if paddle1_pos[1] > HEIGHT:
        paddle1_pos[0] = HEIGHT - PAD_HEIGHT
        paddle1_pos[1] = HEIGHT
    if paddle1_pos[0] < 0:
        paddle1_pos[0] = 0
        paddle1_pos[1] = 0 + PAD_HEIGHT   
    if paddle2_pos[1] > HEIGHT:
        paddle2_pos[0] = HEIGHT - PAD_HEIGHT
        paddle2_pos[1] = HEIGHT
    if paddle2_pos[0] < 0:
        paddle2_pos[0] = 0
        paddle2_pos[1] = 0 + PAD_HEIGHT
       
    paddle2_pos[0] += paddle2_vel[1]
    paddle2_pos[1] += paddle2_vel[1]
    paddle1_pos[0] += paddle1_vel[1]
    paddle1_pos[1] += paddle1_vel[1]
    '''   
    elif paddle2_pos[0] >= 0:
        paddle2_vel[1] = 0
        
    elif paddle1_pos[1] >= HEIGHT:
        paddle1_vel[1] = 0
        
    elif paddle1_pos[0] <= 0:
        paddle1_vel[1] = 0
     '''   
        

    
   

    
    # determine whether paddle and ball collide    
    
    # draw scores
    
    canvas.draw_text(str(score1),[WIDTH/4, 100], 50, "White")
    canvas.draw_text(str(score2),[3*WIDTH/4, 100], 50, "White")
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    global paddle1_pos, paddle2_pos
    

        
    
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += 3
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= 3
        
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += 3
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= 3
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
        
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button("restart", new_game, 75)


# start frame
new_game()
frame.start()

spawn_ball(True)
