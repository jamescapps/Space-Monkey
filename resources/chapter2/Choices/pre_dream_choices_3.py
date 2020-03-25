import pygame
from resuable_functions import update_and_flip, dialogue, good_luck
from chapter2 import dream


def hybernation_explanation():
    # Commander
    update_and_flip()
    dialogue(' Your body will be in suspension.       ', 490, 150, 15)
    dialogue(' However, your mind will be active.     ', 490, 200, 15)
    dialogue(' Essentially you will be having a       ', 490, 250, 15)
    dialogue(' 750 year long dream...                 ', 490, 300, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) Will I perceive time?                    ', 243, 600, 15)
        dialogue(' (2) Are there any long-term effects?         ', 243, 625, 15)
        dialogue(' (3) Well let\'s get to it!                   ', 243, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) Will I perceive time?                    ', 243, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Are there any long-term effects?         ', 243, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Well let\'s get to it!                   ', 243, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    good_luck()
                    # Run function to enter dream
                    # Need a better transition into dream...
                    dream.dream()


def get_personal():
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) Are you afraid to die?   ', 243, 600, 15)
        dialogue(' (2) Will you miss me?        ', 243, 625, 15)
        dialogue(' (3) Nothing.. I am ready...  ', 243, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) Are you afraid to die?   ', 243, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Will you miss me?        ', 243, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Nothing.. I am ready...  ', 243, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    good_luck()
                    # Run function to enter dream
                    # Need a better transition into dream...
                    dream.dream()


def pleasure():
    while True:
        # Monkey
        update_and_flip()
        dialogue(' Sir, it has been an absolute pleasure   ', 243, 600, 15)
        dialogue(' to serve under you. I wish you all      ', 243, 625, 15)
        dialogue(' the best.                               ', 243, 650, 15)

        # Maybe add something meaningful from the Commander.
        pygame.time.delay(3000)
        good_luck()
        # Run function to enter dream
        # Need a better transition into dream...
        dream.dream()


def miss_you():
    while True:
        # Monkey
        update_and_flip()
        dialogue(' Sir...                                  ', 243, 600, 15)
        dialogue(' I am... going to ...                    ', 243, 625, 15)
        dialogue(' miss you..                              ', 243, 650, 15)

        while True:
            # Commander
            update_and_flip()
            dialogue(' I appreciate that Space Monkey.         ', 490, 150, 15)
            dialogue(' The feeling is mutual.                  ', 490, 200, 15)
            dialogue(' Now get out there and complete your     ', 490, 250, 15)
            dialogue(' mission!                                ', 490, 300, 15)

            pygame.time.delay(3000)
            # Run function to enter dream
            # Need a better transition into dream...
            dream.dream()
