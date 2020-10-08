import pygame
from pygame.draw import *

pygame.init()

FPS = 30
(length, height) = (1250, 834)
screen = pygame.display.set_mode((length, height))
'''
Ниже задаем функции для цвета всех объектов.
front_color - цвет самой нижней части фона
back_color - цвет части фона, которая выше front_color
sky_color - цвет неба (самая высокая часть фона)
height_color - цвет неба (сразу после sky_color)
back_mountains_color - цвет горы (дальняя)
front_mountains_color - цвет горы (средняя)
sun_color - цвет Солнца
bird_color - цвет птиц
mountain_color - цвет горы (ближняя)
'''
front_color = (180, 135, 149)
back_color = (254, 214, 149)
sky_color = (254, 214, 163)
height_color = (254, 214, 197)
back_mountains_color = (252, 153, 45)
front_mountains_color = (173, 65, 49)
sun_color = (252, 239, 27)
bird_color = (64, 27, 3)
mountain_color = (44, 7, 33)


def bird(a, b, size):
    '''
    Данная функция рисует птиц.
    size - размер птичек (их масштаб)
    a - координаты по х
    b - координаты по у
    С помощью q и w задаем форму птиц
    '''
    q = []
    w = []
    for k in range(a, a + 15 * size, 1):
        q.append((k, (0.15 / size) * (k - a - 10 * size)**2 + b - 15 * size))
        w.append((2 * a - k, (0.15 / size) * (k - a - 10 * size)**2 + b - 15 * size))
    for k in range(a + 1, a + 15, -1):
        q.append((k, (1 / 20 / size) * (k - a - 15 * size)**2 + b - 11.25 * size))
        w.append((2 * a - k, (1 / 20 / size) * (k - a - 15 * size)**2 + b - 11.25 * size))
    polygon(screen, bird_color, q)
    polygon(screen, bird_color, w)
'''
Зададим вид самой высокой части фона и той, что чуть ниже.
Отсчет идет с начала координат. 
height - по оси у
length - по оси х
'''
rect(screen, sky_color, (0, 0 * height, length, 0.25 * height))
rect(screen, height_color, (0, 0.25 * height, length, 0.26 * height))
'''
Зададим вид дальней горы (расположена на самом верху).
'''
polygon(screen, back_mountains_color,
        [(0, 0.5 * height), (0, 0.4 * height),
         (0.06 * length, 0.38 * height),
         (0.18 * length, 0.2 * height),
         (0.24 * length, 0.24 * height),
         (0.27 * length, 0.3 * height),
         (0.44 * length, 0.45 * height),
         (0.5 * length, 0.4 * height),
         (0.55 * length, 0.39 * height),
         (0.6 * length, 0.42 * height),
         (0.64 * length, 0.4 * height),
         (0.7 * length, 0.35 * height),
         (0.8 * length, 0.24 * height),
         (0.82 * length, 0.2 * height),
         (0.85 * length, 0.21 * height),
         (0.9 * length, 0.34 * height),
         (0.96 * length, 0.3 * height),
         (length, 0.2 * height), (length, 0.4 * height)])
'''
Зададим вид солнца.
'''
circle(screen, sun_color, (int(0.5 * length), int(0.25 * height)), 80)
'''
Зададим разположение и размер части фона, которая вторая снизу.
'''
rect(screen, back_color, (0, 0.5 * height, length, 0.25 * height))
'''
Зададим вид и место средней горы.
'''
ellipse(screen, front_mountains_color, (0.04 * length, 0.45 * height, 200, 400))
ellipse(screen, front_mountains_color, (0.62 * length, 0.55 * height, 140, 380))
polygon(screen, front_mountains_color,
        [(0, 0.75 * height), (0, 0.55 * height), (0.2 * length, 0.75 * height), (0.27 * length, 0.6 * height),
         (0.35 * length, 0.7 * height),
         (0.38 * length, 0.55 * height), (0.48 * length, 0.6 * height), (0.54 * length, 0.7 * height),
         (0.62 * length, 0.68 * height), (0.68 * length, 0.55 * height),
         (0.8 * length, 0.65 * height), (0.88 * length, 0.55 * height), (0.93 * length, 0.6 * height),
         (length, 0.45 * height), (length, 0.75 * height)])
'''
Зададим расположение и размер самой нижней части фона.
'''
rect(screen, front_color, (0, 0.75 * height, length, 0.25 * height))
'''
Зададим вид и расположение самой ближней горы.
'''
polygon(screen, mountain_color,
        [(0, height), (0, 0.55 * height), (0.12 * length, 0.65 * height),
         (0.3 * length, 0.94 * height), (0.4 * length, 0.98 * height),
         (0.5 * length, 0.92 * height), (0.65 * length, 0.85 * height),
         (0.7 * length, 0.9 * height), (0.86 * length, 0.86 * height),
         (0.94 * length, 0.66 * height), (length, 0.60 * height), (length, height)])
'''
Зададим расположение и размер птиц.
'''
bird(822, 526, 5)
bird(745, 347, 3)
bird(836, 432, 3)
bird(700, 400, 2)
bird(320, 250, 2)
bird(420, 300, 3)
bird(380, 200, 2)
bird(310, 190, 1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
