from graphics import *
import random

"""
Assigns characters to each player.

I/P: players, a list of players of length 7
O/P: dict that maps characters to list of players

"""
def assign(players):
    good_guys = []
    bad_guys = []
    characters = {}
    random.shuffle(players)

    num_players = len(players)
    num_bad = num_players / 2
    
    for i in range(0,num_bad):
        bad_guys += players[i]
    for j in range(num_bad,num_players):
        good_guys += players[j]
        
    characters["Good"] = good_guys
    characters["Bad"] = bad_guys

    random.shuffle(good_guys)
    random.shuffle(bad_guys)

    characters["Snape"] = bad_guys[0]
    characters['Kingpin'] = good_guys[0]

    return characters

"""
Gets list of players from command line, puts their names onto the game window

I/P: The window to draw on.
O/P: The list of players.

"""
def getPlayers(win):
    x = raw_input('Enter player names (hit enter if done entering): ')
    ctr = 1
    y_pos = 1
    

    player_list = []
    
    while (x != ""):
        player_name= Entry(Point(140*ctr,180+(30*y_pos)), 20)
        player_name.setText(x)
        player_name.draw(win)
        if ctr % 4 == 0:
            y_pos += 1
            ctr = 0
        ctr += 1
        x = raw_input('Enter player names (hit enter if done entering): ')

"""
Main program to start the game.

"""
def main():
    win = GraphWin("The Resistance!", 700, 500)
    win.setBackground('black')

    titleText = Text(Point(350,100), "The Resistance")
    titleText.setTextColor('red')
    titleText.setStyle('bold italic')
    titleText.setSize(36)
    titleText.setFace('courier')
    titleText.draw(win)

    ex_out = Rectangle(Point(670,2), Point(705, 30))
    ex_out.setFill('grey')
    ex_out.draw(win)
    x = Text(ex_out.getCenter(), "X")
    x.setSize(30)
    x.setTextColor('black')
    x.setStyle('bold')
    x.draw(win)
    
    getPlayers(win)

    



    

main()
