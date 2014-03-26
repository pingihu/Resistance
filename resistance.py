from graphics import *
import random
import time
import math
import random

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
        bad_guys.append(players[i])
    for j in range(num_bad,num_players):
        characters[players[j]] = ["Good Guy"]
        good_guys.append(players[j])
        

    for p in characters.keys():
        val = characters[p][0]
        if val == "Mafia":
            characters[p] += [bad_guys]
        else:
            characters[p] += [good_guys]

    #assign a kingpin and a snape
    random.shuffle(bad_guys)
    random.shuffle(good_guys)

    does_snape_exist = (random.randint(1,100) % 2 == 0)
        

    if does_snape_exist:
        characters[bad_guys[0]][0] = "Snape (Mafia)"
        characters[good_guys[0]][0] = "Kingpin (Good Guy)"
        characters[good_guys[0]].append(bad_guys) #gives kingpin mafia info
        characters[good_guys[0]].append(bad_guys[0]) #gives mafia snape info
    else:
        characters[good_guys[0]][0] = "Kingpin (Good Guy)"
        characters[good_guys[0]].append(bad_guys) #gives kingpin mafia info
        characters[good_guys[0]].append("No Snape") #gives mafia snape info

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
        player_list.append(x)
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

    orig_players = []
    orig_players += players
    
    character_dict = assign(players)

    for i in orig_players:
        curr_msg = "Pass the computer to %s. %s, click anywhere to view your character. \n WARNING: You will have 15 seconds ONLY to view your character information." % (i, i)
        curr_text = Text(Point(350,100), curr_msg)
        curr_text.setSize(14)
        curr_text.setTextColor('red')
        
        curr_text.draw(win)
        #wait for the user to click and see their character
        win.getMouse()

        curr_text.undraw()

        info = character_dict[i]
        character_name = info[0]


        teammates = info[1]
        teammates = filter(lambda(x): x!=i, teammates)
        team_string = '\n'.join(str(x) for x in teammates)
        
        character_msg = "You are %s!  \nTeammates: \n%s" % (character_name, team_string)
        character_msg_good = ""
        character_msg_bad = ""
        snape_msg = ""

        if "Mafia" in character_name:
            win.setBackground('dark red')
        elif "Good" in character_name:
            win.setBackground('cornflower blue')
            if "Kingpin" in character_name:
                character_msg = "You are Kingpin!\n"
                character_msg_good = "Good guys: \n%s" % (team_string)
                character_msg_bad = "Mafia: \n%s" % ('\n'.join(str(e) for e in info[2]))
                snape_msg = "Snape:\n%s" % (info[3]) 

        screen_text = Text(Point(350,100), character_msg)
        screen_text.setSize(22)
        KP_text1 = Text(Point(200, 200), character_msg_good)
        KP_text1.setSize(22)
        KP_text2 = Text(Point(400, 200), character_msg_bad)
        KP_text2.setSize(22)
        KP_snape = Text(Point(300, 450), snape_msg)
        KP_snape.setSize(22)
        

        screen_text.draw(win)
        KP_text1.draw(win)
        KP_text2.draw(win)
        KP_snape.draw(win)


        
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
                timer = Text(Point(630,20),(16 - ctr))
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

    instructions = Text(Point(350, 450), 'If you are playing with people who have the same names,\nplease add initials (or use different names)')
    instructions.setTextColor('red')
    instructions.setFace('courier')
    instructions.draw(win)

    #the following function will write all the player's names to
    #the game screen, then return this list of players.
    player_list = getPlayers(win)

    ready_text = Text(Point(360, 170), "Click anywhere to start!")
    ready_text.setSize(35)
    ready_text.setTextColor('red')
    ready_text.draw(win)

    win.getMouse()
    passComputer(win, player_list)

    
    
    
    



    

main()
