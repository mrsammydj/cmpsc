import random
import turtle

def drawBar(green, yellow, red):
    wn = turtle.Screen()
    wn.title("Counts Bar Graph")
    wn.bgcolor("blue")

    trt = turtle.Turtle()
    trt.penup()
    trt.forward(-100)
    trt.pendown()

    color = [["green", green], ["yellow", yellow], ["red", red]]
    for count in color:
        trt.color("black", count[0])
        trt.forward(20)
        trt.left(90)
        trt.begin_fill()
        trt.forward(count[1] * 2)
        trt.right(90)
        trt.write(str(count[1]))
        trt.forward(20)
        trt.right(90)
        trt.forward(count[1] * 2)
        trt.end_fill()
        trt.left(90)
        trt.forward(15)

    wn.mainloop()

def writeValues(x):
    f = open("counts.txt", "w")
    for i in range (x):
        f.write(str(random.randint(0,100)) + "\n")
    f.close()

def getCounts():
    green = 0
    yellow = 0
    red = 0
    f = open("counts.txt")
    for line in f:
        val = int(line)
        if val >= 50:
            green += 1 
        elif val >= 25:
            yellow += 1
        else:
            red += 1
    f.close()
    return green, yellow, red


if __name__ == "__main__":
    writeValues(int(input("Enter a number: ")))
    g, y, r = getCounts()
    drawBar(g,y,r)