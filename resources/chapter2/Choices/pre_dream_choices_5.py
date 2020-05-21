import pygame
from resources.resuable_functions import update_and_flip, dialogue, good_luck
from resources.chapter2 import dream


def no_meaning():
    # Commander
    update_and_flip()
    dialogue(' The question of meaning is separate from the         ', 520, 100, 15)
    dialogue(' question of what existence is. So no that is         ', 520, 150, 15)
    dialogue(' not what I am saying. I can comment on existence     ', 520, 200, 15)
    dialogue(' because we share it. Meaning is yours alone. (enter) ', 520, 250, 15)

    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            while True:
                # Monkey
                update_and_flip()
                dialogue(' I am ready commander.                        ', 243, 600, 15)
                dialogue(' Let\'s get this show on the road!             ', 243, 625, 15)
                dialogue('                                              ', 243, 650, 15)

                pygame.time.delay(1500)
                good_luck()
                pygame.time.delay(1500)
                dream.dream()


def what_is_death():
    # Commander
    update_and_flip()
    dialogue(' The greatest mystery that no one knows the answer        ', 520, 100, 15)
    dialogue(' to, but everyone will have revealed.  (enter)            ', 520, 150, 15)
    dialogue('                                                          ', 520, 200, 15)
    dialogue('                                                          ', 520, 250, 15)

    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            while True:
                # Monkey
                update_and_flip()
                dialogue(' I am ready commander.                        ', 243, 600, 15)
                dialogue(' Let\'s get to it!                             ', 243, 625, 15)
                dialogue('                                              ', 243, 650, 15)

                pygame.time.delay(1500)
                good_luck()
                dream.dream()


def lie():
    # Commander
    update_and_flip()
    dialogue(' Eh... None at all...                              ', 520, 100, 15)
    dialogue(' It is basically a cold.                           ', 520, 150, 15)
    dialogue(' Now get to it!                                    ', 520, 200, 15)
    dialogue('                                                   ', 520, 250, 15)

    pygame.time.delay(6000)
    dream.dream()


def truth():
    # Commander
    update_and_flip()
    dialogue(' There is a chance you could experience an         ', 520, 100, 15)
    dialogue(' illness when you wake up. But it is not probable  ', 520, 150, 15)
    dialogue(' and you are healthy so you should be fine.        ', 520, 200, 15)
    dialogue(' Now get to it!                                    ', 520, 250, 15)

    pygame.time.delay(6000)
    dream.dream()


def professional():
    # Commander
    update_and_flip()
    dialogue(' Space monkey you are an admirable soldier.        ', 520, 100, 15)
    dialogue(' I respect you in a professional way.              ', 520, 150, 15)
    dialogue(' Now get to it!                                    ', 520, 200, 15)
    dialogue('                                                   ', 520, 250, 15)

    pygame.time.delay(6000)
    dream.dream()


def personal():
    # Commander
    update_and_flip()
    dialogue(' Space monkey I will miss you dearly.              ', 520, 100, 15)
    dialogue(' I... eh.. err.                                    ', 520, 150, 15)
    dialogue(' Now get to it!                                    ', 520, 200, 15)
    dialogue('                                                   ', 520, 250, 15)

    pygame.time.delay(6000)
    dream.dream()
