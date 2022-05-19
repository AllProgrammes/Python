#------------SIMPLE DICTIONARY---------------#
myDict = {"Shreya": "My Girlfriend", "Love": "Shreya"}
print(myDict["Love"])
print(myDict["Shreya"])

#------------NESTED DICTIONARY---------------#
mylife={
    "Life":
        {
         "Goal":"BCA",
         "Class Done":[1,2,3,4,5,6,7,8,9,10,11,12],
         "Shreya":
             {
                 "Partner":"Future Wife"
             }
        }
    }
print(mylife["Life"]["Shreya"]["Partner"])
print(mylife["Life"]["Class Done"])