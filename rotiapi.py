from turtle import *

current_number = 20

def draw_cake():
   
    penup()
    goto(-150, -100)
    pendown()
    color("coral")
    begin_fill()
    forward(300)
    left(90)
    forward(150)
    left(90)
    forward(300)
    left(90)
    forward(150)
    left(90)
    end_fill()

    
    penup()
    goto(-140, 50)
    pendown()
    color("lightpink")
    begin_fill()
    forward(280)
    left(90)
    forward(20)
    left(90)
    forward(280)
    left(90)
    forward(20)
    left(90)
    end_fill()

    
    for i in range(5):
        penup()
        goto(-120 + i * 60, 50)
        pendown()
        color("gray")
        begin_fill()
        forward(10)
        left(90)
        forward(40)
        left(90)
        forward(10)
        left(90)
        forward(40)
        left(90)
        end_fill()

def draw_candle_flames():
   
    for i in range(5):
        penup()
        goto(-115 + i * 60, 100)
        pendown()
        color("yellow")
        begin_fill()
        circle(5)
        end_fill()

def draw_number(num):
    
    penup()
    goto(0, -50)  
    color("pink")
    write(num, align="center", font=("Arial", 48, "bold"))

def move_text(text):
    
    penup()
    goto(0, 140)
    color("white")
    write(text, align="center", font=("Arial", 24, "bold"))

def change_number():
    global current_number
    if current_number == 20:
        current_number = 21  
        clear_number_area()
        draw_number(current_number)  
        draw_candle_flames()  

def clear_number_area():
 
    penup()
    goto(-50, -100)
    pendown()
    color("coral")  
    begin_fill()
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    end_fill()

bgcolor("black")
draw_cake()
draw_number(current_number)
move_text("HAPPY BIRTHDAY")


listen()  
onkey(change_number, "space")  
done()
