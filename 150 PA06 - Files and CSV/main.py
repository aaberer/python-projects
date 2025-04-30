##
# Files and CSV lab for CS 150B.
# https://www.cs.colostate.edu/~cs150b/labs/lab07
# In this lab, you will get practice opening files and using the data in those files
##
# @Andrew Aberer
# aaberer@colostate.edu
# @version 202102

import csv


# Step 1
def file_addition(filename):
    with open(filename) as text:
        file = text.readlines()
        line1 = int(file[0])
        line2 = int(file[1])
    return line1 + line2

# Step 2


def line_counter(filename):
    with open(filename) as t:
        file = t.readlines()
        total = len(file)
        return total


# Step 3
def csv_data(filename):
    count = 0
    max_row_length = 0
    with open(filename, 'r') as myfile:
        csv_reader = csv.reader(myfile)
        for row in csv_reader:
            print(row)
            max_row_length = len(row)
            count += 1
    return count, max_row_length  # returns a tuple of the two values


# Step 4
def get_filtered_CSV(filename, filter_by):
    lst = []
    counter = 0
    with open(filename, 'r') as myfile:
        # remember import csv at the top of the file
        csv_reader = csv.reader(myfile)
        for row in csv_reader:
            print(row)
            if filter_by == row[0]:
                lst.append(row)
    return lst


# Step 5
def find_flight(filename, airlines, city, earliest, latest):
    print(get_filtered_CSV(filename, airlines))
    with open(filename, 'r') as myfile:
        csv_reader = csv.reader(myfile)
        for row in csv_reader:
            if row[1] == city and latest > row[2] >= earliest:
                return row


# Add your own tests to this method
def run():
    print(file_addition("num.txt"))
    print(line_counter("harryPotter.txt"))
    print(csv_data("myfile.csv"))
    print(get_filtered_CSV("Airport.csv", "United"))
    print(find_flight("Airport.csv", "United", "Portland", "0000", "2400"))


if __name__ == '__main__':
    print()
    run()
