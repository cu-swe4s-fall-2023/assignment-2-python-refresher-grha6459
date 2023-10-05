[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# Printing Fires with Blazing Efficiency and Undeniable Panache
## Overview
print_fires.py takes a filename, a query column number, a query value, and a result column number. column numbers are natural numbers, *not* indices. The intended use employs a country name as the query value. Using the function get_column defined in my_utils.py, it opens the file given by the file name, and filters the values in the results column to only those whose corresponding value is the query column matches the query value. Note that the file must be formatted as a csv, included in the current directory. These values are truncated to integers if possible, but if non-numeric values are found, the returned/printed list will include Nan (type float) values.
If the --operation parameter is included, print_fires will instead return the mean, median or standard deviation of the values.
## Example Usage
The parameters are named and given via the command line. See test_my_utils.py for example function runs.
```
python print_fires.py --country 'United States of America' --country_column 1 --fires_column 4 --file_name 'Agrofood_co2_emission.csv'
```
This prints the integer number of fires in the specified country, each year. 
If the file is unable to be opened, or an empty array is read from it, error codes are set to 1 and an error message may be displayed.
If non-numeric values are in the queried column, the statistical functions will return None.

Unit and functional testing have also been added in the testing directory. The test_my_utils.py file creates a class to test the statistical capabilities.
Finally, functional testing using the Stupid Simple Bash Testing framework (see here for more detail: https://github.com/ryanlayer/ssshtest). A test csv file has been added to this directory in the test_data subdirectory.