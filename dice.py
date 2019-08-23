# Created on 8/23/2019

from random import randrange

class Dice:
    def __init__(self, num_dice):
        self.num_dice = num_dice
        self.rolls = [0] * (num_dice)

    def getCombinations(self):
        combos = []
        #There are 2^num_dice cominbations of dice
        for num in range (1, pow(2,len(self.rolls))):
            #binary holds 1 and 0 values for which dice we will add up
            binary = [0] * self.num_dice
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
            for use, val in zip(binary, self.rolls):
                ans += val * use
            if ans not in combos:
                combos.append(ans)
        return combos

    #Fill up an array with random numbers (Roll the dice)
    def rollDice(self):
        roll = ""
        for i in range(self.num_dice):
            self.rolls[i] = randrange(6) + 1
            roll += str(self.rolls[i])
            roll += "" if i == self.num_dice - 1 else ", "
        return roll

    def printRoll(self):
        roll_strings = [["   "," O ","   "], ["  O","   ","O  "], ["  O"," O ","O  "],
                        ["O O","   ","O O"], ["O O"," O ","O O"], ["O O","O O","O O"]]

        top = " -----  " * self.num_dice
        strings = ["| "] * 3
        for idx, val in enumerate(self.rolls):
            for i in range(3):
                strings[i] += roll_strings[val-1][i]
                strings[i] += " | | " if idx != self.num_dice-1 else " |"
        print (top+"\n"+strings[0]+"\n"+strings[1]+"\n"+strings[2]+"\n"+top) 
