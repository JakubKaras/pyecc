from elliptic_curves import EllipticCurve, CurvePoint
from dataclasses import dataclass
import random

@dataclass
class Public_key:
    P: CurvePoint
    Q: CurvePoint

    def __eq__(self, other):
        return (
            self.__class__ is other.__class__
            and self.P == other.P
            and self.Q == other.Q
        )

class Cipherist:
    def __init__(self, public_key: Public_key, eliptic_curve: EllipticCurve) -> None:
        self.public_key = public_key
        self.eliptic_curve = eliptic_curve
    
    def __call__(self, message: CurvePoint):
        a = self.__generate_a_value(self.eliptic_curve.order)
        return self.eliptic_curve.multiply_poit_by_integer(a ,self.public_key.P), self.eliptic_curve.sum_points(message, self.eliptic_curve.multiply_poit_by_integer( a, self.public_key.Q))
    
    def __generate_a_value(self, curve_order: int):
        return random.randint(1, curve_order -1);
    
class Decipherist:
    def __init__(self, public_key: Public_key,  private_key: int, eliptic_curve: EllipticCurve) -> None:
        self.public_key = public_key
        self.private_key = private_key
        self.eliptic_curve = eliptic_curve
    
    def __call__(self, coded_message) -> CurvePoint:
        return self.eliptic_curve.sum_points(coded_message[1], 
                                             self.eliptic_curve.inverse_of_point(
                                                 self.eliptic_curve.multiply_poit_by_integer(self.private_key, 
                                                                                             coded_message[0])))