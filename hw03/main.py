import turtle as t
import math
 
def draw_FiveStars(t=None, start_pos=(0,0), end_pos=(0,10), radius=100, color=None):
    size = radius * math.sin(math.pi/5)/math.sin(math.pi*2/5)
    t.left(math.degrees(math.atan2(end_pos[1]-start_pos[1], end_pos[0]-start_pos[0])))
    t.penup()
    t.goto(start_pos)
    t.fd(radius)
    t.pendown()
    t.right(math.degrees(math.pi*9/10))
    if color:
        t.begin_fill()
        t.fillcolor('yellow')
    for i in range(5):
        t.fd(size)
        t.left(360/5)
        t.fd(size)
        t.right(2*360/5)
    if color:
        t.end_fill()
 
def draw_FiveStarsFlag(times=20):
    width, height = 30*times, 20*times
    window = t.Screen()
    t.hideturtle()
    t.speed(90)
    t.color('red')
    t.penup()
    t.goto(-width/2, height/2)
    t.pendown()
    t.begin_fill()
    t.fillcolor('red')
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.right(90)
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.right(90)    
    t.end_fill()
    draw_FiveStars(t, start_pos=(-10*times, 5*times), end_pos=(-10*times, 8*times), radius=3*times, color='yellow')  
    stars_start_pos = [(-5, 8), (-3, 6), (-3, 3), (-5, 1)]
    for pos in stars_start_pos:
        draw_FiveStars(t, start_pos=(pos[0]*times, pos[1]*times), end_pos=(-10*times, 5*times), radius=1*times, color='yellow')  
    window.exitonclick()
 
if __name__ == '__main__':
        draw_FiveStarsFlag()

