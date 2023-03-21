import logging

if __name__ == "__main__":
    logging.getLogger(__name__)
    logging.basicConfig(format = '\n%(asctime)s %(module)s %(levelname)s: %(message)s', datefmt = '%I:%M:%S %p', level = logging.INFO)

    logging.getLogger().info("Hello from PyECC.")