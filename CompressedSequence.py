#I solved the Compressed Sequence challenge on @codeeval. http://www.codeeval.com/browse/128
import sys
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
    splitList = inputLine.strip().split(" ");
    stringToOutput = "";
    listOfPairs = [];
    currentItem = splitList[0];
    count = 0;
    for i in range (0,len(splitList)):
        item = splitList[i];
        if (item == currentItem):
            count +=1;
        else:
            lastOutput = currentItem;
            stringOut = str(count)+" "+lastOutput;
            listOfPairs.append(stringOut);
            currentItem = item;
            count = 1;
        if (i == (len(splitList)-1)):
            lastOutput = currentItem;
            stringOut = str(count)+" "+lastOutput;
            listOfPairs.append(stringOut);

    stringToOutput = " ".join(listOfPairs);
    print (stringToOutput.strip());

test_cases.close()
