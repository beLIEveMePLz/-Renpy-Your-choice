init python:
    class Player():
        """docstring for Player"""
        def __init__(self, maxhunger, maxrhirst, strengh, stamina, speed, focus, mood, luck):
            self.hunger = 0
            self.maxhunger= maxhunger
            self.thirst = 0
            self.maxrhirst = maxrhirst
            self.strengh = strengh
            self.stamina = stamina
            self.speed = speed
            self.focus = focus
            self.mood = mood
            self.luck = luck
            self.outfit = {hat: None, tshirt: None, torso: None, bikini: None , pants: None, legs: None}

        def addhunger(amount):
            self.hunger += amount
            if self.hunger > self.maxhunger:
                self.hunger = self.maxhunger

        def addthirst(amount):
            self.thirst += amount
            if self.thirst > self.maxrhirst:
                self.thirst = self.maxrhirst

        def losshunger(amount):
            self.hunger -= amount
            if self.hunger <= 0:
                self.hunger = 0

        def lossthirst(amount):
            self.hunger -= amount
            if self.hunger <= 0:
                self.hunger = 0



        