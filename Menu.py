import pygame

pygame.init()


class Button:
    def click(self):
        pos = pygame.mouse.get_pos()
        if pos[0] >= self.x - self.width // 2 and pos[0] <= self.x + self.width // 2 and pos[
            1] <= self.y + self.height // 2 and pos[1] >= self.y - self.height // 2:
            return True
        return False

    def draw(self, win):
        win.blit(self.img, (self.x - self.width // 2, self.y - self.height // 2))


class VerticalButton(Button):
    def __init__(self, img, cost, ty):
        self.cost = cost
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = None
        self.y = None
        self.selected = False
        self.ty = ty

    def draw(self, win):
        win.blit(self.img, (self.x - self.width // 2, self.y - self.height // 2))


class Menu:
    def all_buttons(self):
        img_button_52 = pygame.image.load("32.png")
        img_button_52 = pygame.transform.scale(img_button_52, (70, 60))
        button_52 = VerticalButton(img_button_52, 250, "ArcherTower")
        self.add_button(button_52)

    def add_button(self, button):
        button.x = self.x
        button.y = self.y - self.height // 2 + self.sizes[-1][0] + 10
        self.sizes[-1][1] = self.sizes[-1][0] + button.height + 10
        self.sizes.append([self.sizes[-1][1] + 30, None])
        self.but.append(button)

    def draw(self, win):
        win.blit(self.img, (self.x - self.width // 2, self.y - self.height // 2))
        for button in self.but:
            button.draw(win)
            win.blit(self.star_img, (button.x - 35, 7 + button.y + button.height // 2))
            f = pygame.font.SysFont('arial', 25)
            text = f.render(str(button.cost), 1, (255, 255, 255))
            win.blit(text, (button.x, button.y + button.height // 2 + 5))


class VerticalMenu(Menu):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sizes = [[45, None]]
        self.but = []
        """Graphics"""
        self.star_img = pygame.image.load("star.png")
        self.star_img.set_colorkey((255, 255, 255))
        self.star_img = pygame.transform.scale(self.star_img, (20, 20))
        self.img = pygame.image.load("table.png")
        self.img = pygame.transform.scale(self.img, (115, 430))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
