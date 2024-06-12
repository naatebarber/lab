# I want to assign people to bring food to a potluck.
# I want to do this randomly, so nobody gets the same assignment twice.

# Read in a list of foods from input

foods = input("give me a list of foods, like (bacon, eggs, etc): ")
people = input("give me a list of peoples names, like (timothee, derek, qiqi): ")

# split our input strings by comma to turn them into a list of people / food

foods_split_by_comma = foods.split(",")
people_split_by_comma = people.split(",")

# import random so we can shuffle the lists of food and people

import random

# shuffle the list of fooeds
# we do this so we get a random food assignment each time

random.shuffle(foods_split_by_comma)

# make a dictionary to save a person (key) with a list of foods they need to bring to the potluck (value)
# we start with an empty dictionary

potluck_assignment = {}

# now let's loop over every person in the shuffled_people list and assign foods
# every time we assign a food, we remove it from the shuffled foods list.

# loop until there are no foods left to assign
while len(foods_split_by_comma) > 0:
    # loop over every person
    for person in people_split_by_comma:
        # pull a food item out of the list
        # and assign it to the variable 'food'
        # if theres no more food, we're done.
        if len(food) == 0:
            break

        food = foods_split_by_comma.pop()

        # Check if the person is in the dictionary yet
        if person in potluck_assignment:
            # if they are, add a food to their list
            potluck_assignment[person].append(food)
        else:
            # if they are not in the dictionary,
            # add their name as a key, along with a foods list
            # containing the current food
            potluck_assignment[person] = [food]


# print out the assignment

for person, foods in potluck_assignment.items():
    print(person, "should bring", foods)
