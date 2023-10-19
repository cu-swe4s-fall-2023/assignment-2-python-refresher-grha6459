test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest



# Testing processing on small subset of data

#Unfortunantly, bottom test doesn't run, as the space in the filename causes issues with ssshtest
#run processing_test_1 python ../../src/export_CO2.py --country 'United States of America' --file_name 'test_data/test_data.csv' --column_numbers 27 26 30 9 12
#assert_equal $'United States of America_processed.csv' $( ls $'United States of America_processed.csv' )

run processing_test_2 python ../../src/export_CO2.py --country 'Uruguay' --file_name 'test_data/test_data.csv' --column_numbers 27 26 30 9 12
assert_equal $'Uruguay_processed.csv' $( ls $'Uruguay_processed.csv' )

# Test plotting
run plot_test1 python ../../src/process_and_plot.py
assert_equal $'fig1.png' $( ls $'fig1.png' )