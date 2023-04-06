import numpy as np
import matplotlib.pyplot as plt # type: ignore
import logging
from dataclasses import dataclass
from galois import GF # type: ignore


@dataclass
class CurvePoint:
    x: int
    y: int

    def __eq__(self, other):
        return (
            self.__class__ is other.__class__
            and self.x == other.x
            and self.y == other.y
        )

    def __str__(self):
        return f"[{self.x:>3},{self.y:>3}]"

class EllipticCurve:
    def __init__(self, params: list[int] | None) -> None:
        self.order = 5**3
        self.GF = GF(self.order)
        self.second_powers_of: dict[int, np.ndarray] = {}
        self.points: list[CurvePoint] = [CurvePoint(0, 0)]
        if params is not None:
            self.a = self.GF(params[0])
            self.b = self.GF(params[1])
        else:
            self.a = self.GF(2 % self.order)
            self.b = self.GF(9 % self.order)
        self.check_determinant()
        self.generate_second_powers()
        self.generate_points()

    def check_determinant(self):
        d4 = 2 * self.a
        d6 = 4 * self.b
        if (-8 % self.order) * d4 ** 3 - (27 % self.order) * d6 ** 2 == 0:
            raise ValueError(f"Curve y^2 = x^3 + {self.a}x + {self.b} is not suitable (it has zero determinant).")

    def generate_second_powers(self) -> None:
        second_powers = []
        for i in range(self.order):
            second_powers.append(self.GF(i) ** 2)
        self.second_powers_of.clear()
        for x in second_powers:
            integer_representation = int(x)
            if integer_representation not in self.second_powers_of.keys():
                self.second_powers_of[integer_representation] = np.where(second_powers == x)[0]

    def generate_points(self):
        self.points = [CurvePoint(0, 0)]
        for x_int in range(self.order):
            x_GF = self.GF(x_int)
            curve_x_value_GF = x_GF ** 3 + self.a * x_GF + self.b
            curve_x_value_int = int(curve_x_value_GF)
            if curve_x_value_int in self.second_powers_of.keys():
                for y_int in self.second_powers_of[curve_x_value_int]:
                    self.points.append(CurvePoint(x_int, y_int))

    def print_points(self):
        for point in self.points:
            print(point)

    def sum_points(self, point_a: CurvePoint, point_b: CurvePoint) -> CurvePoint:
        if point_a == CurvePoint(0, 0):
            return point_b
        if point_b == CurvePoint(0, 0):
            return point_a
        if point_a == point_b:
            if point_a.y == 0:
                return CurvePoint(0, 0)
            fraction = (3 * (self.GF(point_a.x) ** 2) + self.GF(self.a)) / (2 * self.GF(point_a.y))
            x = (fraction) ** 2 - 2 * self.GF(point_a.x)
            y = fraction * (self.GF(point_a.x) - x) - self.GF(point_a.y)
            return CurvePoint(int(x), int(y))
        if point_a.x == point_b.x:
            return CurvePoint(0, 0)
        fraction = (self.GF(point_b.y) - self.GF(point_a.y)) / (self.GF(point_b.x) - self.GF(point_a.x))
        x = (fraction) ** 2 - self.GF(point_a.x) - self.GF(point_b.x)
        y = fraction * (self.GF(point_a.x) - x) - self.GF(point_a.y)
        return CurvePoint(int(x), int(y))

    def multiply_point_by_integer(self, integer: int, point: CurvePoint) -> CurvePoint:
        if integer < 1:
            raise RuntimeError("Cannot multiply with given number.")
        result = point
        for _ in range(1, integer):
            result = self.sum_points(result, point)
        return result

    def inverse_of_point(self, point: CurvePoint):
        for curve_point in self.points:
            if self.sum_points(point, curve_point) == CurvePoint(0, 0):
                return curve_point

    def plot(self):
        x_coordinates = [point.x if point.x <= int(self.GF(0) - self.GF(point.x)) else -int(self.GF(0) - self.GF(point.x)) for point in self.points]
        y_coordinates = [point.y if point.y <= int(self.GF(0) - self.GF(point.y)) else -int(self.GF(0) - self.GF(point.y)) for point in self.points]
        plt.figure()
        plt.plot(x_coordinates, y_coordinates, 'o')
        plt.show()

    def print_sum_table(self):
        first_line = "     +    | | " + "  ".join([(str(point)) for point in self.points])
        m = "\n" + first_line + "\n"
        m += "_" * (9 * (len(self.points) + 1) + 2 * (len(self.points) + 1) + 1) + "\n"
        for point in self.points:
            m += str(point) + " | | "
            for point2 in self.points:
                m += str(self.sum_points(point, point2))
                m += "  "
            m += "\n"
        logging.getLogger().info(m)