class Weapon(object):

    def __init__(self):
        self.skill_dictionary = Set()

    def add_skill(self, skill):
        self.skill_dictionary.add(skill)
        
    def read_skills(self, filename):
        # Open the file, read and parse lines,