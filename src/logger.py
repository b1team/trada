import logging

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
formatter = ("[%(asctime)s][%(levelname)s] - %(message)s")
stream_handler.setFormatter(logging.Formatter(formatter))

logger = logging.getLogger("ChatAPP")
logger.handlers = []
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)
