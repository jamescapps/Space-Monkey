import pygame

size = (800, 800)
screen = pygame.display.set_mode(size)
black = (0, 0, 0)
white = (255, 255, 255)

commander = pygame.image.load('img/commander.png').convert()
comms_photo = pygame.image.load('img/comms_photo.png').convert()


def commander_convo():
    while True:
        screen.blit(commander, [300, 200])
        pygame.display.update()
        pygame.display.flip()

        font = pygame.font.SysFont('monospace', 20)
        text = font.render(' Space Monkey! Are you there?  Do you read me?... ', True, white, black)
        text_rect = text.get_rect()
        text_rect.center = (400, 500)
        screen.blit(text, text_rect)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(black)
                break


def monkey_convo():
    while True:
        pygame.display.update()
        pygame.display.flip()
        screen.blit(comms_photo, [300, 200])
        pygame.display.update()
        pygame.display.flip()

        font = pygame.font.SysFont('monospace', 20)
        text = font.render(' Loud and clear Commander! ', True, white, black)
        text_rect = text.get_rect()
        text_rect.center = (420, 500)
        screen.blit(text, text_rect)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(black)
                break