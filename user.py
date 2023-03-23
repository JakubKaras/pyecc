import logging
from elliptic_curves import EllipticCurve, CurvePoint
from cipher import Cipherist, Decipherist, Public_key

class User():
    def __init__(self) -> None:
        self.curve = EllipticCurve(None)
        private_key = 7
        public_key = Public_key(CurvePoint(0,3), self.curve.multiply_poit_by_integer(private_key, CurvePoint(0,3)))
        self.cipherist = Cipherist(public_key = public_key, eliptic_curve = self.curve)
        self.decipherist = Decipherist(public_key = public_key, private_key = private_key, eliptic_curve = self.curve)
        
    def cipher_message(self, message: int):
        print("Your message is equivalent to the EC point: ", self.curve.points[message])
        self.current_coded_message = self.cipherist(self.curve.points[message])
        print("Coded message [c1, c2]: ", self.current_coded_message)
        
    def decipher_current_message(self) -> CurvePoint:
        if self.current_coded_message == None:
            raise RuntimeError("You must first enter your message. Use -c command.")
        uncoded_message = self.decipherist(coded_message = self.current_coded_message)
        print("Uncoded message: ", uncoded_message)
        return uncoded_message
        
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