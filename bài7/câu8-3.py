print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
import turtle

painter = turtle.Turtle()
painter.speed(0)
painter.pensize(2)


colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow']

for i in range(12): 
    painter.pencolor(colors[i % 6]) 
    painter.circle(100)
    painter.left(30) 

turtle.done()
