import random

# ---------GENERATE RANDOM NUMBER FOR COMPUTER-----------#
number = random.randint(1, 10)
if number < 3:
    computer = "s"
elif number < 6 and number > 3:
    computer = "w"
elif number > 6:
    computer = "g"

# ----------HELPER FOR Fx(RESULTS)-----------#
def decide(computer, human):
    # Equal conditions i.e ---> SS WW GG condition
    if computer == human:
        return 0
    # SW and WS condition
    if computer == "s" and human == "w":
        return -1
    elif computer == "w" and human == "s":
        return 1
    # SG ang GS condition
    if computer == "s" and human == "g":
        return 1
    elif computer == "g" and human == "s":
        return -1
    # WG and GW condition
    if computer == "w" and human == "g":
        return -1
    elif computer == "g" and human == "w":
        return 1


# -------DECISION OF WHAT WILL BE THE RESULT----------#
def results(result):
    if result == 1:
        print("You Won! Computer choose", computer, "and you choose", human)
    elif result == -1:
        print("You Lost! Computer choose", computer, "and you choose", human)
    else:
        print("You Draw! Computer choose", computer, "and you choose", human)


# ------------TAKING INPUT FROM THE USER----------------#
human = input(
    "\n\n\t\t\t\tWELCOME TO SNAKE WATER GUN GAME\n\nSNAKE='s'\nWATER='w'\nGUN='g'\n\nEnter your choice here : "
)
result = int(decide(computer, human))
results(result)
