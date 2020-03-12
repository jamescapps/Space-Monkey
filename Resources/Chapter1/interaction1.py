import pygame
from Choices import asteroid_choices

pygame.init()
size = (800, 800)
white = (255, 255, 255)
screen = pygame.display.set_mode(size)
black = (0, 0, 0)
convo_font = pygame.font.SysFont('monospace', 15)

comms_photo = pygame.image.load('img/comms_photo.png').convert()
commander = pygame.image.load('img/commander.png').convert()


def monkey_and_commander_convo():
    while True:
        screen.blit(comms_photo, [500, 500])
        pygame.display.update()
        pygame.display.flip()
        screen.blit(commander, [50, 40])

        text = convo_font.render(' You are approaching the asteroid belt?', True, white, black)
        text_rect = text.get_rect()
        text_rect.center = (500, 150)
        screen.blit(text, text_rect)
        pygame.display.update()

        text = convo_font.render(' Do you remember the Prime Directive?', True, white, black)
        text_rect = text.get_rect()
        text_rect.center = (500, 200)
        screen.blit(text, text_rect)
        pygame.display.update()

        text = convo_font.render(' (1) No ', True, white, black)
        text_rect = text.get_rect()
        text_rect.center = (243, 600)
        screen.blit(text, text_rect)
        pygame.display.update()

        text = convo_font.render(' (2) Yes ', True, white, black)
        text_rect = text.get_rect()
        text_rect.center = (246, 625)
        screen.blit(text, text_rect)
        pygame.display.update()

        text = convo_font.render(' (3) More Choices ', True, white, black)
        text_rect = text.get_rect()
        text_rect.center = (286, 650)
        screen.blit(text, text_rect)
        pygame.display.update()

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    pygame.display.update()
                    pygame.display.flip()
                    convo_font.set_underline(True)
                    text = convo_font.render(' (1) No ', True, white, black)
                    text_rect = text.get_rect()
                    text_rect.center = (248, 600)
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    pygame.display.flip()

                    pygame.time.delay(2000)
                    asteroid_choices.say_no_1()

            if event.key == pygame.K_2:
                while True:
                    pygame.display.update()
                    pygame.display.flip()
                    convo_font.set_underline(True)
                    text = convo_font.render(' (2) Yes ', True, white, black)
                    text_rect = text.get_rect()
                    text_rect.center = (242, 625)
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    pygame.display.flip()

            if event.key == pygame.K_3:
                while True:
                    pygame.display.update()
                    pygame.display.flip()
                    convo_font.set_underline(True)
                    text = convo_font.render(' (3) More Choices ', True, white, black)
                    text_rect = text.get_rect()
                    text_rect.center = (286, 650)
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    pygame.display.flip()
