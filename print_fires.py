import my_utils
import argparse
import sys


def main():
    # Initializing a parser object, which contains arguments with specified properties
    parser = argparse.ArgumentParser(
                description='This is the preferred way to parse command line arguments.',
                prog='print_fires.py')

    parser.add_argument('--country',
                        type=str,
                        help='The name of the country used as query',
                        required=True)

    # Following has default of one, a default is also supplied by get_column, but this prevents None from being passed
    # to my_utils if this argument isn't included in the command line.
    parser.add_argument('--country_column',  # This is the one argument with a default, default is built into my_utils
                        type=int,
                        help='Number (not the index, first column is one) of column query value resides in',
                        required=False,
                        default=1)

    parser.add_argument('--fires_column',
                        type=int,
                        help='Number (not the index, first column is one) of column to be returned',
                        required=True)

    parser.add_argument('--file_name',
                        type=str,
                        help='filename to read from',
                        required=True)

    args = parser.parse_args()
    # Following uses the arguments returned by the parser for a function call
    fires = my_utils.get_column(args.file_name, args.country, args.fires_column, query_column=args.country_column)
    if fires:  # if fires is None (as indicates an error), this conditional is false
        print(fires)
    else:
        sys.exit(1)  # Exit code updated to reflect that an error was encountered


# Main function added
if __name__ == "__main__":
    main()
