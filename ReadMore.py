#I solved the Read More challenge on @codeeval. http://www.codeeval.com/browse/167
import sys
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
    inputLine.strip();
    lengthOfLine = len(inputLine.strip());
    if (lengthOfLine <=55):
        print(inputLine.strip());
    else:
        subString = inputLine.strip()[0:40].rsplit(' ', 1)[0] + '... <Read More>';
        print(subString);
test_cases.close()
