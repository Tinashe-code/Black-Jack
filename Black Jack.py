# Importing usefull modules
from time import *
from turtle import *
from cards import *
from random import *
from dummy import *
from tkinter import *
import sys
import os
from PIL import ImageTk,Image
from tkinter import messagebox


root = Toplevel()
root.title("Black Jack")
root.iconbitmap("game.ico")
root.configure(bg="indigo")
root.geometry("1200x700")

my_img = ImageTk.PhotoImage(Image.open("cards.jpg"))
my_label = Label(root,image=my_img)
my_label.grid(row=0,column=0)


namelist =[]
def help():
   messagebox.showinfo("Help-Black Jack",
                       "-This game can be played by two or more players."
                       "-You have to click on two cards to open them and if they match then it a score for you"
                       "-If you match two cards you continue to play until you click unmatching cards"
                       "-The name of the playing player is displayed on the screen"
                       "-After every click you have to wait for the card to fully open before you click the next card"
                       "-You only click a card after there appears a blue blink at the top right corner of the screen"
                       "--------------")
def playersdetails():
    global user_inputs
    global user_names
    global namelist
    names = user_names.get()
    namelist = names.split()
    sleep(1)
    user_inputs.destroy()
    root.destroy()
    return namelist

def terminate():
    sys.exit()

#this functions contains a child window that will allow players to enter their names
def take_userinputs():
    global user_names
    global user_inputs
    user_inputs = Toplevel(root)
    user_inputs.title("Black Jack")
    user_inputs.iconbitmap("game.ico")
    my_img2 = ImageTk.PhotoImage(Image.open("cards22.jpg"))
    my_label2 = Label(user_inputs, image=my_img2)
    my_label.image = my_img2
    my_label2.grid(row=0, column=0)
    user_inputs.geometry("750x250")
    frame_2 = Frame(user_inputs, pady=5, padx=5, width=150, height=150, bg="black")
    frame_2.place(x=200, y=150)
    play = Button(frame_2,text="Play", width=10, height=1, bg="indigo", fg="yellow", activebackground = "green",activeforeground="white",font=("Arial Black",10),command=play_game)
    play.grid(row=5,column=0)
    user_names= Entry(frame_2,bg="yellow",width=50)
    label = Label(frame_2,text="Input the name of the players seperated by space (Two players and above)",bg="black",fg="white")
    user_names.grid(row=3,column=0)
    label.grid(row=1,column=0)
#make a frame for the buttons of the first page
frame = Frame(root,pady=5,padx=5,width=150, height=150,bg="indigo")
frame.place(x=500,y=300)

#buttons on the first page
button = Button(frame, text="Play New Game", width=20, height=3, bg="indigo", fg="yellow", activebackground = "yellow",activeforeground="indigo",
                font=("Arial Black",20),command=take_userinputs)
button1 = Button(frame, text="Quit", width=20, height=3, bg="indigo", fg="yellow", activebackground = "green",activeforeground="white",
                 font=("Arial Black",20),command=terminate)
button3 = Button(frame, text="Help", width=20, height=3, bg="indigo", fg="yellow", activebackground = "green",activeforeground="white",
                 font=("Arial Black",20),command=help)
#packing the buttons onto the screen
button.grid(row=0, column=0)
button1.grid(row=1, column=0)
button3.grid(row=2,column=0)

click_counter = 0
turns = 1

