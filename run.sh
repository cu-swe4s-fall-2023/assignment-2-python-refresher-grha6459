#!/bin/bash
# WHAT ELSE GOES IN THE TOP

# Below works, default value for country_column is 1, as handled by argparse
python print_fires.py --country 'United States of America' --fires_column 4 --file_name 'Agrofood_co2_emission.csv'
# Below doesn't work, filename misspelled
python print_fires.py --country 'United States of America' --fires_column 4 --file_name 'Agrofood_co2_emissiogfdgfn.csv'
# Below also doesn't work, missing fires_column argument
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emissiogfdgfn.csv'