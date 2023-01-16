
import pygame, sys
pygame.init()
clock = pygame.time.Clock()

#Button Superclass: this is what specific buttons should inherit from
class Button(pygame.sprite.Sprite):
    button_group = pygame.sprite.Group()
    def __init__(self,width, height, pos_x,pos_y):
        super().__init__()
        self.name = str(self)
        self.color= (255,255,255)
        self.image = pygame.Surface([width,height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        Button.button_group.add(self)
    def update(self):
        if self.color == (255,255,255):
            self.color = (255,0,0)
        else:
            self.color = (255,255,255)
        self.image.fill(self.color)
        #replace/add on specific response depending on what you want your button to do

#invisible mouse sprite class: there is only one of these objects for the whole game --> functions as our "clicker"
class Invisible_Follower(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color= (255,255,255)
        self.image = pygame.Surface([1,1])
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    def shoot(self):
        #action that happens when ANY button is pressed
        if pygame.sprite.spritecollide(follower, Button.button_group, dokill=False):
            #actions that happen when SPECIFIC button is pressed
            for button in Button.button_group:
                if pygame.sprite.collide_rect(follower, button):
                    button.update()
        
#Example Button Subclass
class Susanne_Button(Button):
    def __init__(self,width, height, pos_x,pos_y):
        super().__init__(width, height, pos_x, pos_y)
    def update(self):
        if self.color == (255,255,255):
            self.color = (0,255,0)
        else:
            self.color = (255,255,255)
        self.image.fill(self.color)


# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

#button group
challenge_button = Button(50, 50, 100, 100)
#susanne_button = Susanne_Button(60,30,200,200)

#invisible mouse sprite group
follower = Invisible_Follower()
follower_group = pygame.sprite.Group()
follower_group.add(follower)

# True loop not necessary for final module, should be combined w GUI loop later on

while True:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #triggers button response
        if event.type == pygame.MOUSEBUTTONDOWN:
            follower.shoot()

    # Flip the display
    pygame.display.flip()

    #button display
    Button.button_group.draw(screen)
    follower_group.draw(screen)
    follower_group.update()
    clock.tick(60)


#TODO
#make a card subclass of button
    # def show_card(self):
    #     pass
    #     #gets called when you press a card in your hand
    #     #move card up and magnify it
#make challenge button --> maybe 2? one for complete, one for continuable?

    