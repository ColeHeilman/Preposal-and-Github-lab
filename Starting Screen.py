


import pygame
from pygame import mixer
import random
import sys

pygame.init()

display = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()



file = open("Trivia questions.txt","r")
data = file.read()
lst = data.split(",")

aQuest = []
qQuest = []
questions = {}
count = 0
for item in lst:
    if len(item) >= 23:
        qQuest.append(item)
        count += 1
        answer = lst[count]
        questions[item] = answer
        aQuest.append(answer)
    else:
        count += 1
score = 0

counter, text = 90,'90'.rjust(3)
def MainScreen(aQuest,qQuest,counter, text,score):

    mixer.init()

    themeSong = pygame.mixer.Sound("suspensemusic.wav")
    correct = pygame.mixer.Sound('CorrectA.wav')
    incorrect = pygame.mixer.Sound('IncorrectA.wav')


    questFont = pygame.font.Font(None, 25)
    base_font = pygame.font.Font(None,32)
    user_text = ""
    input_rect = pygame.Rect(200,700,140,32)
    color_active = pygame.Color("Blue")
    color_passive = pygame.Color("Red")
    color = color_passive


    
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

   

    theQuest = random.choice(qQuest)

    
    active = True

    while active:
        
        



        total = str(score)

        display.fill((0,0,0))
        display.blit(font.render(text,True, (255,0,0)), (400,50))
        display.blit(font.render('number correct', True, (255,0,0)), (50,50))
        display.blit(font.render("Answer:", True, (255,0,0)), (50,700))
        display.blit(font.render(total,True,(255,0,0)), (100,100))
        display.blit(font.render('Question:',True, (255,0,0)), (50,300))
        
        pygame.draw.rect(display,(255,0,0), (220,300,550,30),2)
        display.blit(questFont.render(theQuest, True, (255,0,0)), (225,305))

        pygame.draw.rect(display,color,input_rect,2)
        text_surface = base_font.render(user_text,True,(0,255,0))
        display.blit(text_surface,(input_rect.x + 5,input_rect.y + 5))
        input_rect.w = max(100,text_surface.get_width() + 10)
        pygame.display.flip()
        clock.tick(60)

        
       


        for event in pygame.event.get():
            

            
           
            if event.type == pygame.USEREVENT:
                counter -= 1


                
                if counter > 0:
                    text = str(counter).rjust(3) 
                
                    
            if counter == 0:
                mixer.Sound.play(incorrect)
                
            if counter < 0:
                mixer.Sound.stop(incorrect)
                ('BOOM!'), pygame.quit()
                quit()

                    
           

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_c or event.key == pygame.K_d or event.key == pygame.K_e or event.key == pygame.K_f or event.key == pygame.K_g or event.key == pygame.K_h or event.key == pygame.K_i or event.key == pygame.K_j or event.key == pygame.K_k or event.key == pygame.K_a or event.key == pygame.K_l or event.key == pygame.K_m or event.key == pygame.K_n or event.key == pygame.K_o or event.key == pygame.K_p or event.key == pygame.K_q or event.key == pygame.K_r or event.key == pygame.K_s or event.key == pygame.K_t or event.key == pygame.K_u or event.key == pygame.K_v or event.key == pygame.K_w or event.key == pygame.K_x or event.key == pygame.K_y or event.key == pygame.K_z:
                        user_text+=str(chr(event.key))
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_SPACE:
                        user_text +=  " "
                    elif event.key == pygame.K_RIGHT:
                        if user_text in aQuest:
                            score+=1
                            if score > 2:
                                pygame.quit()
                                sys.exit()
                            MainScreen(aQuest,qQuest,counter, text,score)
                          
                        else:
                            display.blit(font.render("YOU LOSE", True, (255,0,0)), (350,100))
                            pygame.time.wait(1000)
                            pygame.quit()
                            sys.exit()

                    else:
                        user_text += event.unicode

           

                
               
            
            
       

            
        











