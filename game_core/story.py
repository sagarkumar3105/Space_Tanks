import pygame
import sys
import time
from game_core import constants
from game_core.game_manager import GameManager


class Story:
    def __init__(self):
        self.msg='''Commander!\nIt's a great relief that you joined. On our voage to a new home.We encounter a group of humanoid. We are now left with a small fleet and there's no chance to retret.'''
        self.game_display = pygame.display.set_mode((constants.display_width, constants.display_height))
        self.clock = pygame.time.Clock()
        self.img=pygame.image.load("assets/images/warfield.jpg").convert_alpha()
        self.story_font = pygame.font.Font("assets/fonts/digital.ttf", 20)
        self.exit_status=False
        
    def disp(self,str):
        x=0
        y=10  
        for i in str:
            pygame.event.clear()

            time.sleep(0.05)
            if(i=="\n"):
                y+=25
                x=0
                continue
            text = self.story_font.render(i, False, (2, 241, 16), (0, 0, 0))
            textrect = text.get_rect(topleft=(x, y))
            x+=15
            if(not(x<constants.display_width)):
                y+=25
                x=0           
            self.game_display.blit(text, textrect)
            pygame.display.update()

        self.game_display.fill(constants.black)     
        self.img_rect = self.img.get_rect()
        self.img_rect.center = constants.display_width//2, constants.display_height//2                

        self.game_display.blit(self.img,self.img_rect)
        pygame.display.update()
            
            
    def show_message(self):
        self.disp(self.msg)
    
    def run(self):
        #self.game_display.fill(black)
        self.show_message()
        start_flag=0
        while(not start_flag):
            for event in pygame.event.get():    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start_flag=1
                        break
        if start_flag==1:        
            GameManager(constants.players_number, constants.tanks_number).run()
