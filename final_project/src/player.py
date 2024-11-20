#Rectangle: w, h, pos 
#surface: contains rect, has image

class Player(pygame.sprite.Sprite): 
    def __init__(self,name):
        super().__init__()
        
        self.name
        self.size = 'small'
        self.image = pygame.image.load(f"/assets/{name}.png") 
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed 
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed

