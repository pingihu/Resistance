from graphics import *
import random
import time
import math

good = []
bad = []

"""
Assigns characters to each player.

I/P: players, a list of players of length 7
O/P: dict that maps players to a list of what team they are on
        and their teammates

"""
def assign(players):
    good_guys = []
    bad_guys = []
    characters = {}
    random.shuffle(players)

    num_players = len(players)
    num_bad = num_players / 2
    
    for i in range(0,num_bad):
        characters[players[i]] = ["Mafia"]
        print "now looking at: %s" % (players[i])
        bad_guys += players[i]
    for j in range(num_bad,num_players):
        characters[players[j]] = ["Good Guy"]
        good_guys += players[j]
        

    for p in characters.keys():
        val = characters[p][0]
        if val == "Mafia":
            characters[p] += [bad_guys]
        else:
            characters[p] += [good_guys]

    #assign a kingpin and a snape
    random.shuffle(bad_guys)
    random.shuffle(good_guys)

    characters[bad_guys[0]][0] = "Snape (Mafia)"
    characters[good_guys[0]][0] = "Kingpin (Good Guy)"

    good = good_guys
    bad = bad_guys
    print bad

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
        player_list += x
        player_name= Entry(Point(140*ctr,180+(30*y_pos)), 20)
        player_name.setText(x)
        player_name.draw(win)
        if ctr % 4 == 0:
            y_pos += 1
            ctr = 0
        ctr += 1
        x = raw_input('Enter player names (hit enter if done entering): ')

    

    return player_list

"""
Returns a string representing your teammates
"""
def teamAsString(teammates, you):
    toReturn = ""
    for mate in teammates:
        if mate != you:
            toReturn += "%s\n" % (mate)

    return toReturn

"""
Displays a "pass the computer to..." prompt,
when the player clicks OK, will show the player
their character for 10 seconds.

"""
def passComputer(win, players):
    win.close()
    win = GraphWin("The Resistance!", 700, 500)
    win.setBackground('black')

    character_dict = assign(players)

    for i in players:
        curr_msg = "Pass the computer to %s. %s, click anywhere to view your character." % (i, i)
        curr_text = Text(Point(350,100), curr_msg)
        curr_text.setTextColor('red')
        curr_text.draw(win)
        #wait for the user to click and see their character
        win.getMouse()

        curr_text.undraw()

        info = character_dict[i]
        character_name = info[0]


        teammates = info[1]
        teammates = filter(lambda(x): x!=i, teammates)
        team_string = ' '.join(str(x) for x in teammates)

        print team_string
        
        character_msg = "You are %s!  \nTeammates: %s" % (character_name, team_string)
        character_msg_good = ""
        character_msg_bad = ""

        if "Mafia" in character_name:
            win.setBackground('red')
        elif "Good" in character_name:
            win.setBackground('blue')
            if "Kingpin" in character_name:
                character_msg = "You are Kingpin!\n"
                character_msg_good = "Good guys:%s" % (team_string)
                character_msg_bad = "Mafia:%s" % ('\n'.join(str(e) for e in bad))

        screen_text = Text(Point(350,100), character_msg)
        screen_text.setSize(22)
        KP_text1 = Text(Point(200, 200), character_msg_good)
        KP_text2 = Text(Point(400, 200), character_msg_bad)

        screen_text.draw(win)
        KP_text1.draw(win)
        KP_text2.draw(win)


        
        begin = time.time()
        diff = 0
        ctr = 0
        cont = time.time()

        timer = Text(Point(630,20),ctr)
        timer.setSize(20)

        while (cont - begin < 16):
            if int(cont - begin) > diff:
                timer.undraw()
                diff = int(cont - begin)
                ctr += 1
                timer = Text(Point(630,20),ctr)
                timer.setSize(20)
                timer.draw(win)
            cont = time.time()

        timer.undraw()
        screen_text.undraw()
        KP_text1.undraw()
        KP_text2.undraw()

        win.setBackground('black')
        

        continue

    return


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

    #the following function will write all the player's names to
    #the game screen, then return this list of players.
    player_list = getPlayers(win)
    print player_list

    ready_text = Text(Point(360, 170), "Click anywhere to start!")
    ready_text.setSize(35)
    ready_text.setTextColor('red')
    ready_text.draw(win)

    win.getMouse()
    passComputer(win, player_list)

    
    
    
    



    

main()
