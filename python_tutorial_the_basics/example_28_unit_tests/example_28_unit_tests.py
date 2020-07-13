# Unit tests typically go in a seperate file from the one they are testing.
import circles

# Test function
#radii = [2, 0, -3, 2 + 5j, True, "Radius"]
#message = "Area of circles with r = {radius} is {area}."

#for r in radii:
#    A = circles.circle_area(r)
#    print(message.format(radius=r, area=A))

# ===== Naming conventions for unit test programs =====
# Naming Convention 1   |   Naming Convention 2
# /circles.py           |   /circles.py
# /test_circles.py      |   /circles_test.py
# -----------------------------------------------------
# /circles.py           |   /circles.py
# /ellipses.py          |   /circles_test.py
# /hyperbolas.py        |   /ellipses.py
# /polygons.py          |   /ellipses_test.py
# /test_circles.py      |   /hyperbolas.py
# /test_ellipses.py     |   /hyperbolas_test.py
# /test_hyperbolas.py   |   /polygons.py
# /test_polygons.py     |   /polygons_test.py

# Naming Convention 1 will be used for the following examples
# After creating circles.py and test_circles.py,
# open the Python command shell.
# Type 'python -m unittest test_circles' (This is good for running a specific unit test).
# Type 'python -m unittest' (Python will run a process called test discovery to find tests and run them).

# There are many assert methods. It is recommended to look them up with the help method.
import unittest
print(help(unittest.TestCase.assertSetEqual))