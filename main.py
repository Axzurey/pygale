import pygame
from pygame import Vector3, Vector2
from WorldObject import WorldObject
from Camera import Camera


screenSize = (1280, 720)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(screenSize)

camera = Camera(Vector2(screenSize))
camera.position = Vector3()

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
], camera)

cube.position = Vector3(screenSize[0] // 2, screenSize[1] // 2, 15)

while True:

    events = pygame.event.get()

    screen.fill((0, 0, 0))
    
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    cube.rotation += Vector3(1, 1, 1)

    for p0, p1, p2 in cube.faces:

        pygame.draw.polygon(screen, (0, 255, 0), [
            (p0[0], p0[1]),
            (p1[0], p1[1]),
            (p2[0], p2[1])
        ])

    for p0, p1 in cube.edges:

        pygame.draw.aaline(screen, (255, 0, 0), (p0[0], p0[1]), (p1[0], p1[1]))

    for p in cube.vertices:
        pygame.draw.circle(screen, (0, 255, 255), (p[0], p[1]), 5)

    pygame.display.update()

    clock.tick(60)