story = """once upon a time their was a cartoon named bhuri bhuri.
I watched him so much so that one day he came outside Televiion and ate my head"""
print(len(story))
print(story.endswith("head"))  # returns false if not correct and vice-versa
print(story.startswith("Once"))  # returns false if not correct and vice-versa
print(story.count("o"))  # counts the occurance of the given character
print(story.find("upon"))  # finds the given string or character
print(story.capitalize())  # makes the first letter of the string uppercase
print(story.replace("Televiion", "Football"))  # pretty obvious
