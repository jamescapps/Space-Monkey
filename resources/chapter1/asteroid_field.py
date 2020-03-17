def game():

    import turtle
    import os

    # Set up the screen
    wn = turtle.Screen()
    wn.bgcolor('black')
    wn.title('T h e  A s t e r o i d  F i e l d')

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

    # Create the player turtle
    player = turtle.Turtle()
    player.color('blue')
    player.shape('triangle')
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)

    player_speed = 10

    # Create the enemy
    enemy = turtle.Turtle()
    enemy.color('red')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(-200, 250)

    enemy_speed = 3

    # Create the weapon
    weapon = turtle.Turtle()
    weapon.color('yellow')
    weapon.shape('triangle')
    weapon.penup()
    weapon.speed(0)
    weapon.setheading(90)
    weapon.shapesize(0.5, 0.5)
    weapon.hideturtle()

    weapon_speed = 20

    # Move ship
    def move_left():
        x = player.xcor()
        x -= player_speed
        if x < -280:
            x = -280
        player.setx(x)

    def move_right():
        x = player.xcor()
        x += player_speed
        if x > 280:
            x = 280
        player.setx(x)

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

    # Key binding
    wn.listen()
    wn.onkeypress(move_left, 'Left')
    wn.onkeypress(move_right, 'Right')
    wn.onkeypress(fire_weapon, 'space')

    # Main game loop
    while True:
        # Move the enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Boundary check, then drop.
        if enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 40
            enemy_speed *= -1
            enemy.sety(y)

        if enemy.xcor() < -280:
            y = enemy.ycor()
            y -= 40
            enemy_speed *= -1
            enemy.sety(y)

        # Move laser
        y = weapon.ycor()
        y += weapon_speed
        weapon.sety(y)

        if weapon.ycor() > 275:
            weapon.hideturtle()
            weapon_state = 'ready'












