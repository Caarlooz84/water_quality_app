import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing speed
pen.width(2)

# Color setup
hue = 0  # Start hue (for rainbow effect)

# Draw a spiral flower
for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB
    pen.color(color)

    pen.forward(i * 0.5)
    pen.left(59)

    hue += 0.005  # Slight color shift

turtle.done()