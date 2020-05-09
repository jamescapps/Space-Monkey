import pygame
from resources.resuable_functions import update_and_flip, dialogue, good_luck
from resources.chapter2 import dream
from resources.chapter2.Choices import pre_dream_choices_5


def perceive_time():
    # Commander
    update_and_flip()
    dialogue(' Only in the same way that you may perceive        ', 520, 100, 15)
    dialogue(' time in a dream. And what really is existence?    ', 520, 150, 15)
    dialogue(' Other than time in a dream.                       ', 520, 200, 15)
    dialogue('                                                   ', 520, 250, 15)

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
                    dialogue(' (1) Are you saying there is no meaning?      ', 248, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_5.no_meaning()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Then what is death?                      ', 248, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_5.what_is_death()

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Well let\'s get to it!                   ', 248, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    good_luck()
                    # Run function to enter dream
                    # Need a better transition into dream...
                    dream.dream()


def long_term_effects():
    # Commander
    update_and_flip()
    dialogue(' (1) Lie                                           ', 520, 100, 15)
    dialogue(' (2) Tell the truth                                ', 520, 150, 15)
    dialogue('                                                   ', 520, 200, 15)
    dialogue('                                                   ', 520, 250, 15)

    # Underline selection before running next function.
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            while True:
                update_and_flip()
                dialogue(' (1) Lie                                           ', 525, 100, 15, underline=True)
                pygame.display.flip()
                pygame.time.delay(1500)
                pre_dream_choices_5.lie()

        if event.key == pygame.K_2:
            while True:
                update_and_flip()
                dialogue(' (2) Tell the truth                                ', 525, 150, 15, underline=True)
                pygame.display.flip()
                pygame.time.delay(1500)
                pre_dream_choices_5.truth()


def afraid_to_die():
    # Commander
    update_and_flip()
    dialogue(' Why would I be afraid of the most natural thing   ', 520, 100, 15)
    dialogue(' this world has to offer?                          ', 520, 150, 15)
    dialogue('                                                   ', 520, 200, 15)
    dialogue('                                                   ', 520, 250, 15)

    pygame.time.delay(5000)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' I am ready.                                  ', 243, 600, 15)
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
    dialogue(' (1) In a professional manner.                     ', 520, 100, 15)
    dialogue(' (2) In a personal manner.                         ', 520, 150, 15)
    dialogue('                                                   ', 520, 200, 15)
    dialogue('                                                   ', 520, 250, 15)

    # Underline selection before running next function.
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            while True:
                update_and_flip()
                dialogue(' (1) In a professional manner.                     ', 525, 100, 15, underline=True)
                pygame.display.flip()
                pygame.time.delay(1500)
                pre_dream_choices_5.professional()

        if event.key == pygame.K_2:
            while True:
                update_and_flip()
                dialogue(' (2) In a personal manner.                         ', 525, 150, 15, underline=True)
                pygame.display.flip()
                pygame.time.delay(1500)
                # Run next function
                # personal()
