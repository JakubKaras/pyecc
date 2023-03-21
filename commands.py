import enum
import logging
from elliptic_curves import EllipticCurve
from user import User


class CommandsEnum(enum.Enum):
    NULL_COMMAND = None
    QUIT = ["-q", "quit", "Close interface"]
    HELP = ["-h", "help", "Print help to console."]
    CIPHER = ["-c", "cipher", "Cipher message."]
    DECIPHER = ["-d", "decipher", "Decipher message."]
    SHOW_CURVE = ["--show_curve", "show", "Plot current elliptic curve's points."]
    SET_CURVE = ["--set_curve", "set", "Set ciphering elliptic curve."]


class Command:
    def __init__(self, command: CommandsEnum, params: list | None):
        self.command = command
        self.params = params
    
    def process(self, user: User):
        if self.command == CommandsEnum.NULL_COMMAND:
            logging.getLogger().info(Command._help_message())
        if self.command == CommandsEnum.SET_CURVE:
            user.curve = EllipticCurve(self.params)
        if self.command == CommandsEnum.HELP:
            logging.getLogger().info(Command._help_message())

    @staticmethod
    def _help_message() -> str:
        help_message = "The following commands are available:\nCommand:                    Function:\n"
        for command in CommandsEnum:
            if command.value is not None:
                help_message = help_message + f"  {command.value[0] + ', ':<14}{command.value[1]:<14}{command.value[2]}\n"
        return help_message


def get_command() -> Command:
    user_input = input("Awaiting command: ")
    command = get_command_enum(user_input)
    params = get_command_params(command)
    return Command(command, params)

def get_command_enum(command_string: str) -> CommandsEnum:
    command_string = command_string.lower()
    for command_enum in CommandsEnum:
        if command_enum is CommandsEnum.NULL_COMMAND:
            continue
        for command_key in command_enum.value[:2]:
            if command_key in command_string:
                return command_enum
    return CommandsEnum.NULL_COMMAND

def get_command_params(command_enum: CommandsEnum) -> list | None:
    if command_enum == CommandsEnum.CIPHER:
        return None
    if command_enum == CommandsEnum.DECIPHER:
        return None
    if command_enum == CommandsEnum.SET_CURVE:
        logging.getLogger().info("Setting elliptic-curve in the form y^2 = x^3 + ax + b.")
        param_a = int(User.read_int("Parameter a: "))
        param_b = int(User.read_int("Parameter b: "))
        return [param_a, param_b]
    return None