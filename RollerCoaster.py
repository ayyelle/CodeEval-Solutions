#I solved the Roller Coaster challenge on @codeeval. http://www.codeeval.com/browse/156

import sys
test_cases = open(sys.argv[1], 'r')
for line in test_cases:
    finalString = "";
    upperCase = true;
    for letter in line:
        if (letter.isalpha()):
            if (upperCase):
                finalString += letter.upper();
                upperCase = false;
            else:
                finalString += letter.lower();
                upperCase = true;
        else:
            finalString += letter;
    print (finalString);

test_cases.close()
