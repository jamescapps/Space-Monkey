import pygame
from resources.resuable_functions import dialogue, update_and_flip
from resources.chapter1.asteroid_field import instructions


def i_understand():
    # Monkey
    dialogue('  Great Commander!  I am glad we are on the same       '
             , 250, 600, 15)
    dialogue('  page.  Now let\'s proceed with the mission!          '
             , 250, 625, 15)
    dialogue('                                                       '
             , 250, 650, 15)
    dialogue('                                                       '
             , 250, 675, 15)
    dialogue('                                                       '
             , 250, 700, 15)
    dialogue('                                                       '
             , 250, 725, 15)
    pygame.time.delay(3000)
    # Run function to enter asteroid field without weapons
    instructions(False)


def strong_feelings():
    # Monkey
    dialogue('   Commander I told you from the beginning.....         '
             , 250, 600, 15)
    dialogue('  I am a Space Monkey.  I\'ve got no time for          '
             , 250, 625, 15)
    dialogue('  relationships.  You\'re gonna have to make sure      '
             , 250, 650, 15)
    dialogue('  those feelings don\'t get in the way of the mission. '
             , 250, 675, 15)
    dialogue('                                                       '
             , 250, 700, 15)
    dialogue('                                                       '
             , 250, 725, 15)
    pygame.time.delay(3000)

    while True:
        # Commander
        update_and_flip()
        dialogue('     Space Monkey...                                    '
                 , 520, 100, 15)
        dialogue('       You\'re confidence and aloofness only make me want    '
                 , 510, 125, 15)
        dialogue('   you all the more....                                '
                 , 530, 150, 15)
        dialogue('  Why don\'t you go ahead and use your weapons....    '
                 , 530, 175, 15)
        dialogue('  And don\'t worry about me.  The mission is more     '
                 , 530, 200, 15)
        dialogue('   important than my heart.   (enter)                   '
                 , 530, 225, 15)
        pygame.time.delay(1500)

        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.time.delay(3000)
                # Run function to enter asteroid field with weapons
                instructions(True)
