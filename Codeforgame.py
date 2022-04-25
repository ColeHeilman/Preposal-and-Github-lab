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


score = 0

done = True
while done and score < 10:
   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_c or event.key == pygame.K_d or event.key == pygame.K_e or event.key == pygame.K_f or event.key == pygame.K_g or event.key == pygame.K_h or event.key == pygame.K_i or event.key == pygame.K_j or event.key == pygame.K_k or event.key == pygame.K_aor event.key == pygame.K_l or event.key == pygame.K_m or event.key == pygame.K_n or event.key == pygame.K_o or event.key == pygame.K_p or event.key == pygame.K_q or event.key == pygame.K_r or event.key == pygame.K_s or event.key == pygame.K_t or event.key == pygame.K_u or event.key == pygame.K_v or event.key == pygame.K_w or event.key == pygame.K_x or event.key == pygame.K_y or event.key == pygame.K_z:
                word+=str(chr(event.key))
            elif event.key == pygame.K_SPACE:
                word += " "
            elif event.key == pygame.K_RETURN:
                if guess in aQuest:
                    score += 1
                else:
                    done = False
