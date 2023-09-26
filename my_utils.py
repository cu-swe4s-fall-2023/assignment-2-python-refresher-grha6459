
def get_column(file_name, query_value, result_column, query_column=1):
    """
    :param file_name: The name of the file to be read from, in csv format, in current directory
    :param query_value: The value used to screen results in results_column
    :param result_column: The number (beginning with one) of the column to be returned, in part
    :param query_column: The number (beginning with one) of the column to be returned, in part, default value of one
    :return: a list of the numbers found in the result_column, if non-numerical values are found, will include NaN
             if issues are with file handelong encountered, function will  return None
    """
    # Following Variable (file) is only used as a test, open() is run again below
    file = None
    try:
        file = open(file_name)
    except FileNotFoundError:
        print("File not found. Is ", file_name, " the file you were looking for?")
        return None
    except PermissionError:
        print("Permission denied. Is ", file_name, " open in another program?")
        return None
    with open(file_name) as f:  # with will ensure that it closes
        # result_list is used to store values as they are collected, may convert to an array after it is
        # made
        result_list = []
        # line is the string that contains the entire line
        for line in f:
            # Strip removes newline and trailing whitespaces
            # Split separated the string by commas
            # items is a list data type
            items = line.strip().split(',')
            if items[query_column-1] == query_value:
                try:
                    new_value = int(float(items[result_column - 1]))
                    result_list.append(new_value)  # casting to float, then int
                except ValueError:  # if items[result_column - 1] can't be cast to a string
                    result_list.append(float('nan'))
    return result_list  # Has been updated to return list rather than np array
