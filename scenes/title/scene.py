import ppb
from ppb.events import KeyPressed, Quit, SceneStarted, StartScene
from ppb.keycodes import Q, Space
from scenes.game.scene import GameScene
from scenes.title.sprites.hold_sprite import HoldSprite
from scenes.title.sprites.quit_sprite import QuitSprite
from scenes.title.sprites.rule_one_sprite import RuleOneSprite
from scenes.title.sprites.rule_tree_sprite import RuleTreeSprite
from scenes.title.sprites.rule_two_sprite import RuleTwoSprite
from scenes.title.sprites.rules_sprite import RulesSprite
from scenes.title.sprites.start_sprite import StartSprite
from scenes.title.sprites.title_sprite import TitleSprite


class TitleScene(ppb.Scene):
    background_color = (0, 0, 0)

    def on_scene_started(self, scene_event: SceneStarted, signal):
        self.add(TitleSprite())
        self.add(RulesSprite())
        self.add(RuleOneSprite())
        self.add(RuleTwoSprite())
        self.add(RuleTreeSprite())
        self.add(HoldSprite())
        self.add(StartSprite())
        self.add(QuitSprite())

    def on_key_pressed(self, key_event: KeyPressed, signal):
        if key_event.key == Q:
            signal(Quit())
            return

        if key_event.key == Space:
            signal(StartScene(GameScene()))
