#This is not the complete solution, it is missing the opening files part, so it won't 100% compile:

for line in file:
    arrayofWords = line.strip().split(" ");
    longestWordSoFar = "";
    longestLengthSoFar = 0;
    for word in arrayofWords:
        if ((len(word)) > longestLengthSoFar):
            longestLengthSoFar = len(word);
            longestWordSoFar = word;
    print(longestWordSoFar);
