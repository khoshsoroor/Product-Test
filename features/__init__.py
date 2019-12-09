import yaml
import logging
from aloe import before, after, world
from datetime import datetime

REFERENCE_DATE = datetime.strptime('Jan 01 1970  12:00AM', '%b %d %Y %I:%M%p')
REFERENCE_DATE_DATE = REFERENCE_DATE.date()


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        for k, v in self.__dict__.items():
            if type(v) == dict:
                setattr(self, k, Struct(**v))


f = open('config.yml', 'rt')
config = Struct(**yaml.load(f.read(), Loader=yaml.FullLoader))


logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('test_ostadkar.txt', 'wt', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)


@before.each_step
def log(*args):
    logger.debug('Request: ' + str(args))
