import logging

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