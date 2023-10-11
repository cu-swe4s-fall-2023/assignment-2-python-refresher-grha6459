import my_utils
import argparse
import sys


def main():
    # Initializing a parser object, which contains arguments with specified
    # properties
    parser = argparse.ArgumentParser(
                description='This is the preferred way to parse command line '
                            'arguments.',
                prog='print_fires.py')

    parser.add_argument('--country',
                        type=str,
                        help='The name of the country used as query',
                        required=True)

    # Following has default of one, a default is also supplied by get_column,
    # but this prevents None from being passed
    # to my_utils if this argument isn't included in the command line.
    parser.add_argument('--country_column',  # This is the one argument with a
                        # default, default is built into my_utils
                        type=int,
                        help='Number (not the index, first column is one) of '
                             'column query value resides in',
                        required=False,
                        default=1)

    parser.add_argument('--fires_column',
                        type=int,
                        help='Number (not the index, first column is one) of '
                             'column to be returned',
                        required=True)

    parser.add_argument('--file_name',
                        type=str,
                        help='filename to read from',
                        required=True)

    parser.add_argument('--operation',
                        type=str,
                        help='operation to perform on values, must be either '
                             'mean, median, or standard_deviation',
                        required=False)

    args = parser.parse_args()
    # Following uses the arguments returned by the parser for a function call
    fires = my_utils.get_column(args.file_name, args.country,
                                args.fires_column,
                                query_column=args.country_column)
    if fires.size == 0:
        sys.exit(1)  # Exit code updated to reflect that an error was
        # encountered and no values read
    elif args.operation is None:
        print(fires)
    elif args.operation == 'mean':
        print(my_utils.get_mean(fires))  # I'm still printing this, returning
        # from main seems unnecessary
    elif args.operation == 'median':
        print(my_utils.get_median(fires))
    elif args.operation == 'standard_deviation':
        print(my_utils.get_std_dev(fires))
    else:  # if fires is None (as indicates an error), this is false
        print("Error encountered. Check if operation is set to mean, median, "
              "or standard_deviation")
        sys.exit(1)  # Exit code updated to reflect that an error was
        # encountered


# Main function added
if __name__ == "__main__":
    main()
