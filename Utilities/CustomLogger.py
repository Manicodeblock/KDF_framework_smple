import logging
class LogGen:
    @staticmethod
    def loggen():


        logging.basicConfig(filename="/Users/ticvictech/PycharmProjects/project_kdt/Logs/Logmessage.csv",format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%y %I:%M:%S %P')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

