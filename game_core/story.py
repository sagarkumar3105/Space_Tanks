import pygame
import sys
import time
from game_core import constants
from game_core.game_manager import GameManager

class Story:
    def __init__(self):
        self.msg='''Commander!\nIt's a great relief that you joined. Humankind has reached its new home, planet Kepler-1606b. It is one among a few other habitable planets of the universe. Our ships had just landed a few weeks ago on the surface when we found a fleet of warships invading the atmosphere. We thought it was a fleet of refugees like us. In the beginning they seemed very cordial and were a collation of human-like spicies. We shared our few resources with them. But one day they received a signal from a very distant source. Before that transmission we were sharing the planet with harmony but few months later we found their true identity. They were a group of space-pirates that plundered different planets and use them as a temporary homestead while they consumed the resources and stole most of it. Our chief warnde them and thretended them to retret but they declared a war againsr us. Thanks to the almighty we had a small fleet to protect ourselves from unknown galactic enemies. But now it seems very difficult to win against them as few days ago one of their fleets invaded the planet and attacked on our defense systems. Not only this, they seem to uses some unknown source of energy. They replicated our weapons, machines and everything and are now using it against us. They enemy has grown very powerful but now we will have to somehow win against them. \n\n\n\n\n\n       It's a war of civilizations and we can't retreat. This is our last hope of survival.\n       Commander we believe with you on our side, we may win the war.'''
        
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

            time.sleep(0.01)
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
        time.sleep(5)
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
