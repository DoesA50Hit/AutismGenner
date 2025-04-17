import random
from lib import CLASSES, WORDS

def generate_random_class():
  """
  Pick a random class and return it
  """
  char_class = random.choice(list(CLASSES.keys()))
  return char_class

