import math
import pygame

pygame.init()


class Enem:
    def __init__(self, x, y):
        self.live = True
        self.health = 4000
        self.max_health = 4000
        self.vel = 1
        self.path = [(76, 80), (138, 56), (193, 80), (683, 79), (756, 152), (716, 241), (505, 265), (452, 309),
                     (450, 555), (450, 600)]
        self.x = x
        self.y = y
        self.path_pos = 0
        self.i = 0
        self.img_left = [pygame.image.load("run_left (1).png"), pygame.image.load("run_left (2).png"),
                         pygame.image.load("run_left (3).png"), pygame.image.load("run_left (4).png"),
                         pygame.image.load("run_left (5).png"), pygame.image.load("run_left (6).png"),
                         pygame.image.load("run_left (7).png"), pygame.image.load("run_left (8).png"),
                         pygame.image.load("run_left (9).png"), pygame.image.load("run_left (10).png"),
                         pygame.image.load("run_left (11).png")]
        self.img_right = [pygame.image.load("run_right (1).png"), pygame.image.load("run_right (2).png"),
                          pygame.image.load("run_right (3).png"), pygame.image.load("run_right (4).png"),
                          pygame.image.load("run_right (5).png"), pygame.image.load("run_right (6).png"),
                          pygame.image.load("run_right (7).png"), pygame.image.load("run_right (8).png"),
                          pygame.image.load("run_right (9).png"), pygame.image.load("run_right (10).png"),
                          pygame.image.load("run_right (11).png")]
        for i in range(len(self.img_right)):
            self.img_right[i] = pygame.transform.scale(self.img_right[i], (94, 80))
        for i in range(len(self.img_left)):
            self.img_left[i] = pygame.transform.scale(self.img_left[i], (94, 80))
        self.width = self.img_right[0].get_width()
        self.height = self.img_right[0].get_height()

    def move(self):
        if (self.path[self.path_pos][0] - self.x) <= 5 and (self.path[self.path_pos][1] - self.y) <= 5:
            self.path_pos += 1
        x1, y1 = self.x, self.y
        x2, y2 = self.path[self.path_pos]
        self.x += (x2 - x1) / math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * self.vel
        self.y += (y2 - y1) / math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * self.vel

    def draw(self, win):
        if self.path[self.path_pos][0] - self.x < 0:
            win.blit(self.img_left[self.i], (self.x - self.width // 2, self.y - self.height // 2))
        else:
            win.blit(self.img_right[self.i], (self.x - self.width // 2, self.y - self.height // 2))
        self.i += 1
        if self.i >= len(self.img_right):
            self.i = 0
        self.health_bar(win)

    def set_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.live = False
        else:
            self.live = True

    def health_bar(self, win):
        length = 75
        move_by = length / self.max_health
        health_bar = move_by * self.health
        pygame.draw.rect(win, (255, 0, 0), (self.x - self.width // 2, self.y - self.height // 2, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x - self.width // 2, self.y - self.height // 2, health_bar, 10), 0)
