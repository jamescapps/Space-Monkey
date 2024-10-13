import turtle
import math
import random
import pygame
import time
from resources.resuable_functions import dialogue, update_and_flip
from resources.intro import title_screen
from resources.chapter1 import pre_asteroid
from resources.chapter2 import pre_dream

# Game constants
SCREEN_SIZE = (800, 800)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAX_ENEMIES = 8

# Game status variables
distance_to_end = 1500
shields = 100
warp_drive = 100
enemies = []
end_game = False

def instructions(can_use_weapon):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    while True:
        screen.fill(BLACK)
        update_and_flip()
        render_instructions(screen)
        
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            game(can_use_weapon)

def render_instructions(screen):
    instructions_text = [
        ('T h e  A s t e r o i d  F i e l d', 500, 100, 20),
        ('Instructions', 635, 150, 20),
        ('From now on there will be 2 windows. Make sure they are side by side.', 425, 200, 15),
        ('Use the arrow keys (up, down, left, right) to move your ship.', 370, 250, 15),
        ('Use the space bar to fire your weapon (If you convinced the Commander...).', 425, 300, 15),
        ('But beware, shooting asteroids may cause debris...', 425, 325, 15),
        ('Your rocket is using sophisticated technology.', 300, 375, 15),
        ('When you engage your warp drive (moving forward or backward) time stands still.', 350, 425, 15),
        ('This can be used to your benefit, however, the warp drive will not recharge.', 475, 450, 15),
        ('You win when you survive the asteroid field.', 300, 550, 15),
        ('You lose when your shields get to zero.', 300, 600, 15),
        ('Good Luck!', 400, 650, 15),
        ('Press Enter to continue.', 400, 675, 12)
    ]
    for text, x, y, size in instructions_text:
        dialogue(text, x, y, size)

def game(can_use_weapon):
    wn = setup_game_screen()
    register_images(wn)
    
    control_panel = create_control_panel(wn)
    player, exhaust = create_player_and_exhaust(wn)
    distance_pen, shields_pen, warp_drive_pen = create_control_panels(wn)

    global enemies
    enemies = create_enemies(MAX_ENEMIES)

    bind_key_controls(wn, player, exhaust, can_use_weapon)
    main_game_loop(wn, player, exhaust, distance_pen, shields_pen, warp_drive_pen, can_use_weapon)

def setup_game_screen():
    wn = turtle.Screen()
    wn.bgcolor('black')
    wn.title('T h e  A s t e r o i d  F i e l d')
    wn.bgpic('img/asteroid_background.gif')
    return wn

def register_images(wn):
    image_files = ['small_rocket.gif', 'asteroid.gif', 'laser.gif', 'exhaust.gif', 'control_panel.gif']
    for image in image_files:
        wn.register_shape(f'img/{image}')

def create_control_panel(wn):
    control_panel = turtle.Turtle()
    control_panel.shape('img/control_panel.gif')
    control_panel.penup()
    control_panel.setposition(0, -350)
    return control_panel

def create_player_and_exhaust(wn):
    player = create_turtle('img/small_rocket.gif', 0, -250, 90)
    exhaust = create_turtle('img/exhaust.gif', 0, -325, 90, hidden=True)
    return player, exhaust

def create_turtle(shape, x, y, heading, hidden=False):
    t = turtle.Turtle()
    t.shape(shape)
    t.penup()
    t.speed(0)
    t.setposition(x, y)
    t.setheading(heading)
    if hidden:
        t.hideturtle()
    return t

def create_control_panels(wn):
    distance_pen = create_status_display(-280, -370, 'Distance\nto end:', 12)
    shields_pen = create_status_display(180, -335, 'Shields:', 10)
    warp_drive_pen = create_status_display(180, -375, 'Warp:', 10)
    return distance_pen, shields_pen, warp_drive_pen

def create_status_display(x, y, label, font_size):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.setposition(x, y)
    pen.write(label, False, align='left', font=('Monospace', font_size, 'normal'))
    pen.hideturtle()
    return pen

