print("\n<<<<< Hands on #2 >>>>>")
import random
problems = int(input("How many math problems would you like to practice? "))
counter=0
numberCorrect=0
while counter < problems:
    randNumber1 = random.randrange(1,1000)
    randNumber2 = random.randrange(1,1000)
    correctAnswer=int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"Question: {randNumber1} + {randNumber2} = "))
    if correctAnswer==yourAnswer:
        print(" - Correct!")
        numberCorrect +=1
    else:
        print(f" - Incorrect, the correct answer is {correctAnswer}")
    counter +=1

print(f"You answered {numberCorrect}/{counter} questions correctly!")
print(" - Thanks for playing!\n")