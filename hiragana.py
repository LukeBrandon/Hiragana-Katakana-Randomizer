import random

# The indexes of all of these arrays should always line up
controller = [0,0,0,0,0]
controllerNames=["Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4", "Lesson 5"]
values = [[["a", "あ"], ["i", "い"], ["u", "う"], ["e", "え"], ["o", "お"], 
                            ["ka", "か"], ["ki", "き"], ["ku", "く"], ["ke", "け"], ["ko", "こ"], 
                            ["sa", "さ"], ["shi", "し"], ["su", "す"], ["se", "せ"], ["so", "そ"]], 
        [["ta", "た"], ["chi", "ち"], ["tsu", "つ"], ["te", "て"], ["to", "と"],
                             ["na", "な"], ["ni", "に"], ["nu", "ぬ"], ["ne", "ね"], ["no", "の"], 
                             ["ha", "は"], ["hi", "ひ"], ["fu", "ふ"], ["he", "へ"], ["ho", "ほ"]],
        [["ma", "ま"], ["mi", "み"], ["mu", "む"], ["me", "め"], ["mo", "も"], 
                            ["ya", "や"], ["yu", "ゆ"], ["yo", "よ"], 
                            ["ra", "ら"], ["ri", "り"], ["ru", "る"], ["re", "れ"], ["ro", "ろ"], 
                            ["wa", "わ"], ["o(weird)",""], ["n", "ｎ"]], 
        [["ga", "が"], ["gi", "ぎ"], ["gu", "ぐ"], ["ge", "げ"], ["go", "ご"], 
                            ["za", "ざ"], ["ji", "じ"], ["zu", "ず"], ["ze", "ぜ"], ["zo", "ぞ"]], 
        [["da", "だ"], ["dji","ぢ"], ["dzu", "づ"], ["de", "で"], ["do", "ど"], \
                            ["ba", "ば"], ["bi", "び"], ["bu", "ぶ"], ["be", "べ"], ["bo", "ぼ"], 
                            ["pa", "ぱ"], ["pi", "ぴ"], ["pu", "ぷ"], ["pe", "ぺ"], ["po", "ぽ"]]]

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
        input(combinedArray[i][0])
        input(combinedArray[i][1])

print("Get ready to practice some Hiragana!!")
whichCharacters()
beginTesting()
