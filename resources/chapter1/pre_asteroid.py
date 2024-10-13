import pygame
from resources.resuable_functions import dialogue, update_and_flip
from resources.intro import stars
from resources.chapter1.Choices import asteroid_choices

size = (800, 800)
screen = pygame.display.set_mode(size)
black = (0, 0, 0)
white = (255, 255, 255)

# Register images
images = {
    'commander': pygame.image.load('img/commander.png').convert(),
    'comms_photo': pygame.image.load('img/comms_photo.png').convert(),
    'stars': pygame.image.load('img/stars.png').convert()
}

def handle_keypress(key, choices):
    """Handles the selection of dialogue choices."""
    if key == pygame.K_1:
        highlight_choice('(1) No', 248, 600)
        asteroid_choices.say_no_1()
    elif key == pygame.K_2:
        highlight_choice('(2) Yes', 242, 625)
        asteroid_choices.say_yes_1()
    elif key == pygame.K_3:
        highlight_choice('(3) More Choices', 286, 650)
        asteroid_choices.say_more_choices_1()


def highlight_choice(text, x, y):
    """Helper function to highlight a selected choice."""
    while True:
        update_and_flip()
        dialogue(text, x, y, 15, underline=True)
        pygame.display.flip()
        pygame.time.delay(1500)


def commander_convo():
    """Handles the conversation with the commander."""
    run_conversation(images['commander'], ' Space Monkey! Are you there?  Do you read me?... ',
                     '                    (Enter)                       ', [290, 200])


def monkey_convo():
    """Handles the monkey’s conversation."""
    run_conversation(images['comms_photo'], ' Loud and clear Commander! ', '          (Enter)          ', [300, 200])


def run_conversation(image, text1, text2, position):
    """Helper function to run a single conversation."""
    while True:
        update_and_flip()
        screen.blit(image, position)
        dialogue(text1, 420, 500, 20)
        dialogue(text2, 420, 525, 12)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            screen.fill(black)
            break


def monkey_and_commander_convo():
    """Handles the conversation between the monkey and the commander."""
    while True:
        update_and_flip()
        screen.blit(images['comms_photo'], [500, 500])
        screen.blit(images['commander'], [50, 40])
        screen.blit(stars, [60, 350])
        screen.blit(stars, [360, 350])
        screen.blit(stars, [660, 350])

        # Dialogue Options
        display_dialogue_options()

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            handle_keypress(event.key, asteroid_choices)


def display_dialogue_options():
    """Displays the dialogue options on screen."""
    # Commander Dialogue
    dialogue(' You are approaching the asteroid belt?', 500, 150, 15)
    dialogue(' Do you remember the Prime Directive?', 490, 200, 15)

    # Monkey's Choices
    dialogue(' (1) No ', 243, 600, 15)
    dialogue(' (2) Yes ', 246, 625, 15)
    dialogue(' (3) More Choices ', 286, 650, 15)