def Instruction():

    width = display.get_width()
    height = display.get_height()
    s = (600,600)
    color_white = (225,255,255)
    color_light = (180,180,180)
    color_dark = (110,110,110)
    smallfont = pygame.font.SysFont("Timesnewroman", 20)
    buttonText = smallfont.render("Start", True, color_white)

        


    while True:
        for i in pygame.event.get():
            
            display.fill((0,0,0))
                
            titlefont = pygame.font.SysFont('arial',50)
            title = titlefont.render("How to Play",True,(0,225,0))
            
            
            display.blit(title,(275,25))

            
            font = pygame.font.SysFont('arial',25)

            line1 = font.render("You're mission is to diffuse the bomb before time runs out.",True,(0,225,0))
            line2 = font.render("You will have 60 seconds to answer 10 questions correctly.",True,(0,225,0))
            line3 = font.render("If either you answer incorrectly or,  misspell your answer,",True,(0,225,0))
            line4 = font.render("the bomb will automatically detonate.",True,(0,225,0))
            line5 = font.render("Both speed and accuracy are needed if you are to succeed,",True,(0,225,0))
            line6 = font.render("in diffusing the bomb.",True,(0,225,0))
            line7 = font.render("Each time you successfully diffuse the bomb,",True,(0,225,0))
            line8 = font.render("you will recieve a point.",True,(0,225,0))
            line9 = font.render("Compete to see who can score the most points.",True,(0,225,0))
            line10 = font.render("Good luck.",True,(0,225,0))

            display.blit(line1,(100,100))
            display.blit(line2,(100,150))
            display.blit(line3,(100,200))
            display.blit(line4,(100,250))
            display.blit(line5,(100,300))
            display.blit(line6,(100,350))
            display.blit(line7,(100,400))
            display.blit(line8,(100,450))
            display.blit(line9,(100,500))
            display.blit(line10,(100,550))

            if i.type == pygame.QUIT:
                pygame.quit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                    if width/2 <= mouse[0] <= width/2+140 and 700 <= mouse[1] <= 740:
                        MainScreen(aQuest,qQuest,counter, text,score)

        mouse = pygame.mouse.get_pos()
        if width/2 <= mouse[0] <= width/2+140 and 700 <= mouse[1] <= 740:
            pygame.draw.rect(display,color_light,[width/2,700,140,40])
        else:
            pygame.draw.rect(display,color_dark,[width/2,700,140,40])
        display.blit(buttonText,(width/2 + 50,700))
        pygame.display.update()











def startingScreen():
    
    pygame.display.set_caption('Starting Screen')  
    background = pygame.image.load("soccer-stuff-182425593.jpeg") 
    font = pygame.font.SysFont("Timesnewroman", 100)  
    text = font.render("String of Bombs", True, (225, 0, 0))
    background = pygame.transform.scale(background,(800,800))
    display = pygame.display.set_mode((800,800))

    pygame.display.update() 
    

    width = display.get_width()
    height = display.get_height()
    s = (600,600)
    color_white = (225,255,255)
    color_light = (180,180,180)
    color_dark = (110,110,110)
    smallfont = pygame.font.SysFont("Timesnewroman", 20)
    buttonText = smallfont.render("Start", True, color_white)

    
    while True:
        for i in pygame.event.get():
            display.blit(background,[0,0])
            display.blit(text,(50,50))

            if i.type == pygame.QUIT:
                pygame.quit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                    Instruction()
        mouse = pygame.mouse.get_pos()
        if width/2 <= mouse[0] <= width/2+240 and height/2 <= mouse[1] <= height/2+40:
            pygame.draw.rect(display,color_light,[width/2,height/2,140,40])
        else:
            pygame.draw.rect(display,color_dark,[width/2,height/2,140,40])
        display.blit(buttonText,(width/2+50,height/2))
        pygame.display.update()

startingScreen()


        
