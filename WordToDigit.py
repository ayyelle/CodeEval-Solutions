#I solved the Word to Digit challenge on @codeeval. http://www.codeeval.com/browse/104
import sys
test_cases = open(sys.argv[1], 'r')
numberDictionary = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9};
for inputLine in test_cases:
    inputStripped = inputLine.strip().split(";");
    stringOut = "";
    for word in inputStripped:
        stringOut += str(numberDictionary[word]);

    print (stringOut.strip());
test_cases.close()
