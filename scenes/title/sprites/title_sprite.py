import ppb


class TitleSprite(ppb.Sprite):
    image = ppb.Text(
        'BLOCK HERO\n\nPRESS ANY KEY',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=48),  # noqa: W605
        color=(255, 255, 255)
    )
