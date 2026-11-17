import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    numbers = []
    with open(filepath, 'r') as infile:
        count = 0
        for line_number, line in enumerate (infile, start=0):
            count += 1
            try:
               num = line.split("\t")[column]
            except IndexError:
                raise IndexError(f"Exiting: There is no valid 'list index' in column {column} in line {line_number} in file: {filepath}")
            try:
                num = float(num)
            except ValueError:
                continue
            if math.isnan(num):
                continue
            numbers.append(num)
    if len(numbers) == 0:
        raise ValueError(f"There were no valid number(s) in column {column} in file: {filepath}")
    return numbers, count, len(numbers)

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
    std_dev = math.sqrt(variance)
    return std_dev

def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    sorted_numbers = sorted(number)
    n = len(sorted_numbers)
    if n % 2 == 1:
        middle_index = n // 2
        return sorted_numbers[middle_index]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
        return median

def run_analysis(filepath:str, column:int):
    print(filepath)
    print(f"Column: {column}\n")

    try:
        numbers, count ,valid_num = load_data("files/data_file.txt", 3)
        print(f"Count = {count:.3f}")
        print(f"ValidNum = {valid_num:.3f}")
        print(f"Average = {calculate_average(numbers):.3f}")
        maximum , minimum = get_max_and_min(numbers)
        print(f"Maximum = {maximum:.3f}")
        print(f"Minimum = {minimum:.3f}")
        print(f"Variance = {calculate_variance(numbers):.3f}")
        print(f"Std Dev = {calculate_std_dev(numbers):.3f}")
        print(f"Median = {calculate_median(numbers):.3f}")
    except ValueError as error:
        print(f"Error: {error}")
    except IndexError as error:
        print(error)
    print("-" * 80)

if __name__ == "__main__":
    run_analysis("files/data_file.txt", 3)
    run_analysis("files/data_file2.txt", 3)
    run_analysis("files/data_file3.txt", 3)
    run_analysis("files/data_file3.txt", 10)
    run_analysis("files/data_file3.txt", 1)
    run_analysis("files/data_file2.txt", 4)
    


