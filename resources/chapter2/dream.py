import pygame
from resources.resuable_functions import update_and_flip, dialogue
from resources.chapter2.levels import level_one

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
dream1_background = pygame.image.load('img/dream/img1_background_animate.jpeg')
dream2_background = pygame.image.load('img/dream/dream8.jpg')
animation_object = pygame.transform.rotate(pygame.image.load('img/working_star.png').convert(), 20)


def dream():
    def dream_intro():
        while True:
            screen.fill(black)
            update_and_flip()
            dialogue('      T h e  D r e a m               ', 440, 100, 20)
            dialogue(' Sometimes there will be two windows.', 440, 200, 15)
            dialogue(' Make sure they are side by side.    ', 440, 250, 15)
            dialogue(' Use left and right to move.         ', 440, 300, 15)
            dialogue(' Answer the questions.               ', 440, 350, 15)
            dialogue('     (enter)                         ', 440, 500, 15)
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    flashing_monkey_moon()

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

        dream_one()

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

        x = 0
        y = 500
        while x < 700 and y < 700:
            update_and_flip()
            screen.blit(dream1_background, [0, 0])
            x += .75
            y -= .75
            screen.blit(animation_object, (x, y))
            pygame.display.flip()
            update_and_flip()

        screen.fill(black)
        update_and_flip()
        dialogue(' W h o  a r e  y o u ?              ', 500, 200, 20)
        pygame.time.delay(3500)

        screen.fill(black)
        update_and_flip()
        dialogue(' W h o  i s  a n y o n e ?              ', 500, 200, 20)
        pygame.time.delay(3500)

        x = 0
        y = 500
        while x < 700 and y < 700:
            update_and_flip()
            screen.blit(dream2_background, [0, 0])
            x += .75
            y -= .75
            screen.blit(animation_object, (x, y))
            pygame.display.flip()
            update_and_flip()

        level_one.game()

    dream_intro()

