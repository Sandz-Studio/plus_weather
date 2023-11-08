import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# DONE
def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

# DONE
def convert_date(iso_string):
    datetime.strftime(iso_string)

    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass

# DONE
def convert_f_to_c(temp_in_farenheit): 
    celsius = round((float(temp_in_farenheit) - 32) * (5/9),1)
    return celsius

    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

# DONE
def calculate_mean(weather_data):
    list_of_int = []

    for item in weather_data:
        item = float(item)
        list_of_int.append(item)
    
    sum_of_nums = sum(list_of_int)
    len_of_nums = len(list_of_int)
    return round(float(sum_of_nums/len_of_nums),5)
    
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass

# DONE
def load_data_from_csv(csv_file):

    weather_data = []

    with open(csv_file, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for line in reader:
            if len(line) != 0:
                weather_data.append([line[0], int(line[1]), int(line[2])])

    return weather_data

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    pass

# DONE
def find_min(weather_data): 
    if not weather_data:
        return ()


    for line in weather_data:
        min_weather_data = min(weather_data)
        min_index_num = [index for index, item in enumerate(weather_data) if item == min_weather_data]

        return float(min_weather_data), min_index_num[-1]


    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass

# DONE
def find_max(weather_data):
    if not weather_data:
        return ()

    for line in weather_data:
        max_weather_data = max(weather_data)
        max_index_num = [index for index, item in enumerate(weather_data) if item == max_weather_data]

        return float(max_weather_data), max_index_num[-1]

    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
