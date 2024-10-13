import pygame
from resources.resuable_functions import dialogue, update_and_flip
from resources.chapter1.asteroid_field import instructions

# Constants for dialogue positioning
DIALOGUE_X = 250
COMMANDER_X = 520
DIALOGUE_Y_START = 600
DIALOGUE_LINE_SPACING = 25
DELAY_TIME = 3000

def display_dialogue(lines, x=DIALOGUE_X, start_y=DIALOGUE_Y_START):
    """Display multiple lines of dialogue."""
    for i, line in enumerate(lines):
        dialogue(line, x, start_y + (i * DIALOGUE_LINE_SPACING), 15)
    pygame.time.delay(DELAY_TIME)

def i_understand():
    lines = [
        '  Great Commander!  I am glad we are on the same       ',
        '  page.  Now let\'s proceed with the mission!          ',
        '                                                       ',
        '                                                       ',
        '                                                       ',
        '                                                       '
    ]
    display_dialogue(lines)
    # Run function to enter asteroid field without weapons
    instructions(False)

def strong_feelings():
    lines = [
        '   Commander I told you from the beginning.....         ',
        '  I am a Space Monkey.  I\'ve got no time for          ',
        '  relationships.  You\'re gonna have to make sure      ',
        '  those feelings don\'t get in the way of the mission. ',
        '                                                       ',
        '                                                       '
    ]
    display_dialogue(lines)

    while True:
        # Commander dialogue
        update_and_flip()
        commander_lines = [
            '   Space Monkey...                                      ',
            '   Your confidence and aloofness only                  ',
            '  make me want you all the more....                    ',
            '  Why don\'t you go ahead and use your weapons....      ',
            '  And don\'t worry about me.  The mission is more       ',
            '  important than my heart.   (enter)                    '
        ]
        for i, line in enumerate(commander_lines):
            dialogue(line, COMMANDER_X, 100 + (i * DIALOGUE_LINE_SPACING), 15)
        pygame.display.flip()
        pygame.time.delay(1500)

        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            pygame.time.delay(DELAY_TIME)
            # Run function to enter asteroid field with weapons
            instructions(True)
