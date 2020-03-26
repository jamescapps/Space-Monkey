import pygame
from resuable_functions import update_and_flip, dialogue, good_luck
from chapter2 import dream
from chapter2.Choices import pre_dream_choices_5


def perceive_time():
    # Commander
    update_and_flip()
    dialogue(' Only in the same way that you may perceive        ', 490, 150, 15)
    dialogue(' time in a dream. And what really is existence?    ', 490, 200, 15)
    dialogue(' Other than time in a dream.                       ', 490, 250, 15)
    dialogue('                                                   ', 490, 300, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) Are you saying there is no meaning?      ', 243, 600, 15)
        dialogue(' (2) Then what is death?                      ', 243, 625, 15)
        dialogue('(3) Well let\'s get to it!                   ', 243, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) Are you saying there is no meaning?      ', 243, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_5.no_meaning()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Then what is death?                      ', 243, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function
                    # what_is_death()

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


def long_term_effects():
    # Commander
    update_and_flip()
    dialogue(' (1) Lie                                           ', 490, 150, 15)
    dialogue(' (2) Tell the truth                                ', 490, 200, 15)
    dialogue('                                                   ', 490, 250, 15)
    dialogue('                                                   ', 490, 300, 15)

    # Underline selection before running next function.
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            while True:
                update_and_flip()
                dialogue(' (1) Lie                                           ', 243, 600, 15, underline=True)
                pygame.display.flip()
                pygame.time.delay(1500)
                # Run next function
                # lie()

        if event.key == pygame.K_2:
            while True:
                update_and_flip()
                dialogue(' (2) Tell the truth                                ', 243, 625, 15, underline=True)
                pygame.display.flip()
                pygame.time.delay(1500)
                # Run next function
                # truth


def afraid_to_die():
    # Commander
    update_and_flip()
    dialogue(' Why would I be afraid of the most natural thing   ', 490, 150, 15)
    dialogue(' this world has to offer?                          ', 490, 200, 15)
    dialogue('                                                   ', 490, 250, 15)
    dialogue('                                                   ', 490, 300, 15)

    pygame.time.delay(5000)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' That\'s beautiful commander.                 ', 243, 600, 15)
        dialogue(' Let\'s get to it!                            ', 243, 625, 15)
        dialogue('                                              ', 243, 650, 15)

        pygame.time.delay(1500)
        good_luck()
        # Run function to enter dream
        # Need a better transition into dream...
        dream.dream()


def miss_me():
    # Commander
    update_and_flip()
    dialogue(' (1) In a professional manner.                     ', 490, 150, 15)
    dialogue(' (2) In a personal manner.                         ', 490, 200, 15)
    dialogue('                                                   ', 490, 250, 15)
    dialogue('                                                   ', 490, 300, 15)

    # Underline selection before running next function.
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            while True:
                update_and_flip()
                dialogue(' (1) In a professional manner.                     ', 243, 600, 15, underline=True)
                pygame.display.flip()
                pygame.time.delay(1500)
                # Run next function
                # professional()

        if event.key == pygame.K_2:
            while True:
                update_and_flip()
                dialogue(' (2) In a personal manner.                         ', 243, 625, 15, underline=True)
                pygame.display.flip()
                pygame.time.delay(1500)
                # Run next function
                # personal()