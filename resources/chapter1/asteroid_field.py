import turtle
import math
import random
import pygame
from resuable_functions import dialogue, update_and_flip


# Things to remember-
# Use the arrow keys to move your ship.
# Use the space bar to fire your weapon. (if applicable)
#   -But beware, shooting asteroids causes debris which can be unseen and can cause damage to your ship.
# Your rocket is using sophisticated technology-
#   - When you engage your warp drive (moving forward or backward)
#       - Time stands still
#       - This can be used to your benefit, however the warp drive will not recharge and once it is out you cannot move up and down.
#  You win when you survive the asteroid field.
#  You lose when your shields get to zero.
def instructions(can_use_weapon):
    size = (800, 800)
    screen = pygame.display.set_mode(size)
    black = (0, 0, 0)
    pygame.init()
    while True:
        screen.fill(black)
        update_and_flip()
        dialogue(' T h e  A s t e r o i d  F i e l d                ', 500, 100, 20)
        dialogue(' Instructions                                     ', 635, 150, 20)
        dialogue(' Use the arrow keys (up, down, left, right) to move your ship.', 370, 250, 15)
        dialogue('  Use the space bar to fire your weapon. (If you convinced the Commander...)', 425, 300, 15)
        dialogue(' -But beware, shooting asteroids can cause debris ', 425, 325, 15)
        dialogue(' which is invisible and can damage your ship.', 410, 350, 15)
        dialogue(' Your rocket is using sophisticated technology.', 300, 400, 15)
        dialogue(' - When you engage your warp drive (moving forward or backward) ', 490, 425, 15)
        dialogue(' - Time stands still. ', 350, 450, 15)
        dialogue(' - This can be used to your benefit, however the  ', 475, 475, 15)
        dialogue(' warp drive will not recharge and once it is  ', 475, 500, 15)
        dialogue(' depleted you cannot move up or down.  ', 442, 525, 15)
        dialogue(' You win when you survive the asteroid field.  ', 300, 575, 15)
        dialogue(' You lose when your shields get to zero.       ', 300, 625, 15)
        dialogue('                    Good Luck!                      ', 400, 675, 15)
        dialogue('                    (Enter)                       ', 400, 700, 12)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game(can_use_weapon)


# When distance is zero stage is cleared.
distance_to_end = 1500
# When shields are zero game is over.
shields = 100
# When warp_drive is zero player cannot move forward or backward.
warp_drive = 100
enemies = []
end_game = False


