#I solved the Lettercase Percentage Ratio  challenge on @codeeval.http://www.codeeval.com/browse/147
import sys
test_cases = open(sys.argv[1], 'r')
for inputString in test_cases:
    lowerCounter = 0;
    upperCounter = 0;
    lengthOfWord = len(inputString.strip());

    for letter in inputString.strip():
        if (letter == letter.lower()):
            lowerCounter +=1;
        else:
            upperCounter +=1;
        
    lowerRatio = float(lowerCounter)/float(lengthOfWord);
    upperRatio = float(upperCounter)/float(lengthOfWord);
    lowerRatio = lowerRatio*100;
    upperRatio = upperRatio*100;

    lowerRatioString ="lowercase: "+ "%0.2f" % lowerRatio;
    upperRatioString = "uppercase: " + "%0.2f" % upperRatio;
    finalString = lowerRatioString +" "+ upperRatioString
    print(finalString.strip());
   

test_cases.close()
