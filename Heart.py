import turtle

def draw_heart():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Perfect Red Heart")

    # Create a turtle object
    heart = turtle.Turtle()
    heart.speed(3)  # Set a medium speed for smoother drawing
    heart.color("red")
    heart.fillcolor("red")

    # Start filling the heart
    heart.begin_fill()

    # Move to the starting position
    heart.penup()
    heart.goto(0, -200)
    heart.pendown()

    # Draw the heart shape
    heart.left(50)
    heart.forward(133)
    heart.circle(50, 200)
    heart.right(140)
    heart.circle(50, 200)
    heart.forward(133)

    # End filling the heart
    heart.end_fill()

    # Hide the turtle and keep the window open
    heart.hideturtle()
    screen.mainloop()

# Call the function to draw the heart
draw_heart()
