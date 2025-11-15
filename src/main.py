from settings import *
from support import *
from sprites import Player
from groups import *

class Game:
    
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Lantern Boy')
        self.clock = pygame.time.Clock()
        self.running = True
    
        
        
        # groups 
        self.all_sprites = AllSprite()
        self.collision_sprites = pygame.sprite.Group()
        
        self.load_assets()
        
        self.player = Player((0,0),self.all_sprites,self.collision_sprites,self.player_frames)
    
    def load_assets(self):
        #graphics 
        self.player_frames = import_folder('assets','png','idle')
        
        
    def run(self):
        
        while self.running:
            dt = self.clock.tick(FRAMERATE) / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 
                if event.type == pygame.K_RIGHT:
                    self.player_state='walk'
                    
            #update
            self.all_sprites.update(dt)
            
            
            # draw 
            self.display_surface.fill(BG_COLOR)
            
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    #instantiate
    game = Game()
    game.run()
    
    
