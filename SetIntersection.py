#I solved the Set Intersection challenge on @codeeval. http://www.codeeval.com/browse/30

import sys
test_cases = open(sys.argv[1], 'r')
for inputString in test_cases:
    inputString.strip();
    newList = inputString.strip().split(";");

    leftSide = newList[0].split(",");
    rightSide = newList[1].split(",");

    similarArray = similarArray = list(set(leftSide).intersection(rightSide));
    similarArray.sort();
    newString = ','.join(similarArray);

    print(newString.strip());

test_cases.close()
