import enum
import logging
from dataclasses import dataclass
from elliptic_curves import EllipticCurve
from user_inputs import read_int

class CommandsEnum(enum.Enum):
    NULL_COMMAND = None
    QUIT = ["-q", "quit"]
    HELP = ["-h", "help"]
    CIPHER = ["-c", "cipher"]
    DECIPHER = ["-d", "decipher"]
    SHOW_CURVE = ["--show_curve", "show"]
    SET_CURVE = ["--set_curve", "set"]

@dataclass
class Command:
    command: CommandsEnum
    params: EllipticCurve | None


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
        for command_key in command_enum.value:
            if command_key in command_string:
                return command_enum
    return CommandsEnum.NULL_COMMAND

def get_command_params(command_enum: CommandsEnum) -> EllipticCurve | None:
    if command_enum == CommandsEnum.CIPHER:
        return None
    if command_enum == CommandsEnum.DECIPHER:
        return None
    if command_enum == CommandsEnum.SET_CURVE:
        logging.getLogger().info("Setting elliptic-curve in the form y^2 = x^3 + ax + b.")
        param_a = int(read_int("Parameter a: "))
        param_b = int(read_int("Parameter b: "))
        return EllipticCurve(param_a, param_b)
    return None