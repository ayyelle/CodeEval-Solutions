#I solved the Self Describing Numbers challenge on @codeeval. http://www.codeeval.com/browse/40

import sys
def selfDescribe(inputValue):
    selfDes = 1;
    for i in range(0,len(inputValue)):
        count = int(inputValue[i]);
        numberToCount = str(i);
        countNumberOf = inputValue.count(numberToCount);
        if (count == countNumberOf):
            selfDes = 1;
        else:
            selfDes = 0;
            return selfDes;
    return selfDes;
    
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
    inputString = inputLine.strip();
    print(selfDescribe(inputString));
    
test_cases.close()
