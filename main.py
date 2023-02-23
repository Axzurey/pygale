import pygame
from pygame import Vector3
from WorldObject import WorldObject

screenSize = (1280, 720)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(screenSize)

cube = WorldObject([
    Vector3(-100, -100, -100), #bottom left
    Vector3(-100, 100, -100), #top left
    Vector3(100, -100, -100), #bottom right
    Vector3(100, 100, -100), #top right
    Vector3(-100, -100, 100), #bottom left back
    Vector3(-100, 100, 100), #top left back
    Vector3(100, -100, 100), #bottom right back
    Vector3(100, 100, 100) #top right back
], [
    [0, 1],
    [0, 2],
    [0, 4],
    [5, 1],
    [5, 4],
    [5, 7],
    [7, 6],
    [3, 2],
    [3, 1],
    [4, 6],
    [6, 2],
    [3, 7]
], [
    [0, 1, 2],
    [1, 2, 3],
    [0, 1, 4],
    [1, 4, 5],
    [1, 5, 7],
    [1, 3, 7],
    [4, 5, 6],
    [4, 6, 7],
    [2, 3, 6],
    [3, 6, 7],
    [0, 2, 4],
    [2, 4, 6]
])

cube.position = Vector3(screenSize[0] // 2, screenSize[1] // 2, 0)

while True:

    events = pygame.event.get()

    screen.fill((0, 0, 0))
    
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    cube.rotation += Vector3(0, 1, 0)

    for p0x, p1x, p2x in cube.faces:
        p0 = list(p0x.flat) #type: ignore
        p1 = list(p1x.flat) #type: ignore
        p2 = list(p2x.flat) #type: ignore

        pygame.draw.polygon(screen, (0, 255, 0), [
            (p0[0], p0[1]),
            (p1[0], p1[1]),
            (p2[0], p2[1])
        ])

    for p0x, p1x in cube.edges:
        p0 = list(p0x.flat) #type: ignore
        p1 = list(p1x.flat) #type: ignore

        pygame.draw.aaline(screen, (255, 0, 0), (p0[0], p0[1]), (p1[0], p1[1]))

    for point in cube.vertices:
        p = list(point.flat) #type: ignore
        pygame.draw.circle(screen, (0, 255, 255), (p[0], p[1]), 5)

    pygame.display.update()

    clock.tick(60)