# How to use python to send 'get' requests to web servers
# and then parse the response.
# ==================================
# URL = Uniform Resource Locator
# Example: https://en.wikipedia.org/wiki/URL?key=value&life=42#History
# Protocol: http, https, ftp, ...   |
# Host: en.wikipedia.org            |
# Port: http=80, https=443          | Sometimes see <hostname>:<port_number> if not then default.
# Path: wiki/URL                    |
# Querystring: key=value&life=42    | A collection of key/value pairs seperated by &
# Fragment: History                 | A '#' followed by a string. Used to jump to a section in a web page.

# Python 3 comes witha a package that simplifies the task of building, loading, and parsing URLs.
# The 'urllib' package.
# This package comes with five modules.
# - requestl: open URLs
# - response: (used internally)
# - error: request exceptions
# - parse: useful URL functions
# - robotparser: robots.txt files

# This program will focus on the request module.
import urllib
print(dir(urllib), "\n")

from urllib import request
print(dir(request), "\n")

resp = request.urlopen("https://www.wikipedia.org")

print(type(resp))

# HTTP Status Codes
# 200: OK
#
# 400: Bad Request
# 403: Forbidden
# 404: Not Found
# ⋮
print(resp.code)
print(resp.length) # The size in bytes.
print(resp.peek())

data = resp.read()
print(type(data))
print(len(data))

html = data.decode("UTF-8")
print(type(html))
print(120*"=")
print(html)

print(resp.read()) # Python closes the response after the first read. So nothing happens here.

# Google doesn't want competitors to use their search.
# resp = request.urlopen("https://www.google.com/search?q=socratica")

# Load the youtube video "Black Holes" by socratica.
# https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s
# v = video id
# t = start time
# One way to construct a QueruString
qs = "v=" + "EuC-yVzHhMI" + "&" + "t=" + "5m56s"

# An easier way.
from urllib import parse
print(dir(parse), "\n")

params = {"v": "EuC-yVzHhMI", "t=": "5m56s"}
querystring = parse.urlencode(params)
print(querystring)

url = "https://www.youtube.com/watch" + "?" + querystring
resp = request.urlopen(url)
print(resp.isclosed())
print(resp.code)

html = resp.read().decode("utf-8")
print(html[:500])