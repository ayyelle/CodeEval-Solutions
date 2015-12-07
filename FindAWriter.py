#I solved the Find a Writer challenge on @codeeval. http://www.codeeval.com/browse/97

import sys
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
    splitList = inputString.strip().split("|");
    firstItem = splitList[0].strip();
    secondItem = splitList[1].strip().split(" ");
    stringToPrint = "";

    for number in secondItem:
        value = int(number);
        stringToPrint += firstItem[value -1];
    
    print(stringToPrint).strip();

test_cases.close()
