import logging

class logger():

    def logging(self):
        logger=logging.getLogger(__name__)

        fileHandler=logging.FileHandler('./logs/logfile.log')
        logger.setLevel(logging.DEBUG)
        formatter=logging.Formatter("%(asctime)s :%(levelname)s :(name)s :(messages)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)


        # logger.debug("Debug Log")
        # logger.info("Information Log")
        # logger.warning("Warning Log")
        # logger.error("Error Log")
        # logger.critical("Critical Log")
        return logger


