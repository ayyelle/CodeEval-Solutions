#I solved the Mth to last element challenge on @codeeval. http://www.codeeval.com/browse/10
import sys
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
    if (inputLine != ""):
        newList = inputLine.strip().split(" ");
        lengthOfList = len(newList) - 1;
        numberToFind = int(newList[lengthOfList]);
        reversedList = [];
        if (len(newList) > numberToFind):
            for i in reversed(newList):
                reversedList.append(i);
        print(reversedList[numberToFind]);


test_cases.close()
