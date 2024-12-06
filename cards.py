from turtle import *
from random import choice
tina = Turtle()
wn = Screen()
setworldcoordinates(-200,-500,200,500)
tina.hideturtle()
class Card:
    def __init__(self,name,symbol_color,shape):
        self.shape = shape
        self.name = name
        self.symbol_color = symbol_color
        self.symbols = {"diamond":chr(9830),"heart":chr(9829),"club":chr(9827),"spade":chr(9824)}

    def draw_card(self,myturtle,row,column):
        #Draw the card border and fill in background color
        myturtle.speed(0)
        y = -400 + (200 * (row - 1))
        x = -300 + (60 * (column - 1))
        if y < -400 and x > -180:
            pass
        else:
            myturtle.color("black")
            myturtle.up()
            myturtle.goto(x, y)
            myturtle.down()
            myturtle.begin_fill()
            myturtle.fillcolor("white")
            myturtle.fd(60)
            myturtle.rt(90)
            myturtle.fd(200)
            myturtle.rt(90)
            myturtle.fd(60)
            myturtle.rt(90)
            myturtle.fd(200)
            myturtle.rt(90)
            myturtle.end_fill()
            myturtle.fd(60)
            myturtle.rt(90)
            myturtle.fd(200)
            myturtle.rt(90)
            myturtle.fd(60)
            myturtle.rt(90)
            myturtle.fd(200)
            myturtle.rt(90)
    #this code will delete the cards y drawing a brown color on the flipped card
    def delete_cards(self,myturtle,row,column):
        y = -600 + (200 * (row))
        x = -360 + (60 * (column))
        myturtle.up()
        myturtle.goto(x, y)
        myturtle.down()
        myturtle.begin_fill()
        myturtle.color("brown")
        myturtle.fillcolor("brown")
        myturtle.fd(60)
        myturtle.rt(90)
        myturtle.fd(200)
        myturtle.rt(90)
        myturtle.fd(60)
        myturtle.rt(90)
        myturtle.fd(200)
        myturtle.rt(90)
        myturtle.end_fill()

    # write to the top of the card
    def write_top(self,myturtle,row,column,card_name,charcode):
        x_1 = -295 + (60 * (column - 1))
        y_1 = -450 + (200 * (row - 1))
        y_4 = -590 + (200 * (row - 1))
        myturtle.up()
        myturtle.goto(x_1, y_1)
        myturtle.down()
        myturtle.write(card_name, False, font=("Calibri", 15, "bold"))
        myturtle.up()
        myturtle.goto(x_1, y_4)
        myturtle.down()
        myturtle.write(chr(charcode), False, font=("Calibri", 20, "bold"))
        myturtle.up()

    # write to the bottom of the card
    def write_bottom(self,myturtle,row,column,card_name,charcode):
        x_2 = -255 + (60 * (column - 1))
        y_2 = -590 + (200 * (row - 1))
        y_3 = -450 + (200 * (row - 1))
        myturtle.up()
        myturtle.goto(x_2, y_2)
        myturtle.down()
        myturtle.write(card_name, False, font=("Calibri", 15, "bold"))
        myturtle.up()
        myturtle.goto(x_2, y_3)
        myturtle.down()
        myturtle.write(chr(charcode), False, font=("Calibri", 20, "bold"))
        myturtle.up()

    #write in the middle of the card. At this point we will be writing the suit in the central position of the clicked card.
    #this is how we will be flipping on the cards
    def write_middle(self,myturtle,charcode,row,column):
        y = -560 + (200 * (row-1))
        x = -280 + (60 * (column-1))
        myturtle.up()
        myturtle.goto(x,y)
        myturtle.down()
        if charcode==9824 or charcode==9827:
            myturtle.color("#000000")
            myturtle.write(chr(charcode), False, font=("Courier New", 50, "bold"))

        else:
            myturtle.color("#FF0000")
            myturtle.write(chr(charcode), False, font=("Courier New", 50, "bold"))
        pass

    def flip_back(self,myturtle,row,column):
        y = -600 + (200 * (row))
        x = -360 + (60 * (column))
        myturtle.up()
        myturtle.goto(x, y)
        myturtle.down()
        myturtle.begin_fill()
        myturtle.color("orange")
        myturtle.fillcolor("orange")
        myturtle.fd(60)
        myturtle.rt(90)
        myturtle.fd(200)
        myturtle.rt(90)
        myturtle.fd(60)
        myturtle.rt(90)
        myturtle.fd(200)
        myturtle.rt(90)
        myturtle.end_fill()
        myturtle.color("black")
        myturtle.goto(x, y)
        myturtle.down()
        myturtle.fd(60)
        myturtle.rt(90)
        myturtle.fd(200)
        myturtle.rt(90)
        myturtle.fd(60)
        myturtle.rt(90)
        myturtle.fd(200)
        myturtle.rt(90)
        #this code will draw the back design of our playing cards by locating the center of the cards
        y = -560 + (200 * (row-1))
        x = -285 + (60 * (column-1))
        myturtle.up()
        myturtle.goto(x,y)
        myturtle.down()
        myturtle.color("black")
        myturtle.write(chr(9821), False, font=("Courier New", 50, "bold"))
        myturtle.up()




class CardDeck:
    def __init__(self):
        pass

    # in this part we will make a random dictionary of our deck
    # this will ensure that each time the game is played there is a unique arrangements of the cards
    # we will use the random choice method for this part
    def card_selection(self):
        count = 0
        card_choices = {}
        names = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        shapes = ["diamond", "club", "spade", "hearts"]
        while count<52:
            shape = choice(shapes)
            name = choice(names)
            if (shape, name) in card_choices.items()==True:
                pass
            else:
                card_choices[shape] = name
                count = count + 1
        shapes_to_use = list(card_choices.keys())
        return shapes_to_use