import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

#1 DONE
def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    
#2 DONE
def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    converted_date = date.strftime('%A %d %B %Y')
    return converted_date
    
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    
#3 DONE
def convert_f_to_c(temp_in_farenheit): 
    celsius = round((float(temp_in_farenheit) - 32) * (5/9),1)
    return celsius

    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

#4 DONE
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

#5 DONE
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

#6 DONE
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


#7 DONE
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

#8 DONE
def generate_summary(weather_data):
    
    day_value = len(weather_data)

    dates = [value[0] for value in weather_data]
    min_temps = [value[1] for value in weather_data]
    max_temps = [value[2] for value in weather_data]

    min_temp_tupal = find_min(min_temps)
    min_temp = format_temperature(convert_f_to_c(min_temp_tupal[0]))
    min_date_position = min_temp_tupal[1]
    min_date = convert_date(dates[min_date_position])
    
    max_temp_tupal = find_max(max_temps)
    max_temp = format_temperature(convert_f_to_c(max_temp_tupal[0]))
    max_date_position = max_temp_tupal[1]
    max_date = convert_date(dates[max_date_position])

    low_mean = format_temperature(convert_f_to_c(calculate_mean(min_temps)))
    high_mean = format_temperature(convert_f_to_c(calculate_mean(max_temps)))

    return f"{day_value} Day Overview\n  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}, and will occur on {max_date}.\n  The average low this week is {low_mean}.\n  The average high this week is {high_mean}.\n"

    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """


#9 DONE
def generate_daily_summary(weather_data):
    summary = ""

    for row in weather_data:
        day_value = convert_date(row[0])
        min_temp = format_temperature(convert_f_to_c(row[1]))
        max_temp = format_temperature(convert_f_to_c(row[2]))
        summary += (f"---- {day_value} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n")
    
    return summary

    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """