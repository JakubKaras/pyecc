from dataclasses import dataclass
from galois import GF # type: ignore

class EllipticCurve:
    def __init__(self, a, b) -> None:
        self.GF = GF(5**3)
        self.a = self.GF(a)
        self.b = self.GF(b)
        self.check_determinant()

    def check_determinant(self):
        d4 = 2 * self.a
        d6 = 4 * self.b
        if 117 * d4 ** 3 - 27 * d6 ** 2 == 0:
            raise ValueError(f"Curve y^2 = x^3 + {self.a}x + {self.b} is not suitable (it has zero determinant).")

@dataclass
class CurvePoint:
    x: int
    y: int