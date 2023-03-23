import enum
import logging
from elliptic_curves import EllipticCurve, CurvePoint
from user import User


class CommandsEnum(enum.Enum):
    NULL_COMMAND = None
    QUIT = ["-q", "quit", "Close interface"]
    HELP = ["-h", "help", "Print help to console."]
    CIPHER = ["-c", "cipher", "Cipher message."]
    DECIPHER = ["-d", "decipher", "Decipher message."]
    SHOW_CURVE = ["--show_curve", "show", "Plot current elliptic curve's points."]
    SET_CURVE = ["--set_curve", "set", "Set ciphering elliptic curve."]
    SUMS = ["--sum_table", "sums", "Show table of sums of curve's points."]
    PRINT_POINTS = ["--print_points", "print", "Show all points of the curve."]


class Command:
    def __init__(self):
        user_input = input("Awaiting command: ")
        self.command = Command._get_command_enum(user_input)
        self.params = Command._get_command_params(self.command)
    
    def process(self, user: User):
        if self.command == CommandsEnum.NULL_COMMAND:
            logging.getLogger().info("The command was not recognized.")
        if self.command == CommandsEnum.SET_CURVE:
            user.curve = EllipticCurve(self.params)
        if self.command == CommandsEnum.HELP:
            logging.getLogger().info(Command._help_message())
        if self.command == CommandsEnum.SHOW_CURVE:
            logging.getLogger().info("Close the figure to continue.")
            user.curve.plot()
        if self.command == CommandsEnum.SUMS:
            user.curve.print_sum_table()
        if self.command == CommandsEnum.PRINT_POINTS:
            user.curve.print_points()
        if self.command == CommandsEnum.CIPHER:
            user.cipher_message(self.params)
        if self.command == CommandsEnum.DECIPHER:
            user.decipher_current_message()    
            

    @staticmethod
    def _help_message() -> str:
        help_message = "The following commands are available:\nCommand:                    Function:\n"
        for command in CommandsEnum:
            if command.value is not None:
                help_message = help_message + f"  {command.value[0] + ', ':<14}{command.value[1]:<14}{command.value[2]}\n"
        return help_message

    @staticmethod
    def _get_command_enum(command_string: str) -> CommandsEnum:
        command_string = command_string.lower()
        for command_enum in CommandsEnum:
            if command_enum is CommandsEnum.NULL_COMMAND:
                continue
            for command_key in command_enum.value[:2]:
                if command_key in command_string:
                    return command_enum
        return CommandsEnum.NULL_COMMAND

    @staticmethod
    def _get_command_params(command_enum: CommandsEnum) -> list | None:
        if command_enum == CommandsEnum.CIPHER:
            logging.getLogger().info("Type message you want to coded. Message can be an arbitrary number in the range 0 - 134.")
            return int(User.read_int("Messege: "))
        # if command_enum == CommandsEnum.DECIPHER:
        #     raise NotImplementedError("Deciphering is not implemented yet.")
        if command_enum == CommandsEnum.SET_CURVE:
            logging.getLogger().info("Setting elliptic-curve in the form y^2 = x^3 + ax + b.")
            param_a = int(User.read_int("Parameter a: "))
            param_b = int(User.read_int("Parameter b: "))
            return [param_a, param_b]
        return None