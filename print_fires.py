import my_utils
import argparse
import sys


def main():

    parser = argparse.ArgumentParser(
                description='This is the preferred way.',
                prog='print_fires.py'
    )
    parser.add_argument('--country',
                        type=str,
                        help='The name of the country used as query',
                        required=True)

    parser.add_argument('--country_column',  # This is the one argument with a default, default is built into my_utils
                        type=int,
                        help='Number (not the index, first column is one) of column query value resides in',
                        required=False,
                        default=1)
    # default value to one, this is also handled by the function, but prevents None being passed to function

    parser.add_argument('--fires_column',
                        type=int,
                        help='Number (not the index, first column is one) of column to be returned',
                        required=True)

    parser.add_argument('--file_name',
                        type=str,
                        help='filename to read from',
                        required=True)

    args = parser.parse_args()
    # args.fires_column

    # country='United States of America'
    #  county_column = 1
    #  fires_column = 4
    #  file_name = 'Agrofood_co2_emission.csv'
    # fires = my_utils.get_column(file_name,country,fires_column,query_column=county_column)
    fires = my_utils.get_column(args.file_name, args.country, args.fires_column, query_column=args.country_column)
    if fires:  # if fires is None, this conditional is false
        print(fires)
        return
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
