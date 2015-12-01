# I solved the Remove Characters challenge on @codeeval.  http://www.codeeval.com/browse/13
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    splitArray = test.split(",");

    word = splitArray[0].strip();

    takeway = splitArray[1].strip();

    for letter in takeway:
        for otherLetter in word:
            if (otherLetter == letter):
                word=  word.replace(otherLetter,"");

    print(word);

test_cases.close()
