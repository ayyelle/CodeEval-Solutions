#I solved the Beautiful Strings challenge on @codeeval.http://www.codeeval.com/browse/83

import sys
test_cases = open(sys.argv[1], 'r')
for inputString in test_cases:
    inputString.strip();
    letters = [];
    letterCount = {};
    for character in inputString:
        if (character.isalpha()):
            letters.append(character.lower());
        
    for item in letters:
        if (item not in letterCount.keys()):
            letterCount[item] = 1;
        else:
            letterCount[item] +=1;

    values = letterCount.values();
    multiple = 26;
    sumTotal = 0;

    values.sort(reverse= True);

    for integer in values:
        m = integer*multiple
        sumTotal +=m;
        multiple = multiple - 1;
    print(sumTotal);

test_cases.close()
