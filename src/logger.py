import logging

logging.basicConfig(filename='log.txt', level=logging.INFO, encoding="UTF-8",
                    format='%(asctime)s : %(levelname)s ^ %(message)s')


def log(msg):
    logging.info(msg)
    print('INFO: ' + msg)
