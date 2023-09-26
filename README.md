[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# Printing Fires with Blazing Efficiency and Undeniable Panache
## Overview
print_fires.py takes a filename, a query column number, a query value, and a result column number. column numbers are natural numbers, *not* indices. The intended use employs a country name as the query value. Using the function get_column defined in my_utils.py, it opens the file given by the file name, and filters the values in the results column to only those whose corresponding value is the query column matches the query value. Note that the file must be formatted as a csv, included in the current directory. These values are truncated to integers if possible, but if non-numeric values are found, the returned/printed list will include Nan (type float) values.
## Example Usage
The parameters are named and given via the command line. See run.sh for an examples of a terminal command to run (and two examples of incorrect usage). For an example using all four command line arguments (including a value specified for country_column, the only one with a built-in default), see below: <br>
```
python print_fires.py --country 'United States of America' --country_column 1 --fires_column 4 --file_name 'Agrofood_co2_emission.csv'
```
This prints the integer number of fires in the specified country, each year.

What follows is another example using the same files and arguments, but an alternative query value and corresponding column number to print integer list of fires taking place in a specified year:
```
python print_fires.py --country '1998' --country_column 2 --fires_column 4 --file_name 'Agrofood_co2_emission.csv'
```
