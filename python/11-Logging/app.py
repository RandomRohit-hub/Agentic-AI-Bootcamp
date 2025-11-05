import logging

# Configure both file and console logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log', mode='w'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("arithmetic_app")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def sub(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def mult(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def div(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is not allowed!")
        return None



add(10, 5)
sub(10, 5)
mult(10, 5)
div(10, 5)
div(10, 0)
