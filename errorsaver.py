# Save errors separately in a file instead of poping all in console 
import logging

logger = logging.getLogger(__name__) 
logger.setLevel(logging.INFO)
file = logging.FileHandler('logs.log') 
formatter = logging.Formatter('%(name)s:%(message)s:%(levelname)s') 
file.setFormatter(formatter)

logger.addHandler(file)

# ValueError case

number = input("Give a number: ")
try:
  number = int(number)
except Exception as err:
  logger.exception(err)
else:
  number = int(number)
  
#ZeroDivisionError case
new_number = 10
next_number = input("Give a number: ") 

try:
  new_number = new_number / int(next_number)
except ValueError as val:
  logger.exception(val)
except ZeroDivisionError as zerr:
  logger.exception(zerr)
