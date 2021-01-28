import random
number = random.randrange(10,100)
numList = list(range(number))
print(numList)
print("The max is: ", max(numList))
print("The min is: ", min(numList))
print("The sum is: ", sum(numList))
print("The average is: ", sum(numList)/len(numList))