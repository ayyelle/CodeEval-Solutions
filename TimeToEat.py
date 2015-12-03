#I solved the 'Time to eat' challenge on @codeeval. http://www.codeeval.com/browse/214

import sys
test_cases = open(sys.argv[1], 'r')
for stringInput in test_cases:
    newList = stringInput.strip().split(" ");

    newList.sort(reverse = True);
    outputString = "";
    for i in range (0,len(newList)):
        outputString += newList[i] + " ";
    
    print (outputString.strip());

test_cases.close()
