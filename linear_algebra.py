import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BadData(Exception):
    def __init__(self, a):
        super().__init__(a)

def check_vector(x):
    if type(x) is list and all([type(b) is float or type(b) is int for b in x]):
        return True
    else:
        return False

def dot(x, y):
    if check_vector(x) and check_vector(y) and len(x) == len(y):
        return sum([a*b for a, b in zip(x,y)])
    else:
        #logger.error("dot is for vectors")
        raise BadData("dot is for vectors")

