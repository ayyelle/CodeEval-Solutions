#I solved the Simple or trump challenge on @codeeval. http://www.codeeval.com/browse/235

def trumper(inputLine):
    cardDictionary= {"2":"1","3":"2","4":"3","5":"4","6":"5","7":"6","8":"7","9":"8","10":"9","J":"10","Q":"11","K":"12","A":"13"}
    inputLine = inputLine.strip();
    separatedPipe = inputLine.split(" | ");
    justCards = separatedPipe[0].strip().split(" ");
    justCards1 = justCards[0];
    justCards2 = justCards[1];
    trumpSuite = separatedPipe[1].strip();
    card11 = False;
    card22 = False;
    
    if (len(justCards1) ==2):
        card = justCards1[0];
        suit = justCards1[1]
    else:
        card = justCards1[0]+justCards1[1]
        suit = justCards1[2]
    cardPlace1 = int(cardDictionary[card])
    #suitPlace1 = suitDictionary[suit];
    
    if (len(justCards2) ==2):
        card2 = justCards2[0];
        suit2 = justCards2[1]
    else:
        card2 = justCards2[0]+justCards2[1]
        suit2 = justCards2[2]
    cardPlace2 = int(cardDictionary[card2])
    #suitPlace2 = suitDictionary[suit];
    
    if (suit == trumpSuite):
        card11 = True;
    elif (suit2 == trumpSuite):
        card22 = True;
    
    if (card11 and card22):
        return separatedPipe[0].strip();
    elif (card11):
        return justCards1;
    elif (card22):
        return justCards2;
    else:
        if (cardPlace1 > cardPlace2):
            return justCards1;
        elif (cardPlace2 > cardPlace1):
            return justCards2;
        else:
            return separatedPipe[0].strip();
