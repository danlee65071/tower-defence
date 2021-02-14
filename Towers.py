import math
import pygame
import time

pygame.init()


class Bullet:
    def __init__(self, dur, time_in):
        self.time_in = time_in
        self.dur = dur


class Towers:
    def draw(self, win):
        win.blit(self.img, (self.x - self.width // 2, self.y - self.height // 2))
        win.blit(self.img_per[self.i], (self.x - self.width // 2 + 25, self.y - self.height // 2 - 10))
        if self.fire_b:
            self.i += 1
            if self.i >= len(self.img_per):
                self.i = 0
        else:
            self.i = 0

    def fire(self, enemies):

        for enemy in enemies:
            if math.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2) <= self.radius_damage and enemy.live:
                enemy.set_health(self.damage)
                self.fire_b = True
                break
        else:
            self.fire_b = False

    def sell(self):
        return self.sell_pr


class ArcherTower(Towers):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sell_pr = 200
        self.price = 250
        ''''''
        self.img = pygame.image.load("7.png")
        self.img = pygame.transform.scale(self.img, (80, 120))
        ''''''
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.damage = 25
        self.radius_damage = 100
        self.radius = 20
        self.fire_b = False
        self.i = 0
        ''''''
        self.img_per = [pygame.image.load("38.png"), pygame.image.load("39.png"), pygame.image.load("40.png"),
                        pygame.image.load("41.png"), pygame.image.load("42.png"), pygame.image.load("43.png")]
        for i in range(len(self.img_per)):
            self.img_per[i] = pygame.transform.scale(self.img_per[i], (25, 30))
        ''''''
        self.attack_speed = 5
        self.bul = None