def play_game():
    # creating instances of our methods from our classe we have made in our modules
    suit_to_print = SubDeck()
    p = Card("diamond","red","diamond")
    current_player = Player()
    taku = Turtle()
    Jennie = Turtle()
    tina = Turtle()
    win = Screen()
    win.bgcolor("brown")
    wn = Screen()._root
    tina.speed(0)
    taku.speed(0)
    Jennie.speed(0)
    #setting up the environments for the tutles
    setworldcoordinates(-200,-500,200,500)
    tina.hideturtle()
    taku.hideturtle()
    Jennie.hideturtle()
    tina.up()
    wn.title("Black Jack")
    wn.iconbitmap("game.ico")

    # Running the main program
    # below is the card to run our main program
    # we will be making use of the modules we are using



    #The code to enter any number of users names. This code matches each player name to a unique number and creates a dictionary also responsible for handling scores
    playersplayinggame = playersdetails()
    players_scores = {}
    players_indexs = {}
    for player in playersplayinggame:
        players_indexs[playersplayinggame.index(player)+1]=player
        players_scores[player] = 0
    #this list contains the names of the players
    listredu = list(players_scores.keys())

    def increemnt_scores(player_number):
        players_scores[listredu[player_number-1]] = players_scores.get(listredu[player_number-1], 0) + 1




    #colour the initial background color of the cards
    Jennie.color("white")
    Jennie.begin_fill()
    Jennie.fillcolor("orange")
    Jennie.up()
    Jennie.goto(-300,600)
    Jennie.down()
    Jennie.goto(300, 600)
    Jennie.goto(300, -400)
    Jennie.goto(-180, -400)
    Jennie.goto(-180, -600)
    Jennie.goto(-300,-600)
    Jennie.goto(-300,600)
    Jennie.end_fill()

    #place the replay button on the turtle screen
    Jennie.begin_fill()
    Jennie.color("black")
    Jennie.fillcolor("black")
    Jennie.up()
    Jennie.goto(320, -400)
    Jennie.down()
    Jennie.goto(500, -400)
    Jennie.goto(500, -540)
    Jennie.goto(320, -540)
    Jennie.goto(320, -400)
    Jennie.end_fill()
    Jennie.up()
    Jennie.goto(325, -515)
    Jennie.down()
    Jennie.color("white")
    Jennie.write("Replay", False, font=("Calibri", 30, "bold"))
    Jennie.up()

    # place the exit button on the turtle screen
    Jennie.begin_fill()
    Jennie.color("black")
    Jennie.fillcolor("black")
    Jennie.up()
    Jennie.goto(320, -300)
    Jennie.down()
    Jennie.goto(500, -300)
    Jennie.goto(500, -390)
    Jennie.goto(320, -390)
    Jennie.goto(320, -300)
    Jennie.end_fill()
    Jennie.up()
    Jennie.goto(325, -390)
    Jennie.down()
    Jennie.color("white")
    Jennie.write("Exit", False, font=("Calibri", 30, "bold"))
    Jennie.up()

    #draw the desing on the back of the cards
    def Back_of_cards(myturtle):
        Jennie.hideturtle()
        myturtle.color("black")
        for i in range(6):
            y = -560 + (200 * i)
            for n in range(10):
                x = -290 + (60 * n)
                if y<-400 and x>-180:
                    pass
                else:
                    myturtle.up()
                    myturtle.goto(x, y)
                    myturtle.down()
                    myturtle.write(chr(9821), False, font=("Courier New", 50, "bold"))
    Back_of_cards(Jennie)


    #this is a list of the names we have given to each and every single playing card
    our_list = suit_to_print.sorted_cards()





    #drawing the grids of the cards on the screen
    #drawing the horizontal bars
    for i in range(6):
        tina.goto(-300,(600-200*i))
        tina.down()
        tina.fd(600)
        tina.up()
    tina.goto(-300,-600)
    tina.down()
    tina.goto(-180,-600)
    tina.up()
    # drawing vertical bars
    for i in range(3):
        tina.goto((-300 + 60 * i), 600)
        tina.down()
        tina.goto((-300 + 60 * i), -600)
        tina.up()
    for k in range(9):
        tina.goto((-300+60*(k+2),600))
        tina.down()
        tina.goto((-300+60*(k+2)),-400)
        tina.up()

    # a list that will contain the set of deleted cards
    Deleted = []

    # the following code is used to count the number of clicks made by the user
    #it will then give turns for the users
    click_counter = 0
    turns = 1
    open("outputfile.txt",'w')

    def count_initialise(): #this will initialise the our counters after players have taken their turns
        global click_counter
        click_counter = 0

    #this will make the player turns back to the initial value after the last player have played
    def turns_initialise():
        global turns
        turns=1

    def Jennifar(x,y,click_number,player_number):
        global first_click_row, first_click_column, second_click_row, second_click_column,first_clicked_square,second_clicked_square
        global square
        outputfile = open("outputfile.txt", 'a+')

        if x >= -300 and x <= 300 and y >= -600 and x <= 600:
            column = int(x + 300) // 60 + 1
            row = (y + 600) // 200 + 1
            if row == 6:
                square = (6 * column) / 60 * 10
            elif row == 5:
                square = int(10 + column)
            elif row == 4:
                square = int(20 + column)
            elif row == 3:
                square = int(30 + column)
            elif row == 2:
                square = int(40 + column)
            elif row == 1:
                square = int(50 + column)

            else:
                pass
            if click_number == 1:
                outputfile.writelines("first_click_row" + " " + str(row) + "\n")
                outputfile.writelines("first_click_column" + " " + str(column) + "\n")
                outputfile.writelines("first_click_square" + "  " + str(square) + "\n")
            elif click_number == 2:
                outputfile.writelines("second_click_row " + " " + str(row) + "\n")
                outputfile.writelines("second_click_column " + " " + str(column) + "\n")
                outputfile.writelines("second_click_square" + "  " + str(square) + "\n")
                count_initialise()
            outputfile.close()
            if square not in Deleted:
                myprog(tina,row,column,click_number,player_number)




    def clicked(x,y):
        global click_counter
        global turns
        global square

        if x >= 320 and x <= 500 and y >= -550 and y <= -400:
            win.bye()
            os.system("python main.py")
        if x >= 320 and x <= 500 and y >= -390 and y <= -300:
            sys.exit()
        if x < -300 or x > 300 or y < -600 or y > 600:
            current_player.Invalid_selection(taku)
        else:
            pass
        if x >= -300 and x <= 300 and y >= -600 and y <= 600: #the first two nested if statements are there to check whether you have clicked where there is a card
            if x>=-180 and y<=-400:
                current_player.Invalid_selection(taku)
            else:
                if turns ==1: # this is because players will play in order from player 1
                    current_player.player_playing(taku, players_indexs[turns])
                else:
                    pass
                click_counter = click_counter+1
                if click_counter==2:
                    pass
                if turns == len(namelist)+1:
                    turns_initialise()

                Jennifar(x, y,click_counter,turns)
        else:
            pass


    def myprog(myturtle,clicked_row,clicked_column,click_number,player_number):
        if square<=52:
            global suit
            global names
            global shapes
            names = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
            shapes = ["diamond", "club", "spade", "hearts"]
            suit = {"diamond": 9830, "spade": 9824, "hearts": 9829, "club": 9827}
            card_rank_value = suit_to_print.printed_rank(our_list[int(square - 1)])
            suit_displayed = suit[suit_to_print.printed_suit(our_list[int(square-1)])]
            p.draw_card(myturtle, clicked_row, clicked_column)
            p.write_middle(myturtle, suit_displayed,clicked_row,clicked_column)
            p.write_bottom(myturtle, clicked_row, clicked_column,card_rank_value,suit_displayed)
            p.write_top(myturtle, clicked_row, clicked_column,card_rank_value,suit_displayed)
            if click_number==2:
                Jacob(taku, 2,player_number)
            else:
                pass
            #this code is responsible for giving time delays and notifying users when they can click
            sleep(1)
            taku.up()
            taku.goto(320, 620)
            taku.down()
            taku.begin_fill()
            taku.fillcolor("blue")
            taku.circle(20)
            taku.end_fill()
            taku.up()
            taku.goto(320, 620)
            taku.down()
            taku.begin_fill()
            taku.fillcolor("brown")
            taku.circle(20)
            taku.end_fill()

    def Jacob(myturtle,click_number,player_number):
        global turns
        global click_counter
        clicks = {}
        file = open("outputfile.txt", 'r').readlines()
        for item in file:
            selected_card = item.split()
            clicks[selected_card[0]] = selected_card[1]
        first_click_row = int(float(clicks["first_click_row"]))
        first_click_column = int(float(clicks["first_click_column"]))
        first_clicked_square = int(float(clicks["first_click_square"]))
        second_click_row = int(float(clicks["second_click_row"]))
        second_click_column = int(float(clicks["second_click_column"]))
        second_clicked_square = int(float(clicks["second_click_square"]))
        if click_number==2:
            if first_clicked_square == second_clicked_square:
                current_player.Invalid_selection(taku)
                click_counter = 1
            else:
                if suit_to_print.printed_rank(our_list[int(first_clicked_square) - 1]) == suit_to_print.printed_rank(our_list[int(second_clicked_square) - 1]):
                    p.delete_cards(myturtle, first_click_row, first_click_column)
                    p.delete_cards(myturtle, second_click_row, second_click_column)
                    Deleted.append(first_clicked_square)
                    Deleted.append(second_clicked_square)
                    increemnt_scores(player_number)
                    current_player.player_playing(taku,players_indexs[turns])
                    if len(Deleted) == 52:
                        score_values = list(players_scores.values())
                        winner_score = score_values.index(max(score_values))
                        winner_name = listredu[winner_score]
                        tina.color("black")
                        tina.goto(320, 500)
                        tina.down()
                        tina.write(winner_name + " Won the game", False, font=("Courier New", 10, "bold"))
                        tina.up()
                        tina.goto(320,240)
                        tina.color("white")
                        tina.down()
                        tina.write("Player Scores", False, font=("Courier New", 14, "bold"))
                        tina.up()
                        incrementor = 0
                        for final_names in listredu:
                            Jennie.up()
                            Jennie.color("white")
                            Jennie.goto(320,200-incrementor)
                            Jennie.down()
                            value_to_display = players_scores[final_names]
                            Jennie.write(final_names+"           : "+str(value_to_display))#final_names, "    ",players_scores[final_names], False, font=("Courier New", 10, "bold"))
                            incrementor = incrementor + 20
                            Jennie.up()

                else:
                    p.flip_back(myturtle, first_click_row, first_click_column)
                    p.flip_back(myturtle, second_click_row, second_click_column)
                    turns = turns + 1
                    if turns == len(namelist)+1:
                        turns_initialise()
                    else:
                        current_player.player_playing(taku, players_indexs[turns])
        else:
            pass
        foo = open("outputfile.txt", 'w')
        foo.close()
    onscreenclick(clicked)
    mainloop()
root.mainloop()



