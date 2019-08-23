# Created on 8/22/2019

from random import randrange
from time import sleep
from player import Player

roll_strings = [["   "," O ","   "], ["  O","   ","O  "], ["  O"," O ","O  "],
                    ["O O","   ","O O"], ["O O"," O ","O O"], ["O O","O O","O O"]]

def main():
    #Initialize our players
    players = [Player("Aaron"),Player("Kyle")]

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
                    players.append(Player(name))
                    break
        #Ask again if anything else is inputed
    print ("Players:", [x.name for x in players])

    #Keep playing until playing = false
    playing = True
    while playing:
        for player in players:
            playing = playTurn(player)
            print ()
            if not playing:
                break

def playTurn(player):
    #Roll dice
    dice = [0,0,0]
    print (player.name,"rolled:", rollDice(dice))
    printRoll(dice)

    #Get all combinations of dice values
    combos = getCombinations(dice)

    #Cross off numbers
    while player.nums[0] in combos:
        num = player.nums.pop(0)
        print ("Crossed off", num)
        print ("Left to go:", player.nums)
        if len(player.nums) == 0:
            print (player.name, "Wins!")
            return False
    return True
    
def getCombinations(dice):
    combos = []
    #There are 2^num_dice cominbations of dice
    for num in range (1, pow(2,len(dice))):
        #binary holds 1 and 0 values for which dice we will add up
        binary = [0] * len(dice)
        #power holds which spot we are at in binary (2 to what power)
        power = len(binary) - 1
        temp = num
        while temp > 0 and power >= 0:
            #If temp is even, divide by two and move to the next binary spot
            if temp % 2 == 0:
                temp /= 2
                power -= 1
            #If temp is odd, subtract 1 and set the current binary spot to 1
            else:
                temp -= 1
                binary[power] = 1
        #Add up the combination of dice specified in the binary array
        ans = 0
        for use, val in zip(binary, dice):
            ans += val * use
        if ans not in combos:
            combos.append(ans)
    return combos

#Fill up an array with random numbers (Roll the dice)
def rollDice(dice):
    roll = ""
    for i in range(len(dice)):
        dice[i] = randrange(6) + 1
        roll += str(dice[i])
        roll += "" if i == len(dice) - 1 else ", "
    return roll

def printRoll(dice):
    global roll_strings
    top = " -----  " * 3
    strings = ["| "] * 3
    for idx, val in enumerate(dice):
        for i in range(3):
            strings[i] += roll_strings[val-1][i]
            strings[i] += " | | " if idx != len(dice)-1 else " |"
    print (top+"\n"+strings[0]+"\n"+strings[1]+"\n"+strings[2]+"\n"+top+"\n")
main()