def create_enemies(number_of_enemies):
    enemies = []
    for _ in range(number_of_enemies):
        enemy = create_turtle('img/asteroid.gif', random.randint(-200, 200), random.randint(250, 280), 0)
        enemies.append(enemy)
    return enemies

def bind_key_controls(wn, player, exhaust, can_use_weapon):
    player_speed = 15
    wn.listen()
    wn.onkeypress(lambda: move_left_right(player, exhaust, -player_speed), 'Left')
    wn.onkeypress(lambda: move_left_right(player, exhaust, player_speed), 'Right')
    wn.onkeypress(lambda: move_up_down(player, exhaust, player_speed, 'up'), 'Up')
    wn.onkeypress(lambda: move_up_down(player, exhaust, -player_speed, 'down'), 'Down')
    
    if can_use_weapon:
        weapon = create_weapon(wn)
        wn.onkeypress(lambda: fire_weapon(weapon, player), 'space')

def move_left_right(player, exhaust, speed):
    x = player.xcor() + speed
    x = min(max(x, -280), 280)
    player.setx(x)
    exhaust.setx(x)

def move_up_down(player, exhaust, speed, direction):
    global warp_drive, distance_to_end
    y = player.ycor() + speed if warp_drive > 0 else player.ycor()
    y = min(max(y, -265), 265)
    player.sety(y)
    exhaust.sety(y - 75)
    
    if warp_drive > 0:
        exhaust.showturtle()
        exhaust.hideturtle()
        distance_to_end = max(0, distance_to_end - 2) if direction == 'up' else min(1500, distance_to_end + 2)
        warp_drive = max(0, warp_drive - 1)

def create_weapon(wn):
    weapon = create_turtle('img/laser.gif', 0, -400, 90)
    weapon.shapesize(0.5, 0.5)
    weapon.hideturtle()
    return weapon

def fire_weapon(weapon, player):
    if not weapon.isvisible():
        x, y = player.xcor(), player.ycor() + 10
        weapon.setposition(x, y)
        weapon.showturtle()

def main_game_loop(wn, player, exhaust, distance_pen, shields_pen, warp_drive_pen, can_use_weapon):
    global end_game, enemies
    enemy_speed = 20
    weapon_state = 'ready'
    while distance_to_end > 0 and not end_game:
        for enemy in enemies:
            move_enemy(enemy, enemy_speed)
            if check_collisions(player, enemy, shields_pen):
                break
            if check_laser_collision(weapon, enemy):
                reset_enemy_position(enemy)
        
        move_weapon(weapon)
        check_game_outcome(player, distance_pen)

def move_enemy(enemy, speed):
    x = enemy.xcor() + speed
    enemy.setx(x)
    if enemy.xcor() > 270 or enemy.xcor() < -270:
        drop_enemy(enemy, speed)

def drop_enemy(enemy, speed):
    for e in enemies:
        e.sety(e.ycor() - 40)
    enemy_speed *= -1

def check_collisions(player, enemy, shields_pen):
    global shields, end_game
    if is_collision(player, enemy):
        shields -= 10
        shields_pen.clear()
        shields_pen.write(f'Shields: {shields}% ', False, align='left', font=('Monospace', 15, 'normal'))
        if shields <= 0:
            end_game = True
            return True
    return False

def is_collision(t1, t2):
    return math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)) < 20

def reset_enemy_position(enemy):
    enemy.setposition(random.randint(-200, 200), random.randint(250, 280))

def move_weapon(weapon):
    if weapon.isvisible():
        y = weapon.ycor() + 40
        weapon.sety(y)
        if weapon.ycor() > 250:
            weapon.hideturtle()

def check_game_outcome(player, distance_pen):
    distance_pen.clear()
    distance_pen.write(f'{distance_to_end} Miles', False, align='left', font=('Monospace', 15, 'normal'))
    
    if distance_to_end <= 0:
        game_over(player, "Victory!")
    elif shields <= 0:
        game_over(player, "Game Over")

def game_over(player, message):
    player.hideturtle()
    print(message)


if __name__ == '__main__':
    can_use_weapon = True  
    instructions(can_use_weapon)
