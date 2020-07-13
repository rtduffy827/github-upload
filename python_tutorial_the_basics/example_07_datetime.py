import datetime
print(dir(datetime))
#print(help(datetime.date))

gvr = datetime.date(1956, 1, 31) # Birthday of Guido van Rossum (the creator of python)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(mill + dt)

# The default format for dates in python is YYYY-MM-DD, but this can be customized
# For example,
# The <Day-name, Month-name, Day-#, Year> format can be done in one of two ways

# Solution 1:
print(gvr.strftime("%A, %B %d, %Y")) # A slightly more antiquated solution

# Solution 2:
message = "GVR was born on {:%A, %B %d, %Y}." # A slightly more modern solution
print(message.format(gvr),"\n")

# SpaceX first launced a reused rocket March 30, 2017 22:27 UTC
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print("SpaceX launched its first reused rocket on this date", launch_date)
print("SpaceX launched its first reused rocket at this time", launch_time)
print("SpaceX launched its first reused rocket at this datetime", launch_datetime, "\n")

print("SpaceX launched its first reused rocket at this hour", launch_time.hour)
print("SpaceX launched its first reused rocket at this minute", launch_time.minute)
print("SpaceX launched its first reused rocket at this second", launch_time.second, "\n")

print("SpaceX launched its first reused rocket at this year", launch_datetime.year)
print("SpaceX launched its first reused rocket at this month", launch_datetime.month)
print("SpaceX launched its first reused rocket at this day", launch_datetime.day)
print("SpaceX launched its first reused rocket at this hour", launch_datetime.hour)
print("SpaceX launched its first reused rocket at this minute", launch_datetime.minute)
print("SpaceX launched its first reused rocket at this second", launch_datetime.second, "\n")

now = datetime.datetime.today()
print(now, "\n")

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)

print("moon_landing_datetime is of type", type(moon_landing_datetime))