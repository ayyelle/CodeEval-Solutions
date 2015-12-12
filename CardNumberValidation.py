#I solved the Card number validation challenge on @codeeval. http://www.codeeval.com/browse/172
import sys
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
    inputLine.strip();
    listOfNumbers = [];
    for character in inputLine:
        if (character.isdigit()):
            listOfNumbers.append(character);
        
    multiply = False;
    sumTotal = 0;
    for num in reversed(listOfNumbers):
        numberToAdd = int(num);
        if (multiply != True):
            sumTotal += numberToAdd;
            multiply = True;
        else:
            doubling = str(numberToAdd*2);
            double = int(doubling);
            newList = [];
            if (double > 9):
                for char in doubling:
                    sumTotal += int(char);
                    newList.append(char);    
            else:
                sumTotal += double;
            multiply = False;
    if (sumTotal % 10 == 0):
        print "1";
    else:
        print "0";

test_cases.close()
