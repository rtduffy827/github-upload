# How to setup python for command line use on windows

# Follow the steps below:
# Open Windows CMD.
# Type 'python -m pydoc'.
# Make sure to use the '-m' above to run pydoc as a script.
#
# ===== First use for the pydoc module. =====
# Use pydoc to look at the documentation for a class, module, or function.
# 
# Module example:
# To look at the documentation for the math module.
# Type 'python -m pydoc math'.
# In addition to a brief description of the module pydoc describes each function it contains.
#
# Class example:
# Look at the help text for a class such as tuple.
# Type 'python -m pydoc tuple'
#
# Function example:
# Look at the help text for a function such as pow.
# Type 'python -m pydoc pow'.
#
# To enter interactive mode do the following:
# Windows OS: Type 'py' in the windows CMD, or open python.exe (Note: location of this .exe will vary).
# Linux OS: Type 'python' in the linux terminal.
# Mac OS: Type 'python' in the macOS terminal (I have not verified this personally).
#
# The function pow could also be accessed in interactive mode with the help function.
# E.g. type 'help(pow)'
# Pydoc does not have to import a module to look at the help text.
# This is a small benefit over the help function, but otherwise equivalent.
#
# ===== Second use for the pydoc module. =====
# Use pydoc to search all modules for a certian keyword.
#
# For example,
# To search for the keyword ftp do the following:
# Type 'python -m pydoc -k ftp'
# Results may vary depending on the version of python installed or if additional libraries are installed.
# In this case two results were found. A class and its test class.
# Type 'python -m pydoc ftplib' (Assuming the same results were found).
#
# Another example,
# Does python contain any modules with the keyword sql?
# Type 'python -m pydoc -k sql'.
# Answer: Yes.
# Type 'python -m pydoc sqlite3' (sqlite3 is referred to as a package, which is a collection of modules).
#
# ===== Third use for the pydoc module. =====
# Use pydoc to start an HTTP server on the given port on the local machine.
# Type 'python -m pydoc -p 314'.
# Open the given URL, or type b and python will open a browser with that URL.
#
# This will bring the user to a documentaion homepage.
# The top section displays the builtin modules.
# Clicking on one of the modules will provide full details on the module.
# For example, click <cmath>.
#
# Click on the <Module Index> link at the top of the webpage to return to the homepage.
#
# It is recommended that the user browse the modules and pacakges to become familiar with what is available.
# E.g. click on the xml package.
#
# To view the documentation for a specific item, type it into the text box next to 'Get' and click 'Get'.
# Example, type 'pow' into the 'Get' text box.
#
# If the exact name of the item is not known then use the 'Search' text box instead.
# Example, type 'rpc' into the 'Search' text box (rpc = remote procedure call).
# A list of search results will appear.
# Clicking on a result will bring the user to the documentaion.
#
# Overall this is a faster way to browse, find, and search through the python documentation.
#
# To stop the documentation server.
# Return to the console and type 'q'.
#
# ===== Additional features of the pydoc module. =====
# Type 'python -m pydoc -b'.
# This will start the server on an available port and launch a browser for the user.
# A handy shortcut.
# Especially useful if the user has a large number of services running on a large number of ports.
# 
# Type 'python -m pydoc -w'
# This provides the ability to generate html files of the documentation.
#
# Below are the steps for a demonstration of this feature.
# Windows OS:
# Type 'mkdir pydoc_demo'.
# Type 'cd pydoc_demo'.
# Type 'python -m pydoc -w json'
# The name json is just used as an example.
# This name could be the name of a function, class, module, or pacakge.
# Type 'dir'.
# The user should see that the file json.thml was created.
# Type 'start json.html'.
# The above command will open the bowser for the user.
# This feature is especially useful if the user wants to host the python documentation for the user's code
# on a seperate server rather than the user's work station.
#
# Linux OS: (Not Completed)
# Mac OS: (Not Completed)