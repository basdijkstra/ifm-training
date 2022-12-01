import numpy


# Bad example, as this single function is responsible for many different things
def list_operations(list_of_numbers):
    print(f'Average value: {numpy.average(list_of_numbers)}')
    print(f'Mean value: {numpy.mean(list_of_numbers)}')
    print(f'Minimum value: {numpy.min(list_of_numbers)}')
    print(f'Maximum value: {numpy.max(list_of_numbers)}')


list_operations([1, 2, 3, 4, 5])
