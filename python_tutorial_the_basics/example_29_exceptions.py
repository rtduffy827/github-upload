# There are many built-in exception objects built into Python.
# Exception Object:
# - Description
# - Traceback

# ===== Common Exceptions Examples =====
# Example 1 - SyntaxError:
# for i in range(5)
#     print("Hello, world!")

# Example 2 - ZeroDivisionError:
# print(1/0)

# Example 3 - FileNotFoundError:
# with open("x_files.txt") as xf:
#     the_truth = xf.read()
# print(the_truth)

# Example 4 - TypeError:
# print(1 + 2 + "three")

# Example 5 - ValueError:
# import math
#
# print(math.sqrt(-1)) # For complex numbers, use 'cmath' module

# Use the builtin exceptions whenever possible.
# If necessary, create a new exception by sub-classing the exception class.

# ===== The General Format for Exception Clauses =====
try:
    # Runs first.
    # <code>
    pass # Replace with actual code.
except: # Can have more than one exception clause if necessary.
    # Runs if exception occurs in try block.
    # <code>
    pass # Replace with actual code.
else:
    # Executes if try block *succeeds*.
    # <code>
    pass # Replace with actual code.
finally:
    # This code *always* executes.
    # <code>
    pass # Replace with actual code.

# Objective:
# - Write function that reads binary file and returns data
# - Measure time required

import logging
import time
# Create logger
logging.basicConfig(filename = "problems.Log", 
                    level = logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required."""
    start_time = time.time()
    try:
        f = open(path)
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file=path, time=dt))

data = read_file_timed("movie_1.txt")
data = read_file_timed("audio_file.wav") # 45 MB file