from turtle import Turtle, Screen
from time import sleep
import main_menu
#create root widget
intro = Screen()
intro.setup(width=500, height=300)
intro.title("Black Jack")
intro.bgcolor("#ddddee")
# turn on tracing
intro.tracer(1)
#create intro cards images
intro.register_shape("./cards/ACi.gif")
intro.register_shape("./cards/ADi.gif")
intro.register_shape("./cards/AHi.gif")
intro.register_shape("./cards/ASi.gif")
#club ace 
club = Turtle()
# don´t write tracer line
club.penup()
club.shape("./cards/ACi.gif")
club.goto(-170, 70)
#diamond ace
diamond = Turtle()
diamond.penup()
diamond.shape("./cards/ADi.gif")
diamond.goto(-60, 70)
#heart ace
hearts = Turtle()
hearts.penup()
hearts.shape("./cards/AHi.gif")
hearts.goto(60, 70)
#spade ace
spades = Turtle()
spades.penup()
spades.shape("./cards/ASi.gif")
spades.goto(170, 70)
#turn off tracer
intro.tracer(0)

#write title "BLACK JACK"
def write_intro_title():
  #black part
  black = Turtle()
  black.penup()
  black.shape("square")
  black.color("#000000")
  black.goto(-210, -80)
  black.write("BLACK", font=("Arial", 44, "bold"))
  black.hideturtle()
  #red part
  jack = Turtle()
  jack.penup()
  jack.shape("square")
  jack.color("#990000")
  jack.goto(35, -80)
  jack.write("JACK", font=("Arial", 44, "bold"))
  jack.hideturtle()

#underline the text
def underliner():
  global intro
  underline = Turtle("blank")
  underline.penup()
  underline.speed(1.7)
  underline.goto(-210, -85)
  underline.pensize(5)
  underline.color("#990000")
  #turn on tracing
  intro.tracer(1)
  #black underlining
  underline.pendown()
  underline.forward(205)
  #underline space
  underline.penup()
  underline.forward(40)
  #red underlining
  underline.pendown()
  underline.color("#000000")
  underline.forward(165)
  sleep(1.7)

#start title creating "BLACK JACK" and underline it
write_intro_title()
underliner()
#end intro and go to main menu window
intro.bye()
main_menu.create_main_menu(amenu_bg_color="#ddddee")
