import math
import cmath

#---------------------------------------------------------

# Graph Input

from GraphInput import graphInput

g = graphInput("AdjMatrix.txt")
n = len(g)

#---------------------------------------------------------

# Calculate Resultant Force

from Vector import Vector

def force(i, n, pos, graph):
    resultantForce = Vector(0,0)
    for j in range(0, n):
        if i  == j:
            continue
        else:
            direc = pos[i].vectorTo(pos[j])
            unitDirec = direc.unitVector()
            d = direc.length()

            if graph[i][j] != "MAX":
                x = d - (300 + 100*(int(graph[i][j]) - 3))
            else:
                x = d - 700

            F = x

            forceVector = Vector(unitDirec.x * F, unitDirec.y * F)
            resultantForce = resultantForce.addV(forceVector)
    return resultantForce

#---------------------------------------------------------

# Visualisation

import pygame
pygame.init()
font = pygame.font.Font("Arial.ttf", 15) 

screen = pygame.display.set_mode([1000, 1200])
screen.fill((255, 255, 255))

def draw(pos):
    screen.fill((255, 255, 255))
    # i = 0
    # for p in pos:
    #     x = p.x
    #     y = p.y
    #     screen.blit(font.render(str(i), True, (0,0,0)), (int(x), int(y)))
    #     i += 1

    n = len(pos)
    for i in range(0,n):
        for j in range(0,n):
            if g[i][j] != "MAX":
                pygame.draw.line(screen, (0,0,0), (pos[i].x, pos[i].y), (pos[j].x, pos[j].y), int(g[i][j]))

    for i in range(0,n):
        pygame.draw.circle(screen, (255,0,0), (int(pos[i].x), int(pos[i].y)), int(12))

    pygame.display.flip()

def movement(graph):
    n = len(graph)
    dt = 0.01

    currentPos = []
    currentVel = []
    
    radius = 150

    for i in range(0, n):
        angle = 2 * math.pi * i / n
        point = Vector(500 + radius*math.sin(angle), 500 - radius*math.cos(angle))
        currentPos.append(point)
        currentVel.append(Vector(0,0))

    running = True
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(currentPos)
                running = False
        
        nextPos = []
        nextVel = []

        for i in range(0, n):
            f = force(i, n, currentPos, g).addV(currentVel[i].scalarMultiply(-4*(n**0.5)))
            nextVel.append(currentVel[i].addV(f.scalarMultiply(dt)))    # v = u + at
            nextPos.append(currentPos[i].addV(currentVel[i].scalarMultiply(dt).addV(f.scalarMultiply(dt*dt*0.5))))  #s = s0 + ut + 1/2 a t^2
        
        currentPos = []
        currentVel = []

        for elem in nextPos:
            currentPos.append(elem)
        for elem in nextVel:
            currentVel.append(elem)

        draw(currentPos)
    
    return currentPos

started = False
while started == False:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                started = True                    

movement(g)

pygame.quit()