# Logging
# Purpose: Record progress and problems...
# Levels: Notset, Debug, Info, Warning, Error, Critical
# Addition levels can be created but these five should generally be enough

#importing module
import logging
import math

print(dir(logging)) # This will output three different types of entries: 
                    # All CAPS = constants
                    # Uppercase first letter = classes
                    # Lowercase first letter = methods
# Create and configure logger 
LOG_FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(filename = "newfile.log", 
					format = LOG_FORMAT, 
					filemode='w') # The Default file mode is append
# Note that the default format for a log file is <(level):(logger name, i.e root):(log message)>

# Creating an object 
logger = logging.getLogger() # Naming loggers can create subtley issues
                             # Using a logger without a name is called a root logger
                             # This is a logger object without a name
print(logger.level) # Loggers will only write messages witha level greater than or equal to the set level

# Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) # This could have been done during the creation and configuration of the logger
# For example:
# logging.basicConfig(filename = "example.log", level = logging.DEBUG)

# Test messages 
# logger.notset("Find more info")               # Numerical value = 00
logger.debug("Harmless debug Message")          # Numerical value = 10
logger.info("Just an information")              # Numerical value = 20
logger.warning("Its a Warning")                 # Numerical value = 30
logger.error("Did you try to divide by zero")   # Numerical value = 40
logger.critical("Internet is down")             # Numerical value = 50

def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    # Compute the two roots
    root_1 = (-b + math.sqrt(disc)) / (2*a)
    root_2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger.debug("# Return the roots")
    return (root_1, root_2)
roots = quadratic_formula(1, 0, -4) # Change -4 to 1 to see the effects in the logger
print(roots)