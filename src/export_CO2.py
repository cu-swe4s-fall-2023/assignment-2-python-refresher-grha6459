import my_utils
import argparse
import sys
# Following is redundant with my_utils, but throws error otherwise
import numpy as np


# The purpose of this file is the use of my_utils.py to extract multiple
# columns and export the result as a csv
def main():
    # Initializing a parser object, which contains arguments with specified
    # properties
    parser = argparse.ArgumentParser(
                description='This is the preferred way to parse command line '
                            'arguments.',
                prog='export_CO2.py')

    parser.add_argument('--country',
                        type=str,
                        help='The name of the country used as query',
                        required=True)

    # Following has default of one, a default is also supplied by get_column,
    # but this prevents None from being passed
    # to my_utils if this argument isn't included in the command line.
    parser.add_argument('--country_column',  # This is the one argument with a
                        # default
                        type=int,
                        help='Number (not the index, first column is one) of '
                             'column query value resides in',
                        required=False,
                        default=1)

    parser.add_argument('--file_name',
                        type=str,
                        help='filename to read from',
                        required=True)

    parser.add_argument('--column_numbers', type=int, nargs='+',
                        help='Numbers (not the indices, first column is one) '
                             'to be added to csv file. Pass as integers '
                             'separated by spaces', required=True)
    # nargs+ gives at least one argument, possibly more

    args = parser.parse_args()
    # Following uses the arguments returned by the parser for a function call
    # def get_column(file_name, query_value, result_column, query_column=1)
    # Files for individual countries are indexed by year
    index_column_number = 2
    years = my_utils.get_column(args.file_name, args.country,
                                index_column_number,
                                query_column=args.country_column)
    # Following iterates the column numbers to stack arrays
    combined_array = years  # At this point combined array is 1D
    for i in args.column_numbers:
        # New array created using column number where we used fires_column
        # before
        new_array = my_utils.get_column(args.file_name, args.country,
                                        i,
                                        query_column=args.country_column)
        # Add new column to combined_array
        combined_array = np.column_stack((combined_array, new_array))

    # Export to csv
    csv_file = args.country+"_processed.csv"

    if combined_array.size == 0:
        sys.exit(1)
        # Exit code updated to reflect that an error was
        # encountered and no values read
    else:
        # Export the combined array to a CSV file
        np.savetxt(csv_file, combined_array, delimiter=',')


# Main function added
if __name__ == "__main__":
    main()
