import random

# The indexes of all of these arrays should always line up
controller = [0,0,0,0,0]
controllerNames=["Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4", "Lesson 5"]
values = [[["a", "あ ア"], ["i", "い イ"], ["u", "う ウ"], ["e", "え エ"], ["o", "お オ"], 
                            ["ka", "か カ"], ["ki", "き キ"], ["ku", "く ク"], ["ke", "け ケ"], ["ko", "こ コ"], 
                            ["sa", "さ サ"], ["shi", "し シ"], ["su", "す ス"], ["se", "せ セ"], ["so", "そ ソ"]], 
        [["ta", "た タ"], ["chi", "ち チ"], ["tsu", "つ ツ"], ["te", "て テ"], ["to", "と ト"],
                             ["na", "な ナ"], ["ni", "に ニ"], ["nu", "ぬ ヌ"], ["ne", "ね ネ"], ["no", "の ノ"], 
                             ["ha", "は ハ"], ["hi", "ひ ヒ"], ["fu", "ふ フ"], ["he", "へ ヘ"], ["ho", "ほ ホ"]],
        [["ma", "ま マ"], ["mi", "み ミ"], ["mu", "む ム"], ["me", "め メ"], ["mo", "も モ"], 
                            ["ya", "や ヤ"], ["yu", "ゆ ユ"], ["yo", "よ ヨ"], 
                            ["ra", "ら ラ"], ["ri", "り リ"], ["ru", "る ル"], ["re", "れ レ"], ["ro", "ろ ロ"], 
                            ["wa", "わ ワ"], ["o(weird)",""], ["n", "ん ン"]], 
        [["ga", "が ガ"], ["gi", "ぎ ギ"], ["gu", "ぐ グ"], ["ge", "げ　ゲ"], ["go", "ご　ゴ"], 
                            ["za", "ざ　ザ"], ["ji", "じ　ジ"], ["zu", "ず　ズ"], ["ze", "ぜ　ゼ"], ["zo", "ぞ　ゾ"]], 
        [["da", "だ　ダ"], ["dji","ぢ"], ["dzu", "づ"], ["de", "で　デ"], ["do", "ど　ド"],
                            ["ba", "ば　バ"], ["bi", "び　ビ"], ["bu", "ぶ　ブ"], ["be", "べ　ベ"], ["bo", "ぼ　ボ"], 
                            ["pa", "ぱ　パ"], ["pi", "ぴ　ピ"], ["pu", "ぷ　プ"], ["pe", "ぺ　ペ"], ["po", "ぽ ポ"]]]

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
    i = 0
    while i < len(combinedArray):
        input(combinedArray[i][0])
        input(combinedArray[i][1])
        i += 1

print("Get ready to practice some Hiragana/Katakana!!")
whichCharacters()
beginTesting()
