import logging
from commands import get_command, CommandsEnum

if __name__ == "__main__":
    logging.getLogger(__name__)
    logging.basicConfig(format = '\n%(asctime)s %(module)s %(levelname)s: %(message)s', datefmt = '%I:%M:%S %p', level = logging.INFO)

    logging.getLogger().info("Hello from PyECC.")
    while True:
        try:
            command = get_command()
            logging.getLogger().info(f"Command: {command}")
            if command.command == CommandsEnum.QUIT:
                break
        except Exception as e:
            logging.getLogger().exception(f"An error occured: {e}")