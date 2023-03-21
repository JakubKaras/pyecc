from dataclasses import dataclass
from galois import GF # type: ignore

class EllipticCurve:
    def __init__(self, params: list[int] | None) -> None:
        self.GF = GF(5**3)
        if params is not None:
            self.a = self.GF(params[0])
            self.b = self.GF(params[1])
        else:
            self.a = self.GF(45)
            self.b = self.GF(27)
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