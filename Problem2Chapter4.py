

def draw_square(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()

def many_squares(t):
  for i in range(5):
    draw_square(t,20 + 20*i)

def main():
  import turtle
  t = turtle.Turtle()
  t.color('hotpink')
  t.pensize(3)
  many_squares(t) 

main()
