import pygame
import consts

class Character():
    
    def __init__(self, x, y,animation_sprites):
        self.flip = False
        self.animaton_srpites = animation_sprites
        self.frame_index = 0
        self.image = animation_sprites[self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.shape = pygame.Rect(0, 0 , consts.CHARACTER_WIDTH, consts.CHARACTER_HEIGHT)
        self.shape.center = (x, y)
        self.velocity = consts.CHARACTER_VELOCITY
 

        
    def update_animation(self):
        cooldown_animation = 150
        self.image = self.animaton_srpites[self.frame_index]
        
        if (pygame.time.get_ticks() - self.update_time) >= cooldown_animation:
            if self.frame_index == len(self.animaton_srpites) - 1:
                self.frame_index = 0
            else:    
                self.frame_index += 1 
            self.update_time = pygame.time.get_ticks()
        
    def draw(self, window,color):
        self.image_flip = pygame.transform.flip(self.image, flip_x=self.flip, flip_y=False)
        window.blit(self.image_flip, self.shape)
        pygame.draw.rect(window, color, self.shape,width=1)
        
    
        