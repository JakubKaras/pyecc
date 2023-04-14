import logging
from commands import CommandsEnum, Command
from user import User

if __name__ == "__main__":
    logging.getLogger(__name__)
    logging.basicConfig(format = '\n%(asctime)s %(module)s: %(message)s', datefmt = '%I:%M:%S %p', level = logging.INFO)

    logging.getLogger().info("Hello from PyECC.\nFor list of commands type -h or help.")
    user = User()
    while True:
        try:
            command = Command(user)
            if command.command == CommandsEnum.QUIT:
                break
            command.process()
        except Exception as e:
            logging.getLogger().exception(f"An error occured: {e}")