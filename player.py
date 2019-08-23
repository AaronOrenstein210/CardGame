#Created on 8/22/2019

from dice import Dice

class Player:
    def __init__(self, name, num_dice):
        self.name = name
        self.nums = [0]
        #We need spots for num_dice * 6 both up and down
        self.nums *= num_dice * 12
        #The highest possible value is num_dice * 6
        for i in range(num_dice * 6):
            self.nums[i] = i + 1
            self.nums[len(self.nums) - 1 - i] = i + 1
    
    #Plays a turn, returns true if game continues, else false
    def playTurn(self, dice):
        while True:
            #Roll dice
            print (self.name,"rolled:", dice.rollDice())
            dice.printRoll()

            #Get all combinations of dice values
            combos = dice.getCombinations()

            #Save initial number of numbers to cross of
            length = len(self.nums)

            #Cross off numbers
            while self.nums[0] in combos:
                num = self.nums.pop(0)
                print ("Crossed off", num)
                print ("Left to go:", self.nums)
                if len(self.nums) == 0:
                    print (self.name, "Wins!")
                    return False
                #If we reached the top, turn auto ends
                if num == 12 and self.nums[0] == 12:
                    break

            #If no progress was made, end turn
            if length ==len(self.nums):
                break
            else:
                print()

        print ("Turn Over")

        return True

