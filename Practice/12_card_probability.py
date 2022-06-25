import random


def transform(gcs):
    for i in range(len(gcs) - 1):
        if gcs[i] == 1:
            gcs[i] = 0
            if gcs[i + 1] == 1:
                gcs[i + 1] = 0
            else:
                gcs[i + 1] = 1
    return gcs


"""
Explanation :-
    
    lets suppose the list we get is [1,0,0,1]
    
    length of our list is 4 but as we can't find the right to it index value(5th) so thats why we have to take 4-1=3 where right side of 3rd index is 4th
    
    round 1-
        the code checks if list[0] is 1 or not
        if yes then change it to 0 and do the opposit of what is thier in the right of it i.e index 1
        
        So after the completion of the first round our list looks like this --> [0101]
    round 2-
        looks like this --> [0011]
    round 3-
        looks like this --> [0000]
    and then in the for loop exits and returns the modified/final list to print

"""

if __name__ == "__main__":
    generated_card_sequence = []
    n = int(input("Enter the value of  n : "))

    # randomly generates a list with n length
    for i in range(n):
        generated_card_sequence.append(random.randint(0, 1))

    # prints the randomly generated list
    print("List : ", generated_card_sequence)

    print(transform(generated_card_sequence))
