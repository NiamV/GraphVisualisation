import math
import cmath

# Complete Graph

# n = 5
# g = [ [1 for i in range(0, n)] for j in range(0,n)]

#---------------------------------------------------------

# Graph Input

from GraphInput import graphInput

g = graphInput("AdjMatrix.txt")
n = len(g)

#---------------------------------------------------------

# Results from Dijkstra's Algorithm:

from DijkstraInput import convert

results = convert("DijkstraOutput.txt")

#---------------------------------------------------------

# Animation using pygame

import pygame
pygame.init()

screen = pygame.display.set_mode([1000, 1000])
screen.fill((255, 255, 255))
font = pygame.font.Font("Arial.ttf", 32) 

def points(a, b, i):
    x1 = a[0]
    x2 = b[0]
    xnew = x1 + (x2-x1) * i / 100

    y1 = a[1]
    y2 = b[1]
    ynew = y1 + (y2-y1) * i / 100
    
    return (xnew, ynew)

def drawArrow(a, b, current, changed, backtrack):
    if(g[a][b] != "MAX" and a != b):
        if current == True:
            if changed == True:
                colour = (0, 255, 0)
            else: 
                colour = (255, 0, 0)
        else:
            colour = (0, 0, 0)

        if backtrack == True:
            colour = (200, 200, 0)
        
        offset = 40
        radius = 300
        
        # Calculate angles and positions of the nodes
        angle1 = 2 * math.pi * a / n
        angle2 = 2 * math.pi * b / n
        point1 = (500 + radius*math.sin(angle1), 500 - radius*math.cos(angle1))
        point2 = (500 + radius*math.sin(angle2), 500 - radius*math.cos(angle2))
        
        # Calculate the direction of the arrow
        z1 = complex(point1[0], point1[1])
        z2 = complex(point2[0], point2[1])
        z3 = cmath.polar(z2 - z1)[1]        # Angle of the vector
                                            # Anticlockwise from positive x

        shift = math.pi / 2
        gap = 7
        
        # Calculate actual start and end points
        # Offset is distance to node
        # Gap is distance between arrows between two nodes
        point1 = (point1[0] + offset*math.cos(z3) + gap*math.cos(z3 + shift), point1[1] + offset*math.sin(z3) + gap*math.sin(z3 + shift))
        point2 = (point2[0] - offset*math.cos(z3) + gap*math.cos(z3 + shift), point2[1] - offset*math.sin(z3) + gap*math.sin(z3 + shift))

        # Draw arrows
        arrowEnd1 = (point2[0] + 10*math.cos(z3 - math.pi + math.pi / 6), point2[1] + 10*math.sin(z3 - math.pi + math.pi / 6))
        arrowEnd2 = (point2[0] + 10*math.cos(z3 - math.pi - math.pi / 6), point2[1] + 10*math.sin(z3 - math.pi - math.pi / 6))


        if current == True:
            for f in range(0, 100):
                # print(f)
                s = points(point1, point2, f)
                e = points(point1, point2, f + 1)
                pygame.draw.line(screen, colour, s, e, g[a][b])
                pygame.display.flip()
                pygame.time.delay(10)

            pygame.draw.line(screen, colour, point2, arrowEnd1, g[a][b])
            pygame.draw.line(screen, colour, point2, arrowEnd2, g[a][b])
            pygame.display.flip()
        
        else:
            pygame.draw.line(screen, colour, point1, point2, g[a][b])
            pygame.draw.line(screen, colour, point2, arrowEnd1, g[a][b])
            pygame.draw.line(screen, colour, point2, arrowEnd2, g[a][b])


def frame(step = []):
    source = step[0]
    target = step[1]
    changed = step[2]
    d = step[3]
    pi = step[4]
    
    for i in range(0,n):
        angle = 2 * math.pi * i / n
        if i == source:
            colour = (255, 128, 0)
        elif i == target:
            colour = (0, 0, 255)
        else:
            colour = (0, 0, 0)

        pygame.draw.circle(screen, colour, (math.floor(500 + 300*math.sin(angle)), math.floor(500 - 300*math.cos(angle))), 10)
        
        screen.blit(font.render(str(d[i]), True, (0,0,0)), (math.floor(500 + 350*math.sin(angle)), math.floor(500 - 350*math.cos(angle))))

    for j in range(0, n):
        for k in range(0,n):
            drawArrow(j, k, False, False, False)

    drawArrow(source, target, True, changed, False)

    for l in range(0, n):
        if(pi[l] != "NIL"):
            drawArrow(pi[l], l, False, False, True)
            
    pygame.display.flip()



running = True
frameNo = -1
while running:
    pygame.display.flip()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            f = frameNo
            try:
                if event.key == pygame.K_RIGHT:
                    if(frameNo < len(results) - 1):
                        frameNo += 1
                        print(frameNo)

                        screen.fill((255, 255, 255))
                        frame(results[frameNo])
                        pygame.display.flip()
                    else:
                        Exception
                if event.key == pygame.K_LEFT:
                    if(frameNo > 1):
                        frameNo -= 1
                        print(frameNo)

                        screen.fill((255, 255, 255))
                        frame(results[frameNo])
                        pygame.display.flip()
                    else:
                        Exception
            except:
                print("Invalid Key")
                frame(results[f])
                frameNo = f
                continue

        

pygame.quit()