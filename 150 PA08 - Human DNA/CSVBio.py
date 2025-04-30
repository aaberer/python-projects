# dna_stats()
# params: a list of data from csv
# This function takes in a list of ints that represent DNA lengths. It will return
# a formatted string that has the shortest, longest, and average lengths
# returns: formatted string
# TODO Student (you will need to create the function from scratch)
# Andrew Aberer | aaberer@colostate.edu
# https://www.cs.colostate.edu/~cs150b/labs/lab09
import csv


def file_int_list(file):
    lst = []
    with open(file, 'r') as text:
        for row in text:
            num = int(row)
            lst.append(num)
    # open the file, read every line, convert the list of strings to list of ints (use lst)
    return lst


def dna_stats(lst):
    minimum = min(lst)
    maximum = max(lst)
    length = len(lst)
    total = sum(lst)
    avg = total / length
    final_str = (
        f'Shortest DNA Length: {minimum} \nLongest DNA Length: {maximum} \nAverage DNA Length: {avg:.2f}')
    return final_str


def main():
    count = 0
    fin = []
    dna_files = ['HumanGeneLengths1.txt', 'HumanGeneLengths2.txt',
                 'HumanGeneLengths3.txt', 'HumanGeneLengths4.txt']

    while count < 4:
        fin = file_int_list(dna_files[count])
        print(dna_files[count])
        print(dna_stats(fin))
        count += 1


if __name__ == '__main__':
    main()
