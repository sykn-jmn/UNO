import math

def newX(x,distance,angle):
    newx = x - (distance*math.sin(math.radians(angle)))
    return newx

def newY(y,distance, angle):
    newy = y + (distance*math.cos(math.radians(angle)))
    return newy

class Drawer:
    def __init__(self,don):
        self.don=don

    def draw_number(self,x, y, number, width, height, angle):
        self.don.pencolor('white')
        self.don.penup()
        self.don.setpos(x, y)
        self.don.pendown()
        if number == 'logo':
            don = self.don
            don.forward (width)
            don.left(90)
            don.forward(height/3)
            don.left(90)
            don.forward(width)
            don.right(90)
            don.forward(height/3)
            don.right(90)
            don.forward(width)
            don.left(90)
            don.forward(height/3)
            don.left(90)
            don.forward(width)
            don.left(90)
            don.forward(height/3)
            don.left(90)
        if number == 'wild':
            self.don.fillcolor('yellow')
            self.drawRectangle(x, y, height / 2, width / 2, 0)
            self.don.fillcolor('green')
            self.drawRectangle(newX(x,width/2,angle-90), newY(y,width/2,angle-90), height / 2, width / 2, 0)
            #self.drawRectangle(x + (width / 2), y, height / 2, width / 2, 0)
            self.don.fillcolor('red')
            self.drawRectangle(newX(x, height / 2, angle), newY(y, height / 2, angle), height / 2, width / 2, 0)
            #self.drawRectangle(x, y + (height / 2), height / 2, width / 2, 0)
            self.don.fillcolor('blue')
            distance = math.sqrt(((width/2)*(width/2))+((height/2)*(height/2)))
            self.drawRectangle(newX(x, distance, angle - 27), newY(y, distance, angle-27), height / 2, width / 2, 0)
            #self.drawRectangle(x + (width / 2), y + (height / 2), height / 2, width / 2, 0)

        if number == 'wild4':
            self.draw_number(x, y, 4, width, height,angle)
            self.don.penup()
            self.don.setpos(x, y)
            self.don.forward(width / 2)
            self.don.left(90)
            self.don.forward(height * 3 / 4)
            self.don.right(90)
            self.don.pendown()
            self.don.right(90)
            self.don.forward(height / 2)
            self.don.left(90)
        if number == 'draw2':
            self.draw_number(x, y, 2, width, height,angle)
            self.don.penup()
            self.don.setpos(x,y)
            self.don.forward(width/2)
            self.don.left(90)
            self.don.forward(height*3/4)
            self.don.right(90)
            self.don.pendown()
            self.don.right(90)
            self.don.forward(height / 2)
            self.don.left(90)
        if number == 'reverse':
            distance = math.sqrt((width/6*width/6)+(height/6*height/6))
            angle2 = math.atan2(width/6,height/6)
            self.don.penup()
            self.don.setpos(newX(x,distance,angle+angle2), newY(y,distance,angle+angle2))
            self.don.pendown()
            self.don.left(90)
            self.don.forward(height * 4 / 5)
            self.don.left(90 + 45)
            self.don.forward(width / 2)
            self.don.backward(width / 2)
            self.don.left(90)
            self.don.forward(width / 2)
            self.don.left(45)
            self.don.penup()
            self.don.setpos(x,y)
            self.don.forward(width*5/6)
            self.don.left(90)
            self.don.forward(height*5/6)
            self.don.right(90)
            self.don.pendown()
            self.don.right(90)
            self.don.forward(height * 4 / 5)
            self.don.right(90 + 45)
            self.don.forward(width / 2)
            self.don.backward(width / 2)
            self.don.right(90)
            self.don.forward(width / 2)
            self.don.right(45)
        if number == 'skipped':
            self.draw_number(x, y, 0, width, height,angle)
            self.don.penup()
            self.don.setpos(x, y)
            self.don.pendown()
            distance = math.sqrt((height*height)+(width*width))
            self.don.setpos(newX(x,distance,angle-27),newY(y,distance,angle-27))
        if number == 0:
            self.draw_number(x, y, 7, width, height,angle)
            self.don.penup()
            self.don.setpos(x - ((height / 2) * math.sin(math.radians(angle))),y + ((height / 2) * math.cos(math.radians(angle))))
            self.don.pendown()
            self.don.right(90)
            self.don.forward(height / 2)
            self.don.left(90)
            self.don.forward(width)
        if number == 1:
            self.don.penup()
            self.don.forward(width)
            self.don.pendown()
            self.don.left(90)
            self.don.forward(height)
            self.don.right(90)
        if number == 2:
            self.don.forward(width)
            self.don.backward(width)
            self.don.left(90)
            self.don.forward(height / 2)
            self.don.right(90)
            self.don.forward(width)
            self.don.left(90)
            self.don.forward(height / 2)
            self.don.left(90)
            self.don.forward(width)
            self.don.left(180)
        if number == 3:
            self.don.forward(width)
            self.don.left(90)
            self.don.forward(height / 2)
            self.don.left(90)
            self.don.forward(width)
            self.don.left(180)
            self.don.forward(width)
            self.don.left(90)
            self.don.forward(height / 2)
            self.don.left(90)
            self.don.forward(width)
            self.don.left(180)
        if number == 4:
            self.draw_number(x, y, 1, width, height,angle)
            self.don.penup()
            self.don.setpos(x, y)
            self.don.left(90)
            self.don.forward(height)
            self.don.pendown()
            self.don.left(180)
            self.don.forward(height / 2)
            self.don.left(90)
            self.don.forward(width)
        if number == 5:
            self.don.forward(width)
            self.don.left(90)
            self.don.forward(height / 2)
            self.don.left(90)
            self.don.forward(width)
            self.don.right(90)
            self.don.forward(height / 2)
            self.don.right(90)
            self.don.forward(width)
        if number == 6:
            self.draw_number(x, y, 5, width, height,angle)
            self.don.left(90)
            self.don.penup()
            self.don.setpos(x, y)
            self.don.pendown()
            self.don.forward(height / 2)
            self.don.right(90)
        if number == 7:
            self.draw_number(x, y, 1, width, height,angle)
            self.don.penup()
            self.don.setpos(newX(x,height/2,angle),newY(y,height/2,angle))
            self.don.pendown()
            self.don.left(90)
            self.don.forward(height / 2)
            self.don.right(90)
            self.don.forward(width)
        if number == 8:
            self.draw_number(x, y, 3, width, height,angle)
            self.draw_number(newX(x,width,angle+90), newY(y,width,angle+90), 1, width, height,angle)
        if number == 9:
            self.draw_number(x, y, 7, width, height,angle)
            self.draw_number(x, y, 3, width, height,angle)

    def drawRectangle(self,x, y, width, height, angle):
        self.don.penup()
        self.don.setpos(x, y)
        self.don.pendown()
        self.don.begin_fill()
        self.don.left(angle)
        self.don.forward(height)
        self.don.left(90)
        self.don.forward(width)
        self.don.left(90)
        self.don.forward(height)
        self.don.left(90)
        self.don.forward(width)
        self.don.left(90)
        self.don.right(angle)
        self.don.end_fill()

    def draw_down_card(self,x,y,angle):
        self.don.fillcolor((255,255,255))
        self.don.pencolor('black')
        self.drawRectangle(x,y,70,100,90)
        self.don.fillcolor('black')
        self.don.pencolor('black')
        self.drawRectangle(x - ((7)*math.sin(math.radians(angle+45))), y + ((7)*math.cos(math.radians(angle+45))), 59, 90, 90)
        self.draw_number(x - (54 * math.sin(math.radians(angle + 54))), y + (54 * math.cos(math.radians(angle + 54))), 'logo', 20, 40,angle)

    def draw_card(self,x, y, color, number,angle):  # 70 X 100
        self.don.fillcolor((255, 255, 255))
        self.don.pencolor('black')
        self.drawRectangle(x, y, 70, 100, 90)
        y2 = y + 7
        self.don.fillcolor(color)
        self.don.pencolor(color)
        self.drawRectangle(x - ((7)*math.sin(math.radians(angle+45))), y + ((7)*math.cos(math.radians(angle+45))), 59, 90, 90)
        self.draw_number(x - (97*math.sin(math.radians(angle+38))), y + (97*math.cos(math.radians(angle+38))), number, 8, 16,angle)
        self.draw_number(x - (54 * math.sin(math.radians(angle + 48))), y + (54 * math.cos(math.radians(angle + 48))), number, 17, 34,angle)
        self.draw_number(x - (18 * math.sin(math.radians(angle + 60))), y + (18 * math.cos(math.radians(angle + 60))),number, 8, 16,angle)