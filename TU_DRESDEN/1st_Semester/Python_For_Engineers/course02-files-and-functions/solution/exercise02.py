import sys  # für sys.exit benötigt


def get_data(filename):


    # would work but not recommended:
    # myfile = open(filename, 'r')
    # ...
    # myfile.close()

    # better: context manager notation so you don't forget myfile.close()
    with open(filename, 'r') as myfile:
        list_of_lines = myfile.readlines()

    # list_of_lines is now a list of str objects
    # -> Conversion to list of float objects

    # create an empty list
    values = []

    # iterate over the list of all lines
    for myline in list_of_lines:
        # for each line: convert the str object to float and append it to values
        values.append(float(myline))

    return values


def calc_mean(data):

    # Example safety checks
    assert isinstance(data, (list, tuple))
    assert len(data) > 0

    # calc the sum of all values
    # (we will learn more elegant ways in the future)
    res = 0
    for d in data:
        res += d

    avg = res / len(data)

    return avg


def print_result(avg, filename):

    print(f"The average of all numbers from the file {filename} is {avg}.")


def ask_filename(fallback_name="data1.txt"):
    """
    This function asks for a file name to be entered.
    If an empty string is entered by the user, a fallback_name will be used.

    :param fallback_name:  str; defaults to "data1.txt"
    """

    userinput = input("Please enter the name of the file to be processed: ")

    if userinput == "":
        userinput = fallback_name

    return userinput


# Up to here we only defined functions .
# So that the program does something, the functions must now be called.

fname = ask_filename()  # usage of the default value for fallback_name

# Optional error handling (Taks 3):
try:
    xx = get_data(fname)
except IOError as err:
    print("Invalid file name. Maybe there is a typo ore the working directory is not correct?")
    print("Exiting program.")
    exit(1) # this results in a nonzero return code (also called "exit code") of the program
    # which typically indicates runtime errors to the operating system


mean = calc_mean(xx)
print_result(mean, fname)
