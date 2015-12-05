#I solved the String mask challenge on @codeeval. http://www.codeeval.com/browse/199

import sys
test_cases = open(sys.argv[1], 'r')
for inputString in test_cases:
    listString = inputString.strip().split(" ");
    wordList = listString[0].strip();
    binaryList = listString[1].strip();

    finalWord = "";
    for i in range(0,len(wordList)):
        if (binaryList[i] == "1"):
            finalWord += wordList[i].upper();
        else:
            finalWord += wordList[i];
    print(finalWord.strip());

test_cases.close()
