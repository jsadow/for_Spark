# template for "Stopwatch: The Game"

import simplegui

# define global variables

time = 0
interval = 100
attempts = 0
success = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
    
def format(time):
    ds = time % 10
    
    seconds = (time - ds)/10
 
    s = seconds % 60
    m = (seconds - s) / 60
    
    if s < 10:
        s = '0' + str(s)
        
    return str(m) + ':' + str(s) + '.' + str(ds)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()
    
def stop():
    global success, attempts
    if time %10 == 0 and time != 0 and timer.is_running() == True:
        success += 1
        attempts += 1
        timer.stop()
    elif time %10 != 0 and time != 0 and timer.is_running() == True:
        attempts += 1
        timer.stop()        
    
def reset():
    global time, success, attempts
    timer.stop()
    time, success, attempts = 0, 0, 0

# define event handler for timer with 0.1 sec interval

def timer_handler():
    global time
    time += 1

timer = simplegui.create_timer(interval, timer_handler)


# define draw handler

def draw(canvas):
    canvas.draw_text(format(time),[100, 100], 40, "White")
    canvas.draw_text(str(success)+'/'+str(attempts),[200, 50], 30, "Green")
  
    
# create frame

frame = simplegui.create_frame("Home", 300, 150)


timer = simplegui.create_timer(interval, timer_handler)


# register event handlers

frame.set_draw_handler(draw)

frame.add_button("start", start, 75)
frame.add_button("stop", stop, 75)
frame.add_button("reset", reset, 75)




# start frame
frame.start()

# Please remember to review the grading rubric
