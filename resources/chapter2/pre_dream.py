import pygame
from resources.intro import flying_through_space_1, stars
from resources.resuable_functions import dialogue, update_and_flip
from resources.chapter2.Choices import pre_dream_choices


# Setup
size = (800, 800)
screen = pygame.display.set_mode(size)
black = (0, 0, 0)
white = (255, 255, 255)

# Register images
commander = pygame.image.load('img/commander.png').convert()
comms_photo = pygame.image.load('img/comms_photo.png').convert()


def nice_work():
    while True:
        screen.fill(black)
        screen.blit(comms_photo, [500, 500])
        update_and_flip()
        screen.blit(commander, [50, 40])
        update_and_flip()
        screen.blit(stars, [60, 350])
        screen.blit(stars, [360, 350])
        screen.blit(stars, [660, 350])

        # Commander
        dialogue(' Nice work in the asteroid field!       ', 490, 100, 15)
        dialogue(' Are you ready to enter hybernation?    ', 490, 150, 15)
        dialogue(' Much time and distance will pass before', 490, 200, 15)
        dialogue(' the next phase of your mission.        ', 490, 250, 15)

        # Monkey
        dialogue(' (1) No ', 243, 600, 15)
        dialogue(' (2) Yes ', 246, 625, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) No ', 248, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices.say_no()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Yes ', 251, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices.say_yes()


def main():
    while True:
        screen.fill(black)
        screen.blit(commander, [290, 200])
        update_and_flip()

        dialogue(' Space Monkey! Are you there?  Do you read me?... ', 420, 500, 20)
        dialogue('                    (Enter)                       ', 420, 525, 12)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(black)
                break
    while True:
        update_and_flip()
        screen.blit(comms_photo, [300, 200])
        update_and_flip()

        dialogue(' Loud and clear Commander! ', 420, 500, 20)
        dialogue('          (enter)          ', 420, 525, 12)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(black)
                break

    nice_work()
    # Next group is from within nice_work().
