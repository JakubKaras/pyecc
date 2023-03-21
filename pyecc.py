import logging
from commands import get_command, CommandsEnum
from user import User

if __name__ == "__main__":
    logging.getLogger(__name__)
    logging.basicConfig(format = '\n%(asctime)s %(module)s %(levelname)s: %(message)s', datefmt = '%I:%M:%S %p', level = logging.INFO)

    logging.getLogger().info("Hello from PyECC.")
    user = User()
    while True:
        try:
            command = get_command()
            logging.getLogger().info(f"Command: {command}")
            if command.command == CommandsEnum.QUIT:
                break
            command.process(user)
        except Exception as e:
            logging.getLogger().exception(f"An error occured: {e}")