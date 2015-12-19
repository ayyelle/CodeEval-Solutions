#I solved the Hidden Digits challenge on @codeeval. http://www.codeeval.com/browse/122
import sys
test_cases = open(sys.argv[1], 'r')
for inputString in test_cases:
    inputString.strip();
    dictionaryValues = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9}
    listofKeys = dictionaryValues.keys();
    outputString="";

    for character in inputString:
        if (character in listofKeys):
            outputString +=str(dictionaryValues[character]);
        elif(character.isdigit()):
            outputString +=character;
    if (len(outputString) ==0):
        outputString = "NONE";
    print outputString;

test_cases.close()
