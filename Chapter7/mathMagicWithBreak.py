print("\n<<<<< Hands on #2 >>>>>\n")
import random
counter=0
numberCorrect=0
numberIncorrect=0
while counter < 10:
    randNumber1 = random.randrange(1,1000)
    randNumber2 = random.randrange(1,1000)
    correctAnswer=int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"Question: {randNumber1} + {randNumber2} = "))
    if correctAnswer==yourAnswer:
        print(" - Correct!")
        numberCorrect +=1
    else:
        print(f" - Incorrect, the correct answer is {correctAnswer}")
        numberIncorrect +=1
        if numberIncorrect==5:
            print("\n***You need to meet with a tutor.***")
            counter+=1
            break
    counter +=1

print(f"You answered {numberCorrect}/{counter} questions correctly!")
print(" - Thanks for playing!\n")