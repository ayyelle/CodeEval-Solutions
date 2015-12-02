#I solved the 'Longest Word' challenge on @codeeval. http://www.codeeval.com/browse/111

import sys
test_cases = open(sys.argv[1], 'r')
for line in test_cases:
    arrayofWords = line.strip().split(" ");
    longestWordSoFar = "";
    longestLengthSoFar = 0;
    for word in arrayofWords:
        if ((len(word)) > longestLengthSoFar):
            longestLengthSoFar = len(word);
            longestWordSoFar = word;
    print(longestWordSoFar);
    
test_cases.close()
