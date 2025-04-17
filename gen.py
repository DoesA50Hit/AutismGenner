import random
from lib import CLASSES

def generate_random_class():
    """
    Pick a random class from CLASSES and return its name
    """
    return random.choice(list(CLASSES.keys()))
