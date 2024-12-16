import DrawingPanel
c = DrawingPanel.DrawingPanel(800,600)

#background
def background():
    c.draw_rect(0,0,800,600,)
    c.fill_rect(0,0,800,600,"light blue")

#ground
c.draw_rect(0,400,800,200)
c.fill_rect(0,400,800,600,"dark green")

#car
def car_drawing():
    c.draw_rect(50,375,60,20)
    c.fill_rect(50,375,60,20,"red")

#sun
c.draw_oval(600,80,60,60)
c.fill_oval(600,80,60,60,"yellow")

#cloud
c.fill_oval(100,100,100,100,"white")
c.fill_oval(150,70,100,100,"white")
c.fill_oval(180,100,100,100,"white")

#cloud 2
c.fill_oval(400,200,60,60,"white")
c.fill_oval(460,200,60,60,"white")
c.fill_polygon(400,230,520,230,460,320,"white")

#car move
for i in range(0,100,10):
    car_drawing(i,400)
    car.sleep(30)
    background()

car_drawing()



