#   Andrew Aberer | aaberer@colostate.edu
# https://www.cs.colostate.edu/~cs150b/labs/lab08
# -*- coding: utf-8 -*-
from math import *
import csv


def read_file(file):
    lst = []
    with open(file, 'r') as myfile:
        csv_reader = csv.reader(myfile)
        for row in csv_reader:
            print(row)
            lst.append(row)
    return lst


def get_city_info(data, city_name):
    counter = 0
    store_fc = 0
    for row in data:
        if row[0].lower() == 'Fort Collins'.lower():
            store_fc = counter
        if row[0].lower() == city_name.lower():
            return data[counter]
        counter += 1
    return data[store_fc]


def get_city_latitude(city_info):
    return city_info[1]


def get_city_longitude(city_info):
    return city_info[2]


def convert_degrees_to_decimals(str_value):
    degree_char = str_value.find('°')
    degree = float(str_value[0: degree_char])
    minutes_char = str_value.find('\'')
    minutes = float(str_value[degree_char+1: minutes_char])
    seconds_char = minute_char = str_value.find('\"')
    seconds = float(str_value[minutes_char+1: seconds_char])
    length = len(str_value)
    direction_char = str_value[seconds_char: length]
    direction = 0
    if direction_char == 'N' or direction_char == 'E':
        direction = 1
    if direction_char == 'S' or direction_char == 'W':
        direction = -1
    decimal_value = degree + (minutes / 60) + (seconds / 3600) * direction
    return decimal_value


def distance_between(data, city1, city2):
    city1_info = get_city_info(data, city1)
    city1_latitude = get_city_latitude(city1_info)
    city1_longitude = get_city_longitude(city1_info)
    city2_info = get_city_info(data, city2)
    city2_latitude = get_city_latitude(city2_info)
    city2_longitude = get_city_longitude(city2_info)

    lat1 = convert_degrees_to_decimals(city1_latitude)
    lon1 = convert_degrees_to_decimals(city1_longitude)
    lat2 = convert_degrees_to_decimals(city2_latitude)
    lon2 = convert_degrees_to_decimals(city2_longitude)

    # radius of the earth at 39 degrees latitude in miles - to use Kilometers: 6373
    EARTH_RADIUS = 3961
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = pow(sin(dlat/2), 2) + cos(radians(lat1)) * \
        cos(radians(lat2)) * pow(sin(dlon/2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return EARTH_RADIUS * c


def run_tests():
    data = read_file('cities.csv')
    print("TESTING", data)
    return True  # change to True before submitting for grading, and run the application!


if __name__ == '__main__':
    run_calc = run_tests()

    data = read_file('cities.csv')
    cont = 'y'
    while cont != 'n' and run_calc:
        city1 = input('Enter the first city: ')
        city2 = input('Enter the second city: ')
        dist = distance_between(data, city1, city2)
        print('The distance between {} and {} is {:.2f} miles!'.format(
            city1, city2, dist))
        cont = input('Run again (y/n)? ')[:1].lower()
