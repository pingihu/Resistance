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
    
    for i in range(0,3):
        bad_guys += players[i]
    for j in range(3,6):
        good_guys += players[j]
        
    characters["Good"] = good_guys
    characters["Bad"] = bad_guys

    random.shuffle(good_guys)
    random.shuffle(bad_guys)

    characters["Snape"] = bad_guys[0]
    characters['Kingpin'] = good_guys[0]

    return characters

"""
Testing for assign
*assign takes in a list of players of length 7*

"""    
def test_assign():
    players3 = ["Diplo", "Lauryn Hill", "Miami Horror", "Clams Casino",
                      "Mick Jagger", "Gabe", "Heitor Villa-Lobos"]
    print assign(players3)


"""
Main program to start the game.

"""
def main():
    win = GraphWin("The Resistance!", 700, 500)
    win.setBackground('black')

    titleHandle = open('/Users/pingihu/Resistance/title.txt', 'r')
    title = titleHandle.read()
    titleHandle.close()
    print title

    titleText = Text(Point(30,30), title)
    titleText.setTextColor('red')
    titleText.draw(win)

    ex_out = Rectangle(Point(670,2), Point(705, 30))
    ex_out.setFill('grey')
    ex_out.draw(win)
    x = Text(ex_out.getCenter(), "X")
    x.setSize(30)
    x.setTextColor('black')
    x.setStyle('bold')
    x.draw(win)
    
    player_list = Entry(Point(100,400), 200)
    player_list.draw(win)
    
    

main()