def game(can_use_weapon):
    # Set up the screen
    wn = turtle.Screen()
    wn.bgcolor('black')
    wn.title('T h e  A s t e r o i d  F i e l d')
    wn.bgpic('img/asteroid_background.gif')

    # Register the images
    wn.register_shape('img/small_rocket.gif')
    wn.register_shape('img/asteroid.gif')
    wn.register_shape('img/laser.gif')
    wn.register_shape('img/exhaust.gif')
    wn.register_shape('img/control_panel.gif')

    # Draw border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color('white')
    border_pen.penup()
    border_pen.setposition(-300, -300)
    border_pen.pendown()

    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)

    border_pen.hideturtle()

    # Draw the distance left control panel.
    global distance_to_end
    distance_pen = turtle.Turtle()
    distance_pen.speed(0)
    distance_pen.color('white')
    distance_pen.penup()
    distance_pen.setposition(-280, -370)
    distance_string = f'Distance \nto end:\n '
    distance_pen.write(distance_string, False, align='left', font=('Monospace', 12, 'normal'))
    distance_pen.hideturtle()

    distance_value_pen = turtle.Turtle()
    distance_value_pen.speed(0)
    distance_value_pen.color('white')
    distance_value_pen.penup()
    distance_value_pen.setposition(-280, -385)
    distance_value_string = f'{distance_to_end}m'
    distance_value_pen.write(distance_value_string, False, align='left', font=('Monospace', 20, 'normal'))
    distance_value_pen.hideturtle()

    # Shields control panel.
    global shields
    shields_pen = turtle.Turtle()
    shields_pen.speed(0)
    shields_pen.color('white')
    shields_pen.penup()
    shields_pen.setposition(180, -335)
    shields_string = f'Shields: '
    shields_pen.write(shields_string, False, align='left', font=('Monospace', 10, 'normal'))
    shields_pen.hideturtle()

    shields_value_pen = turtle.Turtle()
    shields_value_pen.speed(0)
    shields_value_pen.color('white')
    shields_value_pen.penup()
    shields_value_pen.setposition(180, -355)
    shields_value_string = f'{shields}% '
    shields_value_pen.write(shields_value_string, False, align='left', font=('Monospace', 15, 'normal'))
    shields_value_pen.hideturtle()

    # Warp Drive control panel.
    global warp_drive
    warp_drive_pen = turtle.Turtle()
    warp_drive_pen.speed(0)
    warp_drive_pen.color('white')
    warp_drive_pen.penup()
    warp_drive_pen.setposition(180, -375)
    warp_drive_string = f'Warp: '
    warp_drive_pen.write(warp_drive_string, False, align='left', font=('Monospace', 10, 'normal'))
    warp_drive_pen.hideturtle()

    warp_drive_value_pen = turtle.Turtle()
    warp_drive_value_pen.speed(0)
    warp_drive_value_pen.color('white')
    warp_drive_value_pen.penup()
    warp_drive_value_pen.setposition(180, -395)
    warp_drive_value_string = f'{warp_drive}% '
    warp_drive_value_pen.write(warp_drive_value_string, False, align='left', font=('Monospace', 15, 'normal'))
    warp_drive_value_pen.hideturtle()

    # Create the control panel
    control_panel = turtle.Turtle()
    control_panel.shape('img/control_panel.gif')
    control_panel.penup()
    control_panel.setposition(0, -350)

    # Create the player
    player = turtle.Turtle()
    player.shape('img/small_rocket.gif')
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)

    # Create the exhaust
    exhaust = turtle.Turtle()
    exhaust.shape('img/exhaust.gif')
    exhaust.penup()
    exhaust.speed(0)
    exhaust.setposition(0, -325)
    exhaust.setheading(90)
    exhaust.hideturtle()

    player_speed = 15

    def here_they_come():
        number_of_enemies = 8
        global enemies

        # Add enemies to the list
        for i in range(number_of_enemies):
            enemies.append(turtle.Turtle())

        for enemy in enemies:
            # Create the enemy
            enemy.shape('img/asteroid.gif')
            enemy.penup()
            enemy.speed(0)
            x = random.randint(-200, 200)
            y = random.randint(250, 280)
            enemy.setposition(x, y)

    enemy_speed = 20

    # Create the laser
    weapon = turtle.Turtle()
    weapon.color('blue')
    weapon.shape('img/laser.gif')
    weapon.penup()
    weapon.speed(0)
    weapon.setheading(90)
    weapon.shapesize(0.5, 0.5)
    weapon.hideturtle()

    weapon_speed = 20

    # Functions
    def move_left():
        x = player.xcor()
        x -= player_speed
        if x < -280:
            x = -280
        player.setx(x)
        exhaust.setx(x)

    def move_right():
        x = player.xcor()
        x += player_speed
        if x > 280:
            x = 280
        player.setx(x)
        exhaust.setx(x)

    def move_up():
        global warp_drive
        y = player.ycor()
        # Player cannot move up if ward drive is at zero.
        if warp_drive == 0:
            y += 0
        else:
            y += player_speed
        if y > 265:
            y = 265
        player.sety(y)
        exhaust.sety(y - 75)
        exhaust.showturtle()
        exhaust.hideturtle()

        if y < 265:
            global distance_to_end
            distance_to_end -= 2
            distance_value_pen.clear()
            # Make sure gauge cannot go below zero.
            if distance_to_end < 0:
                distance_to_end = 0
            distance_value_string = f'{distance_to_end} m'
            distance_value_pen.write(distance_value_string, False, align='left', font=('Monospace', 15, 'normal'))

        # Not allow warp to be used if zero, otherwise decrease by 1.
        if warp_drive == 0:
            warp_drive -= 0
        else:
            warp_drive -= 1
            warp_drive_value_pen.clear()
            warp_drive_value_string = f'{warp_drive}% '
            warp_drive_value_pen.write(warp_drive_value_string, False, align='left', font=('Monospace', 15, 'normal'))

    def move_down():
        global warp_drive
        y = player.ycor()
        # Player cannot move down if warp drive is at zero.
        if warp_drive == 0:
            y -= 0
        else:
            y -= player_speed
        if y < -265:
            y = -265
        player.sety(y)
        exhaust.sety(y - 75)
        exhaust.showturtle()
        exhaust.hideturtle()

        if y > -265:
            global distance_to_end
            distance_to_end += 2
            distance_value_pen.clear()
            # Make sure gauge cannot go below zero.
            if distance_to_end < 0:
                distance_to_end = 0
            distance_value_string = f'{distance_to_end} m'
            distance_value_pen.write(distance_value_string, False, align='left', font=('Monospace', 15, 'normal'))

        # Not allow warp to be used if zero, otherwise decrease by 1.
        if warp_drive == 0:
            warp_drive -= 0
        else:
            warp_drive -= 1
            warp_drive_value_pen.clear()
            warp_drive_value_string = f'{warp_drive}% '
            warp_drive_value_pen.write(warp_drive_value_string, False, align='left', font=('Monospace', 15, 'normal'))

    def fire_weapon():
        global weapon_state
        weapon_state = 'ready'
        if weapon_state == 'ready':
            weapon_state = 'fire'
            # Move the weapon to just above the player.
            x = player.xcor()
            y = player.ycor() + 10
            weapon.setposition(x, y)
            weapon.showturtle()

    def is_collision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
        if distance < 20:
            return True
        else:
            return False

    # Key binding
    wn.listen()
    wn.onkeypress(move_left, 'Left')
    wn.onkeypress(move_right, 'Right')
    wn.onkeypress(move_up, 'Up')
    wn.onkeypress(move_down, 'Down')
    # Allow use of weapon based on previous conversation
    if can_use_weapon:
        wn.onkeypress(fire_weapon, 'space')

    # Main game loop
    # Initialize first wave
    here_they_come()
    while distance_to_end > 0:
        global end_game
        if end_game:
            break

        player.showturtle()
        global enemies
        for enemy in enemies:
            # Move the enemy
            x = enemy.xcor()
            x += enemy_speed
            enemy.setx(x)

            # Boundary check, then drop.
            if enemy.xcor() > 270:
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemy_speed *= -1
                distance_to_end -= 5
                distance_value_pen.clear()
                # Make sure gauge cannot go below zero.
                if distance_to_end < 0:
                    distance_to_end = 0
                distance_value_string = f'{distance_to_end} m'
                distance_value_pen.write(distance_value_string, False, align='left', font=('Monospace', 15, 'normal'))

            if enemy.xcor() < -270:
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemy_speed *= -1
                distance_to_end -= 5
                distance_value_pen.clear()
                # Make sure gauge cannot go below zero.
                if distance_to_end < 0:
                    distance_to_end = 0
                distance_value_string = f'{distance_to_end} m'
                distance_value_pen.write(distance_value_string, False, align='left', font=('Monospace', 15, 'normal'))

            # Reset enemy after it drops below screen.
            if enemy.ycor() < -280:
                x = random.randint(-200, 200)
                y = random.randint(250, 280)
                enemy.setposition(x, y)

            # Check for laser collision.
            if is_collision(weapon, enemy):
                # Reset the weapon
                weapon.hideturtle()
                weapon_state = 'ready'
                weapon.setposition(0, -400)
                # Send enemy back to a random spot.
                x = random.randint(-200, 200)
                y = random.randint(250, 280)
                enemy.setposition(x, y)

            # Check for collision between player and enemy
            if is_collision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()

                # Decrease shields when hit
                shields -= 10
                shields_value_pen.clear()
                shields_value_string = f'{shields}% '
                shields_value_pen.write(shields_value_string, False, align='left', font=('Monospace', 15, 'normal'))
                if shields == 0:
                    print('Game Over')
                    end_game = True
                    break

        # Move laser
        y = weapon.ycor()
        y += weapon_speed
        weapon.sety(y)

        if weapon.ycor() > 275:
            weapon.hideturtle()
            weapon_state = 'ready'

# Need to add screens for winning and losing.
