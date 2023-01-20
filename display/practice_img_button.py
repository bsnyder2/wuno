

# Import and initialize the pygame library
import pygame, sys
pygame.init()
clock = pygame.time.Clock()

#Challenge Button class

class Button(pygame.sprite.Sprite):
    def __init__(self,width, height, pos_x,pos_y):
        super().__init__()
        self.color= (255,255,255)
        self.image = pygame.image.load(sys.path[0] + "/flame pngs/A.png")
        #self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
    def update(self):
        if self.color == (255,255,255):
            self.color = (255,0,0)
        else:
            self.color = (255,255,255)
        self.image.fill(self.color)
        #replace/add on specific response depending on what you want your button to do

class Susanne_Button(Button):
    def __init__(self,width, height, pos_x,pos_y):
        super().__init__(width, height, pos_x, pos_y)
    def update(self):
        if self.color == (255,255,255):
            self.color = (0,255,0)
        else:
            self.color = (255,255,255)
        self.image.fill(self.color)

class Leah_Button(Button):
    def __init__(self,width, height, pos_x,pos_y):
        super().__init__(width, height, pos_x, pos_y)
    def update(self):
        if self.color == (255,255,255):
            self.color = (0,0,255)
        else:
            self.color = (255,255,255)
        self.image.fill(self.color)


#invisible mouse sprite class

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
        if pygame.sprite.spritecollide(follower, button_group, dokill=False):
            #actions that happen when SPECIFIC button is pressed
            for button in button_group:
                if pygame.sprite.collide_rect(follower, button):
                    button.update()



# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
#pygame.mouse.set_visible(False)







#button group
challenge_button = Button(50, 50, 100, 100)
susanne_button = Susanne_Button(60,30,200,200)
leah_button = Leah_Button(100,50,200,300)
button_group = pygame.sprite.Group()
button_group.add(challenge_button, susanne_button, leah_button)


#invisible mouse sprite group
follower = Invisible_Follower()
follower_group = pygame.sprite.Group()
follower_group.add(follower)

# Run until the user asks to quit

while True:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            follower.shoot()

    # Fill the background with white
    #screen.fill((0,0,0))

    # Flip the display
    pygame.display.flip()
    
    button_group.draw(screen)
    follower_group.draw(screen)
    follower_group.update()
    clock.tick(60)


#TODO
#make a card subclass of button
    # def show_card(self):
    #     pass
    #     #gets called when you press a card in your hand
    #     #move card up and magnify it
#make challenge button

    
        