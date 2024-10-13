import pygame
from resources.resuable_functions import update_and_flip, dialogue
from resources.chapter1.Choices.asteroid_choices_2 import (
    good_luck, whats_the_problem, nonsense, bananas, the_party
)
from resources.chapter1.asteroid_field import instructions

# Constants for dialogue positioning and delays
DIALOGUE_X = 510
DIALOGUE_Y_START = 100
DIALOGUE_LINE_SPACING = 50
DELAY_TIME = 3000

# Used to determine which section to go back to when arriving on the same dialogue from different places.
back_counter = 0

def display_dialogue(lines, x=DIALOGUE_X, start_y=DIALOGUE_Y_START):
    """Display multiple lines of dialogue."""
    for i, line in enumerate(lines):
        dialogue(line, x, start_y + (i * 25), 15)
    pygame.display.flip()

def handle_selection(options):
    """Handle user input for selection options."""
    while True:
        update_and_flip()
        for idx, (text, _) in enumerate(options):
            dialogue(f' ({idx + 1}) {text}', 243, 600 + (25 * idx), 15)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_1, pygame.K_2):
                return event.key - pygame.K_1  # Return the selected index

def say_no_1():
    global back_counter
    back_counter = 1
    # Commander dialogue
    display_dialogue([
        'The Prime Directive states that you are not allowed',
        'to shoot an asteroid. The resulting debris may have',
        'negative consequences for other civilizations.',
        'Are you ready to enter the asteroid field?'
    ], DIALOGUE_X, DIALOGUE_Y_START)

    selection = handle_selection(['No', 'Yes'])
    
    if selection == 0:  # No
        dialogue_selected('No', whats_the_problem)
    elif selection == 1:  # Yes
        good_luck_sequence()

def say_yes_1():
    global back_counter
    back_counter = 2
    # Commander dialogue
    display_dialogue([
        'You are one sharp monkey. That is why we selected',
        'you for this mission. Are you ready to enter the',
        'asteroid field?'
    ], DIALOGUE_X, DIALOGUE_Y_START)

    selection = handle_selection(['No', 'Yes'])

    if selection == 0:  # No
        dialogue_selected('No', whats_the_problem)
    elif selection == 1:  # Yes
        good_luck_sequence()

def dialogue_selected(option_text, function_to_call):
    while True:
        update_and_flip()
        dialogue(f' ({option_text})', 243, 600, 15, underline=True)
        pygame.display.flip()
        pygame.time.delay(1500)
        function_to_call()
        say_more_choices_1()

def good_luck_sequence():
    while True:
        update_and_flip()
        good_luck()
        pygame.time.delay(DELAY_TIME)
        instructions(False)

def say_more_choices_1():
    options = [
        ('The Prime Directive is nonsense.', nonsense),
        ('You lied about there being bananas in the capsule!', bananas),
        ('We should talk about what happened at the party...', the_party),
        ('Back', None)  # Placeholder for back option
    ]
    
    while True:
        update_and_flip()
        display_dialogue([text for text, _ in options], 246, 600)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                index = event.key - pygame.K_1
                dialogue_selected(str(index + 1), options[index][1])
            elif event.key == pygame.K_4:  # Back option
                back_navigation()

def back_navigation():
    while True:
        update_and_flip()
        dialogue('                                                        ', 246, 675, 15, underline=True)
        pygame.display.flip()
        pygame.time.delay(1500)
        # Works but need to adjust text rects in certain areas.
        if back_counter == 0:
            monkey_and_commander_convo()
        elif back_counter == 1:
            say_no_1()
        elif back_counter == 2:
            say_yes_1()
