from pygame import Vector3, Vector2
from math import radians, cos, sin, pi
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

        fov = radians(self.fov)

        rx, ry, rz = radians(self.rotation.x), radians(self.rotation.y), radians(self.rotation.z)

        e = Vector3(self.screenSize.x // 2, self.screenSize.y // 2, 1) - self.position

        point_matrix = np.matrix([
            [point.x],
            [point.y],
            [point.z]
        ])

        position_matrix = np.matrix([
            [self.position.x],
            [self.position.y],
            [self.position.z]
        ])

        x_rotation_matrix = np.matrix([
            [1, 0, 0],
            [0, cos(rx), sin(rx)],
            [0, -sin(rx), cos(rz)]
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

        d = x_rotation_matrix * y_rotation_matrix * z_rotation_matrix * (point_matrix - position_matrix)

        f = list((np.matrix([
            [1, 0, e.x / e.z],
            [0, 1, e.y / e.z],
            [0, 0, 1 / e.z]
        ]) * d).flat) #type: ignore

        b = Vector2(f[0] / f[2], f[1] / f[2])

        #print(point, f, b)

        return b