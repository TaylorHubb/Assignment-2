import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    numbers = []
    with open(filepath, 'r') as infile:
        for line in infile:
            try:
               num = line.split("\t")[column]
            except IndexError:
                sys.exit()
            try:
                num = float(num)
            except ValueError:
                continue
            numbers.append(num)
        return numbers, len(numbers)
    

def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    average = sum(numbers) / len(numbers)
    return average

def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    return (max(numbers), min(numbers))

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    average = calculate_average(numbers)
    differences = []
    for num in numbers:
        difference = num - average
        squared_difference = difference ** 2
        differences.append(squared_difference)
    variance = (1 / (len(numbers) - 1)) * sum(differences)
    return variance

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    variance = calculate_variance(numbers)
    std_dev = math.sprt(variance)
    return std_dev

def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    pass


