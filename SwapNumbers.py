#I solved the Swap Numbers challenge on @codeeval.http://www.codeeval.com/browse/196
import sys
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
    listLine = inputLine.strip().split(" ");
    newList = [];
    for stringValue in listLine:
        first = stringValue[0];
        lengthOfString = len(stringValue);
        last = stringValue[lengthOfString-1];
        newString = last+stringValue[1:lengthOfString-1]+first;
        newList.append(newString);
    
    print " ".join(newList).strip();

test_cases.close()
