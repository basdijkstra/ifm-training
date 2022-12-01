import numpy

# Better example, as every function now has its own, atomic responsibility
def print_average(list_to_average):
    print(f'Average value: {numpy.average(list_to_average)}')

def print_mean(list_to_mean):
    print(f'Mean value: {numpy.average(list_to_mean)}')

def print_minimum(list_to_minimum):
    print(f'Minimum value: {numpy.average(list_to_minimum)}')

def print_maximum(list_to_maximum):
    print(f'Maximum value: {numpy.average(list_to_maximum)}')

def list_operations(list_of_numbers):
    print_average(list_of_numbers)
    print_mean(list_of_numbers)
    print_minimum(list_of_numbers)
    print_maximum(list_of_numbers)

list_operations([1, 2, 3, 4, 5])
