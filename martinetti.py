# Created on 8/22/2019

from random import randrange
from time import sleep
from player import Player
from dice import Dice
import sys

num_dice = 10

def main():
    global num_dice

    #Initialize our players
    players = [Player("Aaron", num_dice),Player("Kyle", num_dice)]

    while False:
        #Ask if we are creating a new player
        new = input("Add a player? (y/n): ")
        #Don't add a new player
        if new == "n":
            #If we don't have enough players, ask again else start playing
            if len(players) < 2:
                print ("Please add at least 2 players")
            else:
                break
        #Add a new player
        elif new == "y":
            #Ask for a name unless a valid name is inputted
            while True:
                name = input("Please enter player name: ")
                if name in [x.name for x in players]:
                    print ("Name already in use")
                else:
                    players.append(Player(name, num_dice))
                    break
        #Ask again if anything else is inputed

    #Print player names
    print ("Players: ", end="")
    for idx, player in enumerate(players):
        print (player.name, end=(", " if idx != len(players)-1 else "\n\n"))

    #Create dice object
    dice = Dice(num_dice)

    #Keep playing until playing = false
    playing = True
    while playing:
        for player in players:
            playing = player.playTurn(dice)
            print ()
            if not playing:
                break
            sys.stdout.flush()
            sleep(1)

main()
