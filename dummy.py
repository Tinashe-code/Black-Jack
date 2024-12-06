from random import *
from time import *
class SubDeck:
    def __init__(self):
        pass

    def sorted_cards(self):
        global cards_dictionary
        cards_dictionary = {"A_diamond": "diamond", "A_heart": "hearts", "A_club": "club", "A_spade": "spade",
                            "K_diamond": "diamond", "K_heart": "hearts", "K_club": "club", "K_spade": "spade",
                            "Q_diamond": "diamond", "Q_heart": "hearts", "Q_club": "club", "Q_spade": "spade",
                            "J_diamond": "diamond", "J_heart": "hearts", "J_club": "club", "J_spade": "spade",
                            "10_diamond": "diamond", "10_heart": "hearts", "10_club": "club", "10_spade": "spade",
                            "9_diamond": "diamond", "9_heart": "hearts", "9_club": "club", "9_spade": "spade",
                            "8_diamond": "diamond", "8_heart": "hearts", "8_club": "club", "8_spade": "spade",
                            "7_diamond": "diamond", "7_heart": "hearts", "7_club": "club", "7_spade": "spade",
                            "6_diamond": "diamond", "6_heart": "hearts", "6_club": "club", "6_spade": "spade",
                            "5_diamond": "diamond", "5_heart": "hearts", "5_club": "club", "5_spade": "spade",
                            "4_diamond": "diamond", "4_heart": "hearts", "4_club": "club", "4_spade": "spade",
                            "3_diamond": "diamond", "3_heart": "hearts", "3_club": "club", "3_spade": "spade",
                            "2_diamond": "diamond", "2_heart": "hearts", "2_club": "club", "2_spade": "spade"}
        cards_labels = list(cards_dictionary.keys())
        shuffle(cards_labels)

        card_choices = {}
        for i in range(52):
            card_choices[i + 1] = cards_labels[i]
        card_choices_list = list(card_choices.values())
        return card_choices_list

    def printed_suit(self,card_label):
        suit_to_print = cards_dictionary[card_label]
        return suit_to_print

    def printed_rank(self,card_name):
        rank_dictionary = {"A_diamond": "A","A_heart": "A", "A_club": "A", "A_spade": "A",
                            "K_diamond": "K","K_heart": "K", "K_club": "K","K_spade": "K",
                            "Q_diamond": "Q","Q_heart": "Q", "Q_club":"Q","Q_spade": "Q",
                            "J_diamond": "J","J_heart": "J", "J_club": "J", "J_spade": "J",
                            "10_diamond": "10","10_heart": "10", "10_club": "10", "10_spade": "10",
                            "9_diamond": "9","9_heart": "9", "9_club": "9", "9_spade": "9",
                            "8_diamond": "8","8_heart": "8", "8_club": "8", "8_spade": "8",
                            "7_diamond": "7","7_heart": "7", "7_club": "7", "7_spade": "7",
                            "6_diamond": "6","6_heart": "6", "6_club": "6", "6_spade": "6",
                            "5_diamond": "5","5_heart": "5", "5_club": "5", "5_spade": "5",
                            "4_diamond": "4","4_heart": "4", "4_club": "4", "4_spade": "4",
                            "3_diamond": "3","3_heart": "3", "3_club": "3", "3_spade": "3",
                            "2_diamond": "2","2_heart": "2", "2_club": "2", "2_spade": "2"}
        rank_to_print = rank_dictionary[card_name]
        return rank_to_print

class Player:
    def __init__(self):
        pass

    def player_playing(self,myturtle,player_name):
        myturtle.begin_fill()
        myturtle.color("brown")
        myturtle.fillcolor("brown")
        myturtle.up()
        myturtle.goto(320,600)
        myturtle.down()
        myturtle.goto(420,600)
        myturtle.goto(420,570)
        myturtle.goto(320, 570)
        myturtle.goto(320, 600)
        myturtle.end_fill()
        myturtle.up()
        myturtle.goto(325,578)
        myturtle.down()
        myturtle.color("white")
        myturtle.write(player_name+" is playing", False, font=("Calibri", 10, "bold"))
        myturtle.up()



    def Invalid_selection(self,myturtle):
        myturtle.begin_fill()
        myturtle.color("brown")
        myturtle.fillcolor("brown")
        myturtle.up()
        myturtle.goto(320, 400)
        myturtle.down()
        myturtle.goto(500, 400)
        myturtle.goto(500,340)
        myturtle.goto(320, 340)
        myturtle.goto(320, 400)
        myturtle.end_fill()
        myturtle.up()
        myturtle.goto(325, 340)
        myturtle.down()
        myturtle.color("white")
        myturtle.write(" Invalid selection", False, font=("Calibri", 12, "bold"))
        myturtle.up()
        sleep(1)
        myturtle.begin_fill()
        myturtle.color("brown")
        myturtle.fillcolor("brown")
        myturtle.up()
        myturtle.goto(320, 400)
        myturtle.down()
        myturtle.goto(500, 400)
        myturtle.goto(500, 340)
        myturtle.goto(320, 340)
        myturtle.goto(320, 400)
        myturtle.end_fill()
        myturtle.up()
        myturtle.goto(325, 320)
        myturtle.down()
        myturtle.color("white")