'''
This class will be an individual ability, it's description, and uses per day
Ex. Arcane Pool, Lay on Hands, etc.
'''
class Ability(object):

    def __init__(self):
        self.skill_name = None
        self.skill_description = None
        self.charges = None