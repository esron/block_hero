import ppb


class TitleSprite(ppb.Sprite):
    image = ppb.Text(
        f'BLOCK HERO\n\nPRESS ANY KEY',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=48),
        color=(255, 255, 255)
    )
