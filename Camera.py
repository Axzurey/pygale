from pygame import Vector3, Vector2
from math import radians, cos, sin, tan
import numpy as np

class Camera:
    position: Vector3
    rotation: Vector3
    fov: int = 70

    screenSize: Vector2

    def __init__(self, screenSize: Vector2) -> None:
        self.position = Vector3()
        self.rotation = Vector3()
        self.screenSize = screenSize

    def project_perspective(self, point: Vector3):

        rx, ry, rz = radians(self.rotation.x), radians(self.rotation.y), radians(self.rotation.z)

        a = np.matrix([
            [point.x],
            [point.y],
            [point.z]
        ])

        c = np.matrix([
            [self.position.x],
            [self.position.y],
            [self.position.z]
        ])

        x_rotation_matrix = np.matrix([
            [1, 0, 0],
            [0, cos(rx), sin(rx)],
            [0, -sin(rx), cos(rx)]
        ]);

        y_rotation_matrix = np.matrix([
            [cos(ry), 0, -sin(ry)],
            [0, 1, 0],
            [sin(ry), 0, cos(ry)]
        ]);

        z_rotation_matrix = np.matrix([
            [cos(rz), sin(rz), 0],
            [-sin(rz), cos(rz), 0],
            [0, 0, 1]
        ])

        d = x_rotation_matrix * y_rotation_matrix * z_rotation_matrix * (a - c)

        near = 1
        far = 100

        aspect = self.screenSize[0] / self.screenSize[1]

        fov = radians(self.fov)

        yScale = 1 / tan(fov / 2)
        xScale = yScale / aspect

        nearSubFar = near - far

        fovMatrix = np.matrix([
            [xScale, 0, 0, 0],
            [0, yScale, 0, 0],
            [0, 0, (far + near) / nearSubFar, -1],
            [0, 0, 2 * far * near / nearSubFar, 0]
        ])

        #https://stackoverflow.com/questions/6060169/is-this-a-correct-perspective-fov-matrix

        d = list(d.flat)

        l = np.matrix([
            [d[0]],
            [d[1]],
            [d[2]],
            [1]
        ])

        d = fovMatrix * l
        
        b = Vector2(d[0], d[1])

        #print(point, f, b, 'done')

        return b