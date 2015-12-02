#I solved the Rightmost Char challenge on @codeeval. http://www.codeeval.com/browse/31
import sys
test_cases = open(sys.argv[1], 'r')
for line in test_cases:
    if (line == ""):
        break;
    else:
        splitLine = line.strip().split(",");
        letterToFind = splitLine[1];
        finalLocation = -1;
        wordToSearch = splitLine[0];
        for i in range (0,len(wordToSearch)):
            if (wordToSearch[i] == letterToFind):
                finalLocation = i;
    print (finalLocation);

test_cases.close()
