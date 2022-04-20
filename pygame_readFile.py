import random

file = open("Trivia questions.txt","r")
data = file.read()
lst = data.split(",")

aQuest = []
qQuest = []
questions = {}
count = 0
for item in lst:
    if len(item) > 20:
        qQuest.append(item)
        count += 1
        answer = lst[count]
        questions[item] = answer
        aQuest.append(answer)
    else:
        count += 1
   
def findRandom(aQuest,qQuest):
    score = 0
    while score < 10:
        theQuest = random.choice(qQuest)
        guess = input(theQuest)
        guess.lower()
        qQuest.remove(theQuest)
        if guess in aQuest:
            print("Correct")
            score += 1
            print("Score:",score)
        else:
            print("Correct answer: ",questions[theQuest])
            print("Incorrect")
    print("You Win!")

findRandom(aQuest,qQuest)




