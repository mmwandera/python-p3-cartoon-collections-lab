# This function should accept a list of dwarf names. It should then print out each name, in number order, using print
def roll_call_dwarves(dwarves):
    num = 1
    for dwarf in dwarves:
        print(f"{num}. {dwarf}")
        num += 1
        
# This function should accept a list of planeteer calls as an argument. It should then capitalize each element and add an exclamation point at the end. The return value of this function should be a list
def summon_captain_planet(calls):
    return [call.title() + "!" for call in calls]

# The long_planeteer_calls() function should accept a list of calls as an argument. The function should tell us if any of the calls are longer than four characters. Notice the return value of this function is either True or False, depending on the list it was given as an argument.
def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
    return False

# The find_the_cheese() function should accept a list of strings. It should then look through these strings to find and return the first string that is a type of cheese. The types of cheese that appear are "cheddar", "gouda", and "camembert".
# If, sadly, a list of ingredients does not include cheese, return None
# You can assume that all strings will be lowercase. Take a look at the inLinks to an external site. keyword for a hint. This function asks you to return a string value instead of printing it so keep that in mind.
def find_the_cheese(cheese_types):
    for cheese_type in cheese_types:
        if cheese_type == "cheddar" or cheese_type == "gouda" or cheese_type == "camembert":
            return cheese_type
    return None