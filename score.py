import ppb

class Score(ppb.Sprite):
    position = ppb.Vector(-10, 8)
    points = 0
    image = ppb.Text(
        f'SCORE  {points}',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=12),
        color=(255, 255, 255)
    )
