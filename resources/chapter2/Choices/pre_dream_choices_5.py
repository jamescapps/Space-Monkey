import pygame
from resuable_functions import update_and_flip, dialogue, good_luck
from chapter2 import dream


def no_meaning():
    # Commander
    update_and_flip()
    dialogue(' The question of meaning is separate from the         ', 520, 100, 15)
    dialogue(' question of what existence is. So no that is         ', 520, 150, 15)
    dialogue(' not what I am saying. I can comment on existence     ', 520, 200, 15)
    dialogue(' because we share it. Meaning is yours alone.         ', 520, 250, 15)

    pygame.time.delay(10000)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' I am ready commander.                        ', 243, 600, 15)
        dialogue('Let\'s get this show on the road!             ', 243, 625, 15)
        dialogue('                                              ', 243, 650, 15)

        pygame.time.delay(1500)
        good_luck()
        pygame.time.delay(1500)
        dream.dream()


def what_is_death():
    # Commander
    update_and_flip()
    dialogue(' The greatest mystery that no one knows the answer        ', 490, 150, 15)
    dialogue(' to, but everyone will have revealed.                     ', 490, 200, 15)
    dialogue('                                                          ', 490, 250, 15)
    dialogue('                                                          ', 490, 300, 15)

    pygame.time.delay(5000)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' I am ready commander.                        ', 243, 600, 15)
        dialogue(' Let\'s get to it!                            ', 243, 625, 15)
        dialogue('                                              ', 243, 650, 15)

        pygame.time.delay(1500)
        good_luck()
        # Run function to enter dream
        # Need a better transition into dream...
        dream.dream()


def lie():
    # Commander
    update_and_flip()
    dialogue(' Eh... None at all...                              ', 490, 150, 15)
    dialogue(' It is basically a cold.                           ', 490, 200, 15)
    dialogue(' Now get to it!                                    ', 490, 250, 15)
    dialogue('                                                   ', 490, 300, 15)

    pygame.time.delay(3000)
    # Run function to enter dream
    # Need a better transition into dream...
    dream.dream()


def truth():
    # Commander
    update_and_flip()
    dialogue(' There is a chance you could experience an         ', 490, 150, 15)
    dialogue(' illness when you wake up. But it is not probable  ', 490, 200, 15)
    dialogue(' and you are healthy so you should be fine.        ', 490, 250, 15)
    dialogue(' Now get to it!                                    ', 490, 300, 15)

    pygame.time.delay(3000)
    # Run function to enter dream
    # Need a better transition into dream...
    dream.dream()


def professional():
    # Commander
    update_and_flip()
    dialogue(' Space monkey you are an admirable soldier.        ', 490, 150, 15)
    dialogue(' I respect you in a professional way.              ', 490, 200, 15)
    dialogue(' Now get to it!                                    ', 490, 250, 15)
    dialogue('                                                   ', 490, 300, 15)

    pygame.time.delay(3000)
    # Run function to enter dream
    # Need a better transition into dream...
    dream.dream()


def personal():
    # Commander
    update_and_flip()
    dialogue(' Space monkey I will miss you dearly.              ', 490, 150, 15)
    dialogue(' I... eh.. err.                                    ', 490, 200, 15)
    dialogue(' Now get to it!                                    ', 490, 250, 15)
    dialogue('                                                   ', 490, 300, 15)

    pygame.time.delay(3000)
    # Run function to enter dream
    # Need a better transition into dream...
    dream.dream()
