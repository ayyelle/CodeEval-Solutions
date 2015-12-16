#I solved the Pangrams challenge on @codeeval. http://www.codeeval.com/browse/37
import sys
test_cases = open(sys.argv[1], 'r')
for inputString in test_cases:
    alphaList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
    stringOutput="";

    line = inputString.strip().lower();
    for value in alphaList:
        if (value not in line):
            stringOutput += value;

    if (len(stringOutput)) == 0:
        stringOutput = "NULL";
    print(stringOutput);

test_cases.close()
