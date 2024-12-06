import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
cat = turtle.Turtle()
cat.shape("turtle")
cat.speed(3)

# Function to draw a circle (for the cat's face)
def draw_circle(color, radius, x, y):
    cat.penup()
    cat.goto(x, y)
    cat.pendown()
    cat.begin_fill()
    cat.color(color)
    cat.circle(radius)
    cat.end_fill()

# Function to draw cat ears
def draw_ears(x, y):
    # Left ear
    cat.penup()
    cat.goto(x-40, y+80)
    cat.pendown()
    cat.begin_fill()
    cat.setheading(45)
    for _ in range(3):
        cat.forward(40)
        cat.right(120)
    cat.end_fill()

    # Right ear
    cat.penup()
    cat.goto(x+40, y+80)
    cat.pendown()
    cat.begin_fill()
    cat.setheading(135)
    for _ in range(3):
        cat.forward(40)
        cat.right(120)
    cat.end_fill()

# Draw face and body
draw_circle("gray", 80, 0, -20)

# Draw ears
draw_ears(0, 60)

# Draw eyes
draw_circle("white", 15, -30, 40)  # Left eye
draw_circle("white", 15, 30, 40)   # Right eye

# Draw pupils
draw_circle("black", 7, -30, 45)   # Left pupil
draw_circle("black", 7, 30, 45)    # Right pupil

# Draw nose
draw_circle("pink", 10, 0, 20)

# Draw mouth
cat.penup()
cat.goto(0, 20)
cat.pendown()
cat.setheading(-60)
cat.circle(15, 120)

# Draw whiskers
cat.penup()
cat.goto(-50, 10)
cat.setheading(0)
cat.pendown()
cat.forward(50)
cat.penup()
cat.goto(-50, 0)
cat.setheading(0)
cat.pendown()
cat.forward(50)
cat.penup()
cat.goto(-50, -10)
cat.setheading(0)
cat.pendown()
cat.forward(50)

cat.penup()
cat.goto(50, 10)
cat.setheading(180)
cat.pendown()
cat.forward(50)
cat.penup()
cat.goto(50, 0)
cat.setheading(180)
cat.pendown()
cat.forward(50)
cat.penup()
cat.goto(50, -10)
cat.setheading(180)
cat.pendown()
cat.forward(50)

# Hide the turtle and display the window
cat.hideturtle()
turtle.done()
