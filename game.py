import turtle 
import time
import winsound
wn = turtle.Screen() 
wn.tracer(0)
wn.title("Save the world") 
wn.bgpic("galaxy.gif") 
wn.register_shape("1.gif")
wn.register_shape("2.gif")
wn.register_shape("3.gif")
earth = turtle.Turtle() 
earth.shape("1.gif") 
clicks = 0 
pen = turtle.Turtle() 
pen.hideturtle() 
pen.color("white") 
pen.penup() 
pen.goto(0,200) 
pen.write(f"Clicks: {clicks}", align="center" , font = ("Courier New", 36,"normal"))

apple_pen = turtle.Turtle()
apple_pen.hideturtle() 
apple_pen.color("white")
apple_pen.penup()

timer_text = turtle.Turtle()
timer_text.color("red")
time_text.hideturtle()
timer_text.goto(0,160)
start = time.time()
while time.time() - start < 21:
  timer_text.clear()
  timer_text.write("Time:"+str(int(time.time() - start)),align="center", font=("Courier", 33))
  def clicked(x,y):
      global clicks
      clicks += 1 
      pen.clear() 
      pen.write(f"Clicks: {clicks}", align="center" , font = ("Courier New", 36,"normal"))
      winsound.PlaySound("click.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
      if 50 <= clicks <= 98 :
        earth.shape("2.gif")
      if clicks > 99 :
        earth.shape("3.gif")
      if time.time() - start > 20 :
        clicks-=1
      if time.time() - start > 20 and clicks >=100:
        apple_pen.goto(0,-20)
        apple_pen.write(f"You save the earth!!", align="center" , font = ("Courier New", 26,"bold"))
        winsound.PlaySound("win.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
      if time.time() - start > 20 and clicks <100:
        apple_pen.goto(0,-20)
        apple_pen.write(f"BOOM!!", align="center" , font = ("Courier New", 26,"bold"))
        winsound.PlaySound("bomb.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
  earth.onclick(clicked)
  wn.update()
wn.mainloop()
