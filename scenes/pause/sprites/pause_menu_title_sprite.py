import ppb

class PauseMenuTitleSprite(ppb.Sprite):
    image = ppb.Text(
        'GAME PAUSED',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),
        color=(255, 255, 255)
    )
