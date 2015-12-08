#I solved the Lowest Unique Number challenge on @codeeval. http://www.codeeval.com/browse/103
import sys
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
    inputList = inputLine.strip().split(" ");
    originalList = list(inputList);

    for i in range (0, len(inputList)):
        if (inputList.count(inputList[i]) != (0 or 1)):
            originalList.remove(inputList[i]);
        
    originalList.sort();
    placeToSave = 0;
    if (len(originalList) !=0):
        placeToSave = 0;
        for i in range (0,len(inputList)):
            if (inputList[i] == originalList[0]):
             placeToSave = i + 1;
    print(placeToSave);
    
test_cases.close()
