import turtle
import math
import random


# When distance is zero stage is cleared.
distance_to_end = 1000
shields = 100
enemies = []
lives_left = 3
end_game = False


def game():
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

    # Draw the distance left
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

    # Shields
    global shields
    shields_pen = turtle.Turtle()
    shields_pen.speed(0)
    shields_pen.color('white')
    shields_pen.penup()
    shields_pen.setposition(180, -335)
    shields_string = f'Shields: '
    shields_pen.write(shields_string, False, align='left', font=('Monospace', 12, 'normal'))
    shields_pen.hideturtle()

    shields_value_pen = turtle.Turtle()
    shields_value_pen.speed(0)
    shields_value_pen.color('white')
    shields_value_pen.penup()
    shields_value_pen.setposition(180, -375)
    shields_value_string = f'{shields}% '
    shields_value_pen.write(shields_value_string, False, align='left', font=('Monospace', 20, 'normal'))
    shields_value_pen.hideturtle()

    # Create the control panel
    control_panel = turtle.Turtle()
    control_panel.shape('img/control_panel.gif')
    control_panel.penup()
    control_panel.setposition(0, -350)

    # Create the player turtle
    player = turtle.Turtle()
    player.shape('img/small_rocket.gif')
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)

    # Create the exhaust turtle
    exhaust = turtle.Turtle()
    exhaust.shape('img/exhaust.gif')
    exhaust.penup()
    exhaust.speed(0)
    exhaust.setposition(0, -325)
    exhaust.setheading(90)
    exhaust.hideturtle()

    player_speed = 15

    def here_they_come():
        # Choose number of enemies
        number_of_enemies = 8
        # Create an empty list of enemies
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

    # Create the weapon
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
        y = player.ycor()
        y += player_speed
        if y > 265:
            y = 265
        player.sety(y)
        exhaust.sety(y - 75)
        exhaust.showturtle()
        exhaust.hideturtle()
        # Don't allow distance to decrease if you hit the top boundary?  Probably take away later.
        # Asteroids are stopping when button is held down.
        if y < 265:
            global distance_to_end
            distance_to_end -= 2
            distance_value_pen.clear()
            distance_value_string = f'{distance_to_end} m'
            distance_value_pen.write(distance_value_string, False, align='left', font=('Monospace', 20, 'normal'))

    def move_down():
        y = player.ycor()
        y -= player_speed
        if y < -265:
            y = -265
        player.sety(y)
        # Don't allow distance to increase if you hit bottom boundary.
        # Clear seems to get muddy when you hold down button.
        # Asteroids are stopping when button is held down.
        if y > -265:
            global distance_to_end
            distance_to_end += 2
            distance_value_pen.clear()
            distance_value_string = f'{distance_to_end} m'
            distance_value_pen.write(distance_value_string, False, align='left', font=('Monospace', 20, 'normal'))

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
            if enemy.xcor() > 280:
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemy_speed *= -1
                distance_to_end -= 5
                distance_value_pen.clear()
                distance_value_string = f'{distance_to_end} m'
                distance_value_pen.write(distance_value_string, False, align='left', font=('Monospace', 20, 'normal'))

            if enemy.xcor() < -280:
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemy_speed *= -1
                distance_to_end -= 5
                distance_value_pen.clear()
                distance_value_string = f'{distance_to_end} m'
                distance_value_pen.write(distance_value_string, False, align='left', font=('Monospace', 20, 'normal'))

            if enemy.ycor() < -280:
                x = random.randint(-200, 200)
                y = random.randint(250, 280)
                enemy.setposition(x, y)

            # Need to have more enemies appear when each batch gets about half way down the page.
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

                shields -= 10
                shields_value_pen.clear()
                shields_value_string = f'{shields}% '
                shields_value_pen.write(shields_value_string, False, align='left', font=('Monospace', 20, 'normal'))
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

