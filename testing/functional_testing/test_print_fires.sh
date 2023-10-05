test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# test_data.csv is file with all but two countries removed: the USA and Zimbabwe, the latter contains non-numeric entries
# in the specified column, which cause the stats functions to return none, but don't update the error codes.
# Errors opening the file does cause the error code to be set to 1

# Following should cause no issues
run positive_test python ../../src/print_fires.py --country 'United States of America' --fires_column 4 --file_name 'test_data/test_data.csv' --operation 'median'
assert_stdout 1558
assert_exit_code 0

# Following will finish with exit code 1, wrong file error
run unopened_file_test ../../src/python print_fires.py --country 'United States of America' --fires_column 4 --file_name 'WRONG' --operation 'median'
assert_exit_code 1

# Following should return None, but doesn't change error code
run NaN_Value_test ../../src/python print_fires.py --country 'Zimbabwe' --fires_column 4 --file_name 'test_data/test_data.csv' --operation 'mean'
assert_stdout None
assert_exit_code 0

# Operation spelled incorrectly, checks if "Error encountered..." message is output and error code updated
run incorrect_op_test ../../src/python print_fires.py --country 'United States of America' --fires_column 4 --file_name 'test_data/test_data.csv' --operation 'fdsfdfds'
assert_stdout Error encountered
assert_exit_code 1