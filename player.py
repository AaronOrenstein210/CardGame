#Created on 8/22/2019

class Player:
    def __init__(self, name):
        self.name = name
        self.nums = [0] * 35
        for i in range(18):
            self.nums[i] = i + 1
            self.nums[len(self.nums) - 1 - i] = i + 1
