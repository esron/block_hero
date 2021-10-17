# PPB Game

This game is a minimalist [Archero](https://play.google.com/store/apps/details?id=com.habby.archero&hl=pt_BR&gl=US) clone using [ppb](https://ppb.dev/)

## Project organization

In the `scenes` directory you are going to find a subfolder for every `Scene`. Every `Scene` is composed of a `scene.py` file (the `Scene` itself) and `Sprites` witch are in the `sprites` directory of the `Scene`.

Fonts are stored globally in the `fonts` directory.

A `Scene` should be responsible for all the logic that does not belongs to a `Sprite` in that `Scene`, and the scenes transactions logic.

A `Sprite` should holds all the sprite behavior and logic.

For examples, the `Player` sprite is responsible for moving the player, creating projectiles, etc., but not responsible for the pause and game over scenes transactions.


## Contributing

Create a Python virtual env:
```bash
$ python -m venv .venv
```

Install dependencies:
```bash
$ pip install -r requirements.txt
```

Install pre-commit:
```bash
$ pre-commit install
```
