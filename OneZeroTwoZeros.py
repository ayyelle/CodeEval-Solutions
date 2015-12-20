#I solved the One zero, two zeros... challenge on @codeeval.http://www.codeeval.com/browse/217
import sys
test_cases = open(sys.argv[1], 'r')
for inputString in test_cases:
    inputBreak = inputString.strip().split(" ");
    if len(inputBreak) == 0:
        break;
    numberOfZeros =int(inputBreak[0]);
    lastNumber = int(inputBreak[1]);
    countOf = 0;

    for i in range(1,lastNumber+1):
        binaryVersion = '{0:b}'.format(i);
        zeroCounts = binaryVersion.count("0");
        if (zeroCounts == numberOfZeros):
            countOf +=1;
    print(countOf);

test_cases.close()
