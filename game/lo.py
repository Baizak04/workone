def handle_alien_movement():
global game_time, move_aliens_down, alien_groups,
    move_aliens_right
    alien_rightmost = find_rightmost_alien()
    alien_leftmost = find_leftmost_alien()
    alien_bottommost = find_bottommost_alien()
    (move_aliens_right, move_aliens_down) =
    move_aliens(
    alien_leftmost,
    alien_rightmost,
    alien_bottommost,
    move_aliens_right,
    move_aliens_down)
    14
    15# делаем анимацию
    16for alien_group in alien_groups:
    for next_alien in alien_group:
    next_alien.switch_image(
    int(game_time/blink_speed) % 2 )
    next_alien.update()
    17
    18
    19
    20
    21
    22
    23
    24
    #проигрывать инопланетный звук каждые полсекунды
    if game_time % 400 == 0 and aliens_exist():
    alien_movement.play()118
    25
    for alien_group in alien_groups:
    for alien in alien_group:
    (x,y) = alien.position
    if move_aliens_right:
    alien.move_right()
    else:
    alien.move_left()
if move_aliens_down:
alien.move_down()
alien.update()

move_aliens_down = False