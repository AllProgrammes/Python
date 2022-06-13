name = "Biswajit Mishra"
live_in = "Earth"
age = 19
# details="I am {name}\nI live on {live_in} \nI am {age} yrs old"
# details = "I am {}\nI live on {} \nI am {} yrs old".format(name, live_in, age) --> same as line 4
"""
what if we write like this ?
details = "I am {}\nI live on {} \nI am {} yrs old".format(live_in,name, age)

Then the output will become a blunder like this :-
I am Earth
I live on Biswajit Mishra 
I am 19 yrs old


but but we have a solution for this don't worry :) see line 18 
"""
details = "I am {1}\nI live on {0} \nI am {2} yrs old".format(live_in, name, age)
# Output :-
# I am Biswajit Mishra
# I live on Earth
# I am 19 yrs old
print(details)
