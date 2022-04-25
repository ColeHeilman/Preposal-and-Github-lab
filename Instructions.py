import pygame
import sys
pygame.init()


    
display = pygame.display.set_mode((800,800))
pygame.display.set_caption('Instruction Screen')



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
                    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                        pygame.quit()

        mouse = pygame.mouse.get_pos()
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            pygame.draw.rect(display,color_light,[width/2,height/2,140,40])
        else:
            pygame.draw.rect(display,color_dark,[width/2,height/2,140,40])
        display.blit(buttonText,(width/2+50,height/2))
        pygame.display.update()


                
Instruction()              
            




