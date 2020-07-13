# CSV = Comma Separated Values
# Databases often used to store large amounts of data
# Spreadsheets often used to store small amounts of data
# CSV still have a place
# Python has a CSV module
# Two ways to store the data: without the csv module and with the csv module
# Method 1: without the csv module
# Part A - Methods of data extraction from a csv file
path = "google_stock_data.csv"
file = open(path)
lines = [line for line in file] # a list comprehension

print(lines[0])
print(lines[1])
print(lines[0].strip())
print(lines[0].strip().split(','))

file.close()

# Part B - Getting dataset.csv into a desired form
file = open(path)

dataset = [line.strip().split(',') for line in file]
print(dataset[0])
print(dataset[1])

file.close()

# The issue with method 1 is that some datasets (e.g. books or movies)
# could have titles that contain commas. Also all data in the dataset
# (e.g. dates or times) will be stored as a string. This will require
# a lot more work on the part of the programmer to tailor each dataset
# extraction method to each dataset. The solution is the csv module.

# Method 2: with the csv module
# Part A - using the csv module
import csv
print("\n", dir(csv), "\n")
file = open(path, newline='') # Notice the newline keyword argument.
                              # This step ensures that this instruction
                              # will work on all systems. Different systems
                              # use differnt methods to indicate an end of a string.
reader = csv.reader(file)

header = next(reader) # The first line is the header
data = [row for row in reader] # Read the remaining data

print(header)
print(data[0])

file.close()

# The above code is longer than method 1, but more robust and will handel more exceptions.
# However the approach above still extracts all data into a string type.

from datetime import datetime # From the datetime class import the datetime module

file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # The first line is the header
data = []
for row in reader:
    # row = [Date, Open, High, Low, Close, Volume, Adj. Close]
    # type(Date) = datetime
    # type(Open), type(High), type(Low), type(Close), type(Adj. Close) = float
    # type(Volume) = int
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1]) # 'open' is a builtin function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

print(data[0])

# Stock Return = % change in price
# Compute and store daily stock returns
returns_path = "google_returns.csv"
fp = open(returns_path, 'w')
writer = csv.writer(fp)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1): # for the first day there is not a previouses day's data to compare too
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    # writer.writerow([todays_date, daily_return]) <- not an easily readable format, but gives the correct information
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])

fp.close()
file.close()