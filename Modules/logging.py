import logging
import random

logger = logging.getLogger("script") 

logging.basicConfig(levelname=logging.DEBUG,format="%(asctime)s:%(name)s:%(message)s",filename="script.log") 

def generate_random_number():
  return random.randint(1,100) 

exe = generate_random_number()

logger.debug(exe) 
