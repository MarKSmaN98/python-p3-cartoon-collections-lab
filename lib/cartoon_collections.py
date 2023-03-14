def roll_call_dwarves(dwarves):
    iterator = 0
    while iterator < len(dwarves):
        print(f"{iterator + 1}. {dwarves[iterator]}")
        iterator += 1

def test(expList):
    i = 1
    for item in expList:
        print(f"{i}. {item}")
        i += 1

def summon_captain_planet(exp_list):
    return [elem.capitalize() + '!' for elem in exp_list]

def long_planeteer_calls(word_list):
    for word in word_list:
        if len(word) > 4:
            return True
    return False

def find_the_cheese(exp_list):
    for item in exp_list:
        if item == "cheddar":
            return item
    return None

