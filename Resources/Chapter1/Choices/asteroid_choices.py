import pygame


pygame.init()
size = (800, 800)
white = (255, 255, 255)
screen = pygame.display.set_mode(size)
black = (0, 0, 0)
convo_font = pygame.font.SysFont('monospace', 15)


def say_no_1():
    convo_font.set_underline(False)
    pygame.display.update()
    pygame.display.flip()
    text = convo_font.render(' The Prime Directive states that you are not allowed'
                             , True, white, black)
    text_rect = text.get_rect()
    text_rect.center = (510, 100)
    screen.blit(text, text_rect)
    pygame.display.update()

    text = convo_font.render('to shoot an asteroid. The resulting debris may have'
                             , True, white, black)
    text_rect = text.get_rect()
    text_rect.center = (510, 150)
    screen.blit(text, text_rect)
    pygame.display.update()

    text = convo_font.render('negative consequences for other civilizations.     '
                             , True, white, black)
    text_rect = text.get_rect()
    text_rect.center = (510, 200)
    screen.blit(text, text_rect)
    pygame.display.update()

    text = convo_font.render(' Are you ready to enter the asteroid field?          '
                             , True, white, black)
    text_rect = text.get_rect()
    text_rect.center = (510, 250)
    screen.blit(text, text_rect)
    pygame.display.update()

    while True:
        pygame.display.update()
        pygame.display.flip()
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

                    pygame.time.delay(2000)

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

                    pygame.time.delay(2000)