#I solved the Bit Positions challenge on @codeeval. http://www.codeeval.com/browse/19
import sys
test_cases = open(sys.argv[1], 'r')
for inputString in test_cases:
    inputNumber = inputString.strip().split(",");
    binaryVersion = bin(int(inputNumber[0]));
    index1 = int(inputNumber[1]);
    index2 = int(inputNumber[2]);
    string = binaryVersion[-index1];
    string2 = binaryVersion[-index2];

    if (string == string2):
        print("true");
    else:
        print("false");

test_cases.close()
