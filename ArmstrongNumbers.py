#I solved the Armstrong Numbers challenge on @codeeval. http://www.codeeval.com/browse/82

import sys
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
    inputValue = inputLine.strip();
    lengthOfInput = len(inputValue);
    totalSum = 0;

    for value in inputValue:
        totalSum += pow(int(value), lengthOfInput);
    
    if totalSum == int(inputValue):
        print ("True");
    else:
        print("False");
    
test_cases.close()
