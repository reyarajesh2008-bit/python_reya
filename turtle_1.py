import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Polygon Spiral")

# Set up the turtle
t = turtle.Turtle()
t.speed(6)        # Moderate speed so you can easily see the movement
t.width(3)        # Thicker lines to make the colors pop

# Change sides to change the shape (e.g., 3 = triangle, 4 = square, 6 = hexagon)
sides = 6  
angle = 360 / sides + 1  # The "+ 1" creates the spiral twist effect

# Draw the spiral polygon
for i in range(120):
    # Smooth rainbow color transition
    color = colorsys.hsv_to_rgb(i / 120, 1.0, 1.0)
    t.pencolor(color)
    
    t.forward(i * 3)  # Grows larger each step
    t.right(angle)    # Turns to form the polygon side

# Close the window when clicked
screen.exitonclick()
