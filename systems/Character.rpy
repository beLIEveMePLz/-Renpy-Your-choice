init python:
    class Player():
        """docstring for Player"""
        def __init__(self, hunger, maxhunger, thirst, maxrhirst, strengh, stamina, speed, focus, mood, luck):
            self.hunger = hunger
            self.thirst = thirst
            self.strengh = strengh
            self.stamina = stamina
            self.speed = speed
            self.focus = focus
            self.mood = mood
            self.luck = luck

        def addhung(amount):
            self.hunger += amount
            if self.hunger > self.maxhunger:
                self.hunger = self.maxhunger

        def addthir(amount):
            self.thirst += amount
            if self.thirst > self.maxrhirst:
                self.thirst = self.maxrhirst

e