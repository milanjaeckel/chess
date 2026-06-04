import pygame



class ChessPiece(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__() 
        
        self.image = pygame.image.load(image_path).convert_alpha()
        
        # 3. Get the bounding box (Rect) of the image
        self.rect = self.image.get_rect()
        
        # 4. Set the initial position of the Rect
        self.rect.topleft = (x, y)