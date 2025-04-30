# Andrew Aberer | aaberer@colostate.edu
import csv
date_index = 0
temp_index = 2


def csv_reader(filename):
    file_list = []
    with open(filename) as text:
        csv_reader = csv.reader(text)
        for row in csv_reader:
            file_list.append(row)
        file_list.pop(0)
    return file_list


def client_input():
    filter = input('Please enter a filter: ')
    return filter


def average_temperature(weather, filter):
    lst = []
    counter = 0
    total_temp = 0
    for val in weather:
        if filter in val[date_index]:
            lst.append(val[temp_index])
            total_temp = total_temp + float(val[temp_index])
            counter = counter + 1
    if counter == 0:
        return 0
    return total_temp / counter


def maximum_temperature(weather, filter):
    max_lst = []
    for val in weather:
        if filter in val[date_index]:
            max_lst.append(float(val[temp_index]))
    return max(max_lst)


def minimum_temperature(weather, filter):
    min_lst = []
    for val in weather:
        if filter in val[date_index]:
            min_lst.append(float(val[temp_index]))
    return min(min_lst)


def run():
    call_file = ('Temperatures.csv')
    file = csv_reader(call_file)
    input_var = client_input()
    print(
        f'Average Temperature for {input_var}: {average_temperature(file, input_var):.2f}')
    print(
        f'Maximum Temperature for {input_var}: {maximum_temperature(file, input_var):.2f}')
    print(
        f'Minimum Temperature for {input_var}: {minimum_temperature(file, input_var):.2f}')


if __name__ == '__main__':
    run()
