#imports
import pygame

#initialize pygame
pygame.init()


#window info
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pokemon Demo')


#Colors
white=(255,255,255)
black=(0,0,0)
purple=(55,25,137)

#load textures
TexGrass = pygame.image.load('GrassTexture.png')

#texture dimensions
TexGrassWidth=50
TexGrassHeight=50

#other variables
originX=0
originY=0

def renderTextureWholeScreen(textureHeight, textureWidth, texture):
    maxTexturesX=int(display_width/textureWidth)
    maxTexturesY=int(display_height/textureHeight)

    maxTextures=maxTexturesX*maxTexturesY

    startX=originX
    startY=originY
    
    for y in range(0, maxTexturesY):
        for x in range(0, maxTexturesX):
            gameDisplay.blit(texture, (startX, startY))
            startX+=textureHeight
        startY+=textureHeight
        startX=originX

def renderTextureLine(rangeStart, rangeEnd, texture, startX,startY, startXIncrease, startYIncrease):
    for x in range(rangeStart, rangeEnd):
        gameDisplay.blit(texture, (startX,startY))
        startX+=startXIncrease
        startY+=startYIncrease

def game_loop():

    #game run bool
    gameExit=False

    #game loop
    while not gameExit:

        #input checking
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            #if event.type==pygame.KEYDOWN:
                
        gameDisplay.fill(white)
        #rangeStart, rangeEnd, texture, startX,startY, startXIncrease, startYIncrease
        #renderTextureLine(0,int(display_width/TexGrassWidth), TexGrass, originX, originY, TexGrassWidth, 0)

        #textureHeight, textureWidth, texture
        renderTextureWholeScreen(TexGrassWidth, TexGrassHeight, TexGrass)
        pygame.display.update()
        
game_loop()
pygame.quit()
quit()
