import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(number_array, direction = "ascending"):
    """

    :param number_array: list with numeric array
    :param directions: string indicating sorting direction:ascending, descending
    :return: arraY
    """

    n = len(number_array)
    for i in range(n):
        min_max_i = i
        for num_ind in range(i+1, n):
            if direction == "ascending":
                if number_array[num_ind] < number_array[min_max_i]:
                    min_max_i = num_ind
            elif direction == "descending":
                if number_array[num_ind] > number_array[min_max_i]:
                    min_max_i = num_ind

        number_array[i], number_array[min_max_i] = number_array[min_max_i], number_array[i]

    return number_array

def bubble_sort(number_array):
    """

    :param number_array:
    :return:
    """
    n = len(number_array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if number_array[j] > number_array[j + 1]:
                number_array[j], number_array[j + 1] = number_array[j + 1], number_array[j]

    return number_array

def insertion_sort(number_array):
    n = len(number_array)
    for i in range(1, n):
        krokodilo = number_array[i]
        j = i - 1
        while j == 0 and number_array[j] > krokodilo:
            number_array[j + 1] = number_array[j]
            j = j - 1
        number_array[j + 1] = krokodilo

    return number_array



def main():
    data = read_data("numbers.csv")
    print(data)

    print(selection_sort(data["series_1"]))

    print(bubble_sort(data["series_2"]))

    print(insertion_sort(data["series_3"]))

if __name__ == '__main__':
    main()
