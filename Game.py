import pygame
import Menu
import Towers
import Enemy
import time

pygame.init()


class Graphics:
    def __init__(self):
        self.star_img = pygame.image.load("star.png")
        self.star_img.set_colorkey((255, 255, 255))
        self.star_img = pygame.transform.scale(self.star_img, (50, 50))
        self.health_img = pygame.image.load("health.png")
        self.health_img.set_colorkey((255, 255, 255))
        self.health_img = pygame.transform.scale(self.health_img, (50, 50))

    def draw(self, win, money, health):
        win.blit(self.star_img, (20, 500))
        text = pygame.font.SysFont("arial", 50)
        text = text.render(str(money), 1, (255, 255, 255))
        win.blit(text, (75, 500))
        win.blit(self.health_img, (20, 450))
        text = pygame.font.SysFont("arial", 50)
        text = text.render(str(health), 1, (255, 255, 255))
        win.blit(text, (75, 450))


class Music:
    def __init__(self):
        pygame.mixer_music.load("song.mp3")
        pygame.mixer_music.play(-1)

    def off(self):
        pygame.mixer.music.pause()

    def con(self):
        pygame.mixer.music.unpause()


def gen(n):
    temp = []
    x = 0
    y = 80
    for i in range(n):
        temp.append(Enemy.Enem(x, y))
        x -= 80
    return temp


class Game:
    def __init__(self):
        self.width = 1000
        self.height = 562
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load("bg.png")
        self.vm = Menu.VerticalMenu(945, 280)
        self.vm.all_buttons()
        self.mus = Music()
        self.money = 500
        self.towers = []
        self.waves = [gen(2), gen(4), gen(6), gen(7), gen(8)]
        self.waves_i = 0
        self.enemies = self.waves[self.waves_i]
        self.health = 10
        self.graph = Graphics()
        self.wn = False
        self.tower_place = [[281, 153 - 40, False], [447, 152 - 40, False], [656, 166 - 40, False],
                            [546, 341 - 40, False], [270, 387 - 40, False],
                            [363, 514 - 40, False], [539, 515 - 40, False]]

    def run(self):
        r = True
        FPS = 60
        clock = pygame.time.Clock()
        while r:
            clock.tick(FPS)
            if self.health <= 0:
                r = False
            if not self.enemies:
                self.waves_i += 1
                if self.waves_i >= len(self.waves):
                    self.wn = True
                    r = False
                else:
                    self.enemies = self.waves[self.waves_i]
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    r = False
                elif events.type == pygame.KEYUP:
                    if events.key == pygame.K_1:
                        self.mus.off()
                    elif events.key == pygame.K_2:
                        self.mus.con()
                for buttons in self.vm.but:
                    if events.type == pygame.MOUSEBUTTONDOWN and buttons.click() and self.money >= buttons.cost:
                        for but in self.vm.but:
                            but.selected = False
                        buttons.selected = True
                    bo = True
                    for but in self.vm.but:
                        if but.click():
                            bo = False
                    if bo and buttons.selected and events.type == pygame.MOUSEBUTTONDOWN:
                        """
                        Tower будет получать координаты и ставиться на это место
                        """
                        if buttons.ty == "ArcherTower":
                            temp = Towers.ArcherTower(0, 0)
                            if self.money >= temp.price:
                                pos = pygame.mouse.get_pos()
                                for i in range(len(self.tower_place)):
                                    if abs(self.tower_place[i][0] - pos[0]) <= 25 and abs(
                                            self.tower_place[i][1] - pos[1]) <= 20 and not self.tower_place[i][2]:
                                        pos1 = self.tower_place[i][0]
                                        pos2 = self.tower_place[i][1]
                                        temp = Towers.ArcherTower(pos1, pos2)
                                        self.towers.append(temp)
                                        self.money -= temp.price
                                        self.tower_place[i][2] = True
                        buttons.selected = False
                        pygame.mouse.set_visible(True)
            for i in range(len(self.enemies)):
                if self.enemies[i].path_pos == len(self.enemies[i].path) - 1:
                    self.enemies.pop(i)
                    self.health -= 1
                    break
                self.enemies[i].move()
                if not self.enemies[i].live:
                    self.enemies.pop(i)
                    self.money += 30
                    break
            for t in self.towers:
                t.fire(self.enemies)
            self.draw()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.vm.draw(self.win)
        for en in self.enemies:
            en.draw(self.win)
        for tow in self.towers:
            tow.draw(self.win)
        for buttons in self.vm.but:
            if buttons.selected:
                pygame.mouse.set_visible(False)
                pos = pygame.mouse.get_pos()
                if buttons.ty == "ArcherTower":
                    temp = Towers.ArcherTower(*pygame.mouse.get_pos())
                self.win.blit(temp.img,
                              (pos[0] - temp.img.get_width() // 2, pos[1] - temp.img.get_height() // 2))
                for tmp in self.tower_place:
                    if not tmp[2]:
                        pygame.draw.circle(self.win, (255, 0, 0), (tmp[0], tmp[1] + 40), 10)
        self.graph.draw(self.win, self.money, self.health)
        if self.wn:
            img = pygame.transform.scale(pygame.image.load("win.png"), (243, 100))
            self.win.blit(img, (self.width // 2 - img.get_width() // 2, self.height // 2 - img.get_height() // 2))
        pygame.display.update()
        if self.wn:
            time.sleep(5)


g = Game()
g.run()
