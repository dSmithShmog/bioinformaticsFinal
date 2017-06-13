#Dillan Smith
#May 5, 2016
#CMPSC/BIO 300
#This work is mine unless otherwise cited


import pygame, sys
from pygame.locals import *
import random
from person import person

fps = 60
window_width = 1000
window_height = 800
line_thickness = 10
per_count = 200
black = (0, 0, 0)
white = (255, 255, 255)
red = (204, 0, 51)
blue = (51, 0, 255)
yellow = (255, 204, 0)
poss_dir = [-3, -2, -1, 0, 1, 2, 3]
poss_geno = ["00", "01", "10", "11"]
per_colors = []
global people
people = []
collidePeople = []
peopleDirX = []
peopleDirY = []
age = []


def drawArena():
    display_surface.fill(black)
    pygame.draw.rect(display_surface, white, ((0, 0), (window_width, window_height)), line_thickness * 2)


def createper(perX, perY, geno, color=blue):
    perX = random.randint(line_thickness, window_width - line_thickness)
    perY = random.randint(line_thickness, window_height - line_thickness)
    while True:
        perDirX = poss_dir[random.randint(0, len(poss_dir) - 1)]  ## -1 = left 1 = right
        perDirY = poss_dir[random.randint(0, len(poss_dir) - 1)]
        if perDirY != 0 or perDirX != 0:
            break
    if geno == '00':
        color = red
    elif geno == '10' or geno == '01':
        color = yellow
    per = person(perX, perY, line_thickness / 3, line_thickness / 3, geno, True, perDirX, perDirY, color)
    #collidePer = person(perX, perY, line_thickness / 4, line_thickness / 4, geno, True, perDirX, perDirY, color)
    #collidePeople.append(collidePer)
    people.append(per)
    # randomize directions


    per_colors.append(color)
    age.append(0)


def checkEdgeCollision(per):
    if per.top <= line_thickness or per.bottom >= (window_height - line_thickness):
        per.ydir *= -1
    if per.left <= line_thickness or per.right >= (window_width - line_thickness):
        per.xdir *= -1


def checkRectCollision(per_index):
    for i in range(0, len(people) - 1):
        if i != per_index and people[i] != 1 and people[i].children < 3 and people[per_index] < 3 and people[per_index].colliderect(people[i]):
            breed(per_index, i)


def breed(per1, per2):
    new_geno = people[per1].geno[random.randint(0, 1)] + people[per2].geno[random.randint(0, 1)]
    createper(people[per1].x + 15, people[per1].y + 15, new_geno)

    people[per1].x += 20
    people[per1].y += 20
    people[per2].x += 20
    people[per2].y += 20
    people[per1].breed = False
    people[per2].breed = False
    people[per1].children += 1
    people[per2].children += 1


def render():
    for i in range(0, len(people) - 1):
        if people[i] != 1:
            display_surface.blit(surface2, people[i])
            people[i] = move(people[i])
        #collidePeople[i] = move(collidePeople)

    for i in range(0,len(people)-1):
        if people[i] != 1:
            pygame.draw.rect(display_surface, per_colors[i], people[i])
            checkEdgeCollision(people[i])
            if people[i].breed:
                checkRectCollision(i)
    for i in range(0,len(people)-1):
        if people[i] != 1:
            if people[i].age < 8*fps:
                people[i].age += 1
            elif people[i].age > 8*fps and not people[i].breed:
                people[i].breed = True
                people[i].age += 1
            #elif people[i].age > 4*fps:
                #people[i].k = True
                #collidePeople[i].k = True
            else:
                people[i].age += 1
            if people[i].k:
                people[i] = 1



def move(per):
    per.x += per.xdir
    per.y += per.ydir
    return per


def main():
    pygame.init()
    fpsclock = pygame.time.Clock()
    global display_surface
    global surface2
    surface2 = pygame.Surface((line_thickness / 3, line_thickness / 3))
    display_surface = pygame.display.set_mode((window_width, window_height), HWSURFACE)
    pygame.display.set_caption("Get it")

    # create people with random starting positions, random directions,
    for i in range(per_count):
        if i == 0:
            createper(random.randint(line_thickness + 5, window_width - line_thickness - 5),
                      random.randint(line_thickness + 5, window_height - line_thickness - 5),
                      "00", color=red)
        elif 0 < i < 110:
            createper(random.randint(line_thickness + 5, window_width - line_thickness - 5),
                      random.randint(line_thickness + 5, window_height - line_thickness - 5),
                      poss_geno[random.randint(1, 2)], color=yellow)
        else:
            createper(random.randint(line_thickness + 5, window_width - line_thickness - 5),
                      random.randint(line_thickness + 5, window_height - line_thickness - 5),
                      '11')

    drawArena()
    for i in range(per_count):
        pygame.draw.rect(display_surface, per_colors[i], people[i])

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    # mouse movement commands

            drawArena()
            render()
            pygame.display.flip()
            fpsclock.tick(fps)


if __name__ == "__main__":
    main()