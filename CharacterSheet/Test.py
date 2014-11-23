from Skills import Skill


s = Skill()
s.parseLine("one,two,three, four, five")
print s.skill_name
print s.skill_ranks
print s.skill_modifier
print s.bonuses
print s.temp_modifier


