#I solved the Clean up the words challenge on @codeeval.http://www.codeeval.com/browse/205

import sys
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
    inputLine = inputLine.strip();
    wasAlpha = True;
    newString = "";

    for character in inputLine:
        if (character.isalpha()):
            newString +=character.lower();
            wasAlpha = True;
        else:
            if (wasAlpha):
                newString+=" ";
                wasAlpha = False;
    print(newString.strip());

test_cases.close()
