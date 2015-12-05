#I solved the Testing challenge on @codeeval.http://www.codeeval.com/browse/225
import sys
test_cases = open(sys.argv[1], 'r')
for inputLine in test_cases:
  inputString.strip();
  newList = inputString.split(" | ");

  leftSide = newList[0];
  rightSide = newList[1];
  differences = 0;

  for i in range (0,len(leftSide)):
      if (leftSide[i] != rightSide[i]):
          differences +=1;

  if (differences ==0):
      print("Done")
  elif (differences <=2):
      print ("Low");
  elif(3 <= differences <=4):
      print("Medium");
  elif(5 <=differences <=6):
      print("High");
  elif(differences > 6):
      print ("Critical");
test_cases.close()
