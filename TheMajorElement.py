#I solved the The Major Element challenge on @codeeval. http://www.codeeval.com/browse/132
import sys
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
    counterDictionary = {};
    found = False;

    newList = inputLine.strip().split(",");
    lengthOfList = len(newList);
    for item in newList:
        if (item not in counterDictionary.keys()):
            counterDictionary[item] = 1;
        else:
            counterDictionary[item] +=1;

    for key in counterDictionary:
        value = counterDictionary[key];
        if (value > lengthOfList/2):
            found = True;
            print(key);
            
            
    if (found == False):
        print("None");

test_cases.close()
