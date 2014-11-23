'''
This class will be the window for the various attacks the character can do.

'''
class Skills(object):

    def __init__(self):
        self.skill_dictionary = Set()

    def add_skill(self, skill):
        self.skill_dictionary.add(skill)
        
    def read_skills(self, filename):
        # Open the file, read and parse lines,