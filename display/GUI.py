import pygame
import random
import sprites

pygame.init()

def GUI(hands, nplayers = 1):

    SCREEN_WIDTH = 1300
    SCREEN_HEIGHT = 800

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        
        for i in range(len(hands[0])):
            card = sprites.Cards(hands[0][i])
            card.set_color((0, 0, 0))

            font = pygame.font.SysFont(None, 175)
            letter = font.render(hands[0][i], True, (255, 255, 255))
            card.image.blit(letter, (card.image.get_width() / 2 - letter.get_width() / 2, card.image.get_height() / 2 - letter.get_height() / 2))

            # card.image=pygame.transform.rotate(card.image, (-len(hands[0])+1)*2.5+i*5)

            card_center = (
                (SCREEN_WIDTH - card.image.get_width()) / 2 + (len(hands[0]) - 1 - 2 * i) * 62.5,
                ((SCREEN_HEIGHT - card.image.get_height()))
                # (SCREEN_HEIGHT - card.image.get_height() + 10 * abs(-i + (len(hands[0])-1)/2) ** 1.7)
            )

            screen.blit(card.image, card_center)

        # if nplayers > 1:
        #     for i in range(hands[1]):
        #         card = sprites.Cards
        #         pygame.sprite.Group.add(card)

        #         innersurf = pygame.Surface((115, 165), flags = pygame.SRCALPHA)
        #         innersurf.fill((255, 255, 255))
        #         surf.blit(innersurf, (surf.get_width() / 2 - innersurf.get_width() / 2, surf.get_height() / 2 - innersurf.get_height() / 2))

        #         surf=pygame.transform.rotate(surf, -((-hands[1]+1)*2.5+i*5))

        #         surf_center = (
        #             (SCREEN_WIDTH - surf.get_width()) / 2 + (hands[1] - 1 - 2 * i) * 62.5,
        #             (-50- 10 * abs(-i + (hands[1]-1)/2) ** 1.7)
        #         )

        #         screen.blit(surf, surf_center)
        
        # if nplayers > 2:
        #     for i in range(hands[2]):
        #         card = sprites.Cards
        #         pygame.sprite.Group.add(card)

        #         innersurf = pygame.Surface((165, 115), flags = pygame.SRCALPHA)
        #         innersurf.fill((255, 255, 255))
        #         surf.blit(innersurf, (surf.get_width() / 2 - innersurf.get_width() / 2, surf.get_height() / 2 - innersurf.get_height() / 2))

        #         surf = pygame.transform.rotate(surf, (-hands[2]+1)*2.5+i*5)
                
        #         surf_center = (
        #             (-40 - 10 * abs(-i + (hands[2] - 1) / 2) ** 1.7),
        #             ((SCREEN_HEIGHT / 2 - surf.get_height()) / 2 + (hands[2] - 1 - i) * 87.5)
        #         )

        #         screen.blit(surf, surf_center)

        # if nplayers > 3:
        #     for i in range(hands[3]):
        #         card = sprites.Cards
        #         pygame.sprite.Group.add(card)

        #         innersurf = pygame.Surface((165, 115), flags = pygame.SRCALPHA)
        #         innersurf.fill((255, 255, 255))
        #         surf.blit(innersurf, (surf.get_width() / 2 - innersurf.get_width() / 2, surf.get_height() / 2 - innersurf.get_height() / 2))

        #         surf = pygame.transform.rotate(surf, -((-hands[3]+1)*2.5+i*5))
                
        #         surf_center = (
        #             (SCREEN_WIDTH + 40 -surf.get_width() + 10 * abs(-i + (hands[3] - 1) / 2) ** 1.7),
        #             ((SCREEN_HEIGHT / 2 - surf.get_height()) / 2 + (hands[3] - 1 - i) * 87.5)
        #         )

        #         screen.blit(surf, surf_center)

        clicker = sprites.Clicker()
        clicker.update()
        screen.blit(clicker.image, clicker.position)

        pygame.display.flip()

GUI([['A', 'B', 'C', 'D', 'E', 'F', 'G'], 7, 6, 5], 4)