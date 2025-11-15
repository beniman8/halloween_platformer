from settings import *
from support import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self,pos,surf, groups):
        super().__init__(groups)
        self.image = surf 
        self.rect = self.image.get_frect(topleft=pos)
        
class AnimatedSprite(Sprite):
    def __init__(self,frames, pos, groups):
        self.frames,self.frame_index,self.animation_speed = frames,0,10
        super().__init__(pos,self.frames[self.frame_index] , groups)
        
    def animate(self,dt):
        self.frame_index += self.animation_speed *dt 
        self.image = self.frames[int(self.frame_index) % len(self.frames)]
        
class Player(AnimatedSprite):
    
    def __init__(self,pos,groups,collision_sprites,frames):

        super().__init__(frames, pos, groups)
        
        self.direction = pygame.Vector2()
        self.flip = False
        self.speed = 200
        
        
        
        
    def input(self):
        
        #mechanics 
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
        self.direction = self.direction.normalize() if self.direction else self
        
        
        
    def move(self,dt):
        
        self.rect.x += self.direction.x * self.speed *dt 
        
        
    #TODO This is where you need to start tomorrow
    def animate(self,dt):
        if self.direction.x:
            self.state = 'walk'
            self.frame_index +=self.animation_speed *dt 
            self.flip = self.direction.x < 0
        else:
            self.frame_index = 0 
            
        self.image = self.frames[int(self.frame_index) % len(self.frames)]
        self.image = pygame.transform.flip(self.image,self.flip,False)
    
    
    def update(self,dt):
        self.input()
        self.move(dt)
        self.animate(dt)
        
        