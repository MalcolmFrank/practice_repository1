def x2_minus3x_plus4(x):
    #should return value of y for the given x in x^2-3x+4
    y=x**2-3*x+4
    return y
    
#generalize to quad (a,b,c,x) and still returns y
def quad(a,b,c,x):
    return (a * (x ** 2)) + (b * x) + c

#make turtle draw out a linear approximation
import turtle as bob
world = bob.Screen()
world.screensize(50,50)

bob.shape('turtle')
def x_and_y_axis():
    bob.teleport(0,0)
    bob.shape('turtle')
    bob.color('black')
    bob.penup()
    bob.right(180)
    bob.forward(375)
    bob.right(180)
    bob.pendown()
    bob.forward(750)
    bob.penup()
    bob.right(180)
    bob.forward(375)
    bob.right(90)
    bob.forward(375)
    bob.right(180)
    bob.pendown()
    bob.forward(750)

x_and_y_axis()
bob.color('red')
bob.teleport(0,x2_minus3x_plus4(0))
for i in range(1,30):
    bob.goto(i,x2_minus3x_plus4(i))
print(x2_minus3x_plus4(0))
print(quad(1,-3,4,0))
