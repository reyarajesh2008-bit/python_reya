
import turtle
import colorsys


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Polygon Spiral")


t = turtle.Turtle()
t.speed(6)       
t.width(3)        


sides = 6  
angle = 360 / sides + 1  # The "+ 1" creates the spiral twist effect


for i in range(120):
    
    color = colorsys.hsv_to_rgb(i / 120, 1.0, 1.0)
    t.pencolor(color)
    
    t.forward(i * 3)  
    t.right(angle)    


screen.exitonclick()
