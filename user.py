import logging
import random
from elliptic_curves import EllipticCurve, CurvePoint
from ciphering import Cipherist, Decipherist, Public_key

class User():
    def __init__(self) -> None:
        self.curve = EllipticCurve(None)
        self.private_key = random.randint(1, self.curve.order -1)
        self.public_key = self.__initialize_public_key()
        self.cipherist = Cipherist(public_key = self.public_key, eliptic_curve = self.curve)
        self.decipherist = Decipherist(public_key = self.public_key, private_key = self.private_key, eliptic_curve = self.curve)
        self.current_coded_message = None
        
    def cipher_message(self, message: int):
        logging.getLogger().info("Your message is equivalent to the EC point: " + str(self.curve.points[message]))
        self.current_coded_message = self.cipherist(self.curve.points[message])
        logging.getLogger().info("Coded message [c1, c2]: " + ', '.join(str(x) for x in self.current_coded_message))
        
    def decipher_current_message(self) -> int:
        if self.current_coded_message == None:
            raise RuntimeError("You must first enter your message. Use -c command.")
        uncoded_message_EC = self.decipherist(coded_message = self.current_coded_message)
        logging.getLogger().info("Uncoded message in EC representation: " + str(uncoded_message_EC))
        uncoded_message = self.curve.points.index(uncoded_message_EC)
        logging.getLogger().info("Uncoded message: " + str(uncoded_message))
        return uncoded_message
    
    def get_public_key(self) -> Public_key:
        return self.public_key
    
    def __initialize_public_key(self) -> Public_key:
        P = self.curve.points[random.randint(1, self.curve.order -1)]
        Q = self.curve.multiply_point_by_integer(self.private_key, P)
        return Public_key(P, Q)
        
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