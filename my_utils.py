import numpy as np
#not sure where above line should be
def get_column(file_name, query_value, result_column,query_column=1):
    # Nore that column numbers are not indeceis, they are natural numbers
    # Named variable defaults are set as above, defualt here is 1
    with open(file_name) as f:  # with will ensure that it closes
        #result_list is used to store vaues as they are collected, may convert to an array after it is made
        result_list = []
        # line is the string that contains the entire line
        for line in f:
            # Strip removes newline and trailing whitespaces
            # Split separated the string by commas
            #items is a list data type
            items = line.strip().split(',')
            if items[query_column-1] == query_value:
                result_list.append(items[result_column-1])
    return np.array(result_list)
