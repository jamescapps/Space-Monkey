import pygame
from resuable_functions import update_and_flip, dialogue, good_luck
from chapter2 import dream


def no_meaning():
    # Commander
    update_and_flip()
    dialogue(' The question of meaning is separate from the         ', 490, 150, 15)
    dialogue(' question of what existence is. So no that is         ', 490, 200, 15)
    dialogue(' not what I am saying. I can comment on existence     ', 490, 250, 15)
    dialogue(' because we share it. Meaning is yours alone.         ', 490, 300, 15)

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