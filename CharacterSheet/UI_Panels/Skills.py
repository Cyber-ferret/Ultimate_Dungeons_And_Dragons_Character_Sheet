from sets import Set

class Skill(object):

    def __init__(self):
        self.skill_name = None
        self.skill_ranks = None
        self.skill_modifier = None
        self.bonuses = None
        self.temp_modifier = None
        
    def parseLine(self, line):
        values = string.split(line, ",")
        self.skill_name = string.strip(values[0])
        self.skill_ranks = string.strip(values[1])
        self.skill_modifier = string.strip(values[2])
        self.bonuses = string.strip(values[3])
        self.temp_modifier = string.strip(values[4])
        


class Skills(object):

    def __init__(self):
        self.skill_dictionary = Set()

    def add_skill(self, skill):
        self.skill_dictionary.add(skill)
        
    def read_skills(self, filename):
        # Open the file, read and parse lines,
        