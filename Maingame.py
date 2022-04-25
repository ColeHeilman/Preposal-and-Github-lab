import pygame,sys
from pygame import mixer
import random

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode([800,800])

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

theQuest = random.choice(qQuest)


def MainScreen():

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


    counter, text = 5,'5'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    active = False

    while True:
        for event in pygame.event.get():
            
            mixer.Sound.play(themeSong)
            
            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else ('BOOM!')
            if counter == 0:
                mixer.Sound.stop(themeSong), mixer.Sound.play(incorrect)
            if counter < 0:
                mixer.Sound.stop(incorrect)
                mixer.Sound.stop(themeSong)

                    
           

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

           

                
               
            
            
        if active:
            color = color_active
        else:
            color = color_passive

            
        display.fill((0,0,0))
        display.blit(font.render(text,True, (255,0,0)), (400,50))

        display.blit(font.render("Answer:", True, (255,0,0)), (50,700))
        display.blit(font.render('Question:',True, (255,0,0)), (50,300))
        pygame.draw.rect(display,(255,0,0), (220,300,550,30),2)
        display.blit(questFont.render(theQuest, True, (255,0,0)), (225,305))
        

        pygame.draw.rect(display,color,input_rect,2)
        text_surface = base_font.render(user_text,True,(0,255,0))
        display.blit(text_surface,(input_rect.x + 5,input_rect.y + 5))
        input_rect.w = max(100,text_surface.get_width() + 10)
        pygame.display.flip()
        clock.tick(60)
        
MainScreen()
