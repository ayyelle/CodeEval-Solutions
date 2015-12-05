#I solved the Trick or Treat challenge on @codeeval. http://www.codeeval.com/browse/220
import math
import sys
test_cases = open(sys.argv[1], 'r')
for inputString in test_cases:

    inputString.strip();
    newList = inputString.strip().split(",");
    V= 3;
    Z = 4;
    W = 5;

    dictionary = {};
    for i in range (0,len(newList)):
        selfList = newList[i].split(":");
        dictionary[selfList[0].strip()] = int(selfList[1]);
    
    totalCandies = 0;
    houseNumber=0;
    totalKids = 0;

    for key in dictionary:
        numberOfKids  = dictionary[key];
        if (key != "Houses"):
            totalKids += numberOfKids
        if (key == "Vampires"):
            totalCandies +=V*numberOfKids;
        elif(key == "Zombies"):
            totalCandies +=Z*numberOfKids;
        elif(key == "Witches"):
            totalCandies +=W*numberOfKids;
        else: 
            houseNumber = numberOfKids;
        
    totalCandies = totalCandies*houseNumber;        
    division = totalCandies/totalKids;
    roundedNumber = math.floor(division);
    print(int(roundedNumber));

test_cases.close()
