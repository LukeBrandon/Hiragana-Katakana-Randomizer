import random

# The indexes of all of these arrays should always line up
controller = [0,0,0,0,0]
controllerNames=["Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4", "Lesson 5"]
values = [["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko","sa", "shi", "su", "se", "so"], ["ta", "chi", "tsu", "te", "to", "na", "ni", "nu", "ne", "no", "ha", "hi", "fu", "he", "ho"],
            ["ma", "mi", "mu", "me", "mo", "ya", "yu", "yo", "ra", "ri", "ru", "re", "ro", "wa", "o(weird)", "n"], ["ga", "gi", "gu", "ge", "go", "za", "ji", "zu", "ze", "zo"], 
            ["da", "dji", "dzu", "de", "do", "ba", "bi", "bu", "be", "bo", "pa", "pi", "pu", "pe", "po"]]

# TODO: Change these to be organized by Lesson 1,2,3,etc. instead of by their leading character

numSets = len(controller)

def askToBoolean(name):
    rawAnswer = input(name + "? y/n -->  ")

    if rawAnswer == 'y' or rawAnswer == 'Y':
        return 1
    elif rawAnswer == 'n' or rawAnswer == 'N':
        return 0
    else:
        print("Please use a valid input (y/n)")
        return askToBoolean(name)


def whichCharacters():
    for i in range(numSets):
        name = controllerNames[i]
        controller[i] = askToBoolean(name)


def beginTesting():
    combinedArray = []
    numSetsTesting = 0

    # Combine the sets that are going to be tested
    for i in range(numSets):
        if(controller[i] == 1):
            combinedArray.extend(values[i])
            numSetsTesting += 1
            print(combinedArray)

    # Randomize the order of the array of testing characters
    random.shuffle(combinedArray)

    # Print out the characters one by one
    for i in range((numSetsTesting*5)):
        input(combinedArray[i])

print("Get ready to practice some Hiragana!!")
whichCharacters()
beginTesting()
