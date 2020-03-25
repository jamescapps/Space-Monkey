import pygame
from resuable_functions import update_and_flip

pygame.init()

size = (800, 800)
white = (255, 255, 255)
blue = (0, 6, 40)
black = (0, 0, 0)

# Screen set up
screen = pygame.display.set_mode(size)

# Register images
brown_monkey = pygame.image.load('img/dream/brown_monkey.jpeg')
moon = pygame.image.load('img/dream/moon.jpeg')
dream1 = pygame.image.load('img/dream/dream1.jpeg')
dream2 = pygame.image.load('img/dream/dream2.jpeg')
dream3 = pygame.image.load('img/dream/dream3.jpeg')
dream4 = pygame.image.load('img/dream/dream4.jpeg')
dream5 = pygame.image.load('img/dream/dream5.jpeg')
dream6 = pygame.image.load('img/dream/dream6.jpeg')
dream7 = pygame.image.load('img/dream/dream7.jpeg')
dream8 = pygame.image.load('img/dream/dream8.jpeg')
dream9 = pygame.image.load('img/dream/dream9.jpeg')
dream11 = pygame.image.load('img/dream/dream11.jpeg')
dream1_background = pygame.image.load('img/dream/img1_background_animate.jpeg')
animation_object = pygame.image.load('img/dream/animation_one.jpg')


def dream():
    def flashing_monkey_moon():
        x = -200
        y = 0
        while x > -400:
            update_and_flip()
            screen.fill(black)
            screen.blit(brown_monkey, (-300, 0))
            pygame.time.delay(1500)
            update_and_flip()
            screen.fill(black)
            screen.blit(moon, (x, y))
            x -= 25
            y -= 25

    def dream_one():
        update_and_flip()
        screen.fill(black)
        screen.blit(dream1, (0, 0))
        pygame.time.delay(3000)
        update_and_flip()
        screen.fill(black)
        screen.blit(dream2, (0, 0))
        pygame.time.delay(3000)
        update_and_flip()
        screen.fill(black)
        screen.blit(dream3, (0, 0))
        pygame.time.delay(3000)
        update_and_flip()
        screen.fill(black)
        screen.blit(dream4, (0, 0))
        pygame.time.delay(3000)
        update_and_flip()
        screen.fill(black)
        screen.blit(dream5, (0, 0))
        pygame.time.delay(3000)
        update_and_flip()
        screen.fill(black)
        screen.blit(dream6, (0, 0))
        pygame.time.delay(3000)
        update_and_flip()
        screen.fill(black)
        screen.blit(dream7, (0, 0))
        pygame.time.delay(3000)
        update_and_flip()
        screen.fill(black)
        screen.blit(dream7, (0, 0))
        pygame.time.delay(1500)
        update_and_flip()
        screen.fill(black)
        screen.blit(dream8, (0, 0))
        pygame.time.delay(1500)
        update_and_flip()
        screen.fill(black)
        screen.blit(dream9, (0, 0))
        pygame.time.delay(750)
        # What is happening here? Delay is longer and sometimes last image doesn't show.
        update_and_flip()
        screen.fill(black)
        screen.blit(dream11, (0, 0))
        pygame.time.delay(10000)

        x = 300
        y = 500
        while y > 0:
            update_and_flip()
            screen.blit(dream1_background, [0, 0])
            x += 0
            y -= .5
            screen.blit(animation_object, (x, y))
            pygame.display.flip()
            update_and_flip()

    flashing_monkey_moon()
    dream_one()
