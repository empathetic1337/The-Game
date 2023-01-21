from sprite_object import *
from settings import *
from random import randint


class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/shotgun/0.png', scale=scaler, animation_time=150):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (WIDTH - self.images[0].get_width() - 50 // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 10
        self.counter = 0
        self.surf = pg.Surface((5, 3))
        self.surf.fill((255, 255, 255))
        self.surf.set_alpha(255)

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        if not self.player.shot:
            if self.counter != 25:
                self.counter += 1
            else:
                self.weapon_pos = (WIDTH - self.images[0].get_width() - 50 // 2 + randint(1, 15),
                                   HEIGHT - self.images[0].get_height() + randint(1, 15))
                self.counter = 0
            self.game.screen.blit(self.images[0], self.weapon_pos)
        else:
            self.game.screen.blit(self.images[1], self.weapon_pos)
        self.game.screen.blit(self.surf, (HALF_WIDTH, HALF_HEIGHT))

    def update(self):
        self.check_animation_time()
        self.animate_shot()