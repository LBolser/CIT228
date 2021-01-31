print("\n<<<<< Hands on #2 >>>>>")
import random
prompt = "Would you like another problem? \n Enter 'q' to quit: "
keepPlaying=""
numberCorrect=0
questions=0
while keepPlaying != "q":
    randNumber1 = random.randrange(1,1000)
    randNumber2 = random.randrange(1,1000)
    correctAnswer=int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"Question: {randNumber1} + {randNumber2} = "))
    if correctAnswer==yourAnswer:
        print(" - Correct!")
        numberCorrect +=1
    else:
        print(f" - Incorrect, the correct answer is {correctAnswer}")
    questions +=1
    keepPlaying = input(prompt)

print(f"\nYou answered {numberCorrect}/{questions} questions correctly!")
print(" - Thanks for playing!\n")