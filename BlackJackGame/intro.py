from turtle import Turtle, Screen
from time import sleep
import main_menu
#vytvoření podkladového okna
intro = Screen()
intro.setup(width=500, height=300)
intro.title("Black Jack")
intro.bgcolor("#ddddee")
# vypnutí trasování
intro.tracer(1)
#vytvoření karet nad nadpisem "BLACK JACK" v rámci intro
intro.register_shape("./cards/ACi.gif")
intro.register_shape("./cards/ADi.gif")
intro.register_shape("./cards/AHi.gif")
intro.register_shape("./cards/ASi.gif")
#křížové eso
club = Turtle()
club.penup()
club.shape("./cards/ACi.gif")
club.goto(-170, 70)
#kárové eso
diamond = Turtle()
diamond.penup()
diamond.shape("./cards/ADi.gif")
diamond.goto(-60, 70)
#srdcové eso
hearts = Turtle()
hearts.penup()
hearts.shape("./cards/AHi.gif")
hearts.goto(60, 70)
#pikové eso
spades = Turtle()
spades.penup()
spades.shape("./cards/ASi.gif")
spades.goto(170, 70)

intro.tracer(0)

#funkce napíše nápis "BLACK JACK"
def write_intro_title():
  #černá část
  black = Turtle()
  black.penup()
  black.shape("square")
  black.color("#000000")
  black.goto(-210, -80)
  black.write("BLACK", font=("Arial", 44, "bold"))
  black.hideturtle()
  #červená část
  jack = Turtle()
  jack.penup()
  jack.shape("square")
  jack.color("#990000")
  jack.goto(35, -80)
  jack.write("JACK", font=("Arial", 44, "bold"))
  jack.hideturtle()

#podtrhne intro text
def underliner():
  global intro
  underline = Turtle("blank")
  underline.penup()
  underline.speed(1.7)
  underline.goto(-210, -85)
  underline.pensize(5)
  underline.color("#990000")
  #zapnutí trasování
  intro.tracer(1)
  #černé podtržení
  underline.pendown()
  underline.forward(205)
  #mezera podtržení
  underline.penup()
  underline.forward(40)
  #červené podtržení
  underline.pendown()
  underline.color("#000000")
  underline.forward(165)
  sleep(1.7)

#spuštění nápisu "BLACK JACK" a jeho podtržení
write_intro_title()
underliner()
#ukončení intro a přechod do hlavního menu
intro.bye()
main_menu.create_main_menu(amenu_bg_color="#ddddee")
