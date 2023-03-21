import logging
from elliptic_curves import EllipticCurve

class User():
    def __init__(self) -> None:
        self.curve = EllipticCurve(None)

    @staticmethod
    def read_int(message: str):
        run = True
        while run:
            try:
                user_input = int(input(message))
            except:
                logging.getLogger().error("Input cannot be cast to int.")
            else:
                run = False
        return user_input