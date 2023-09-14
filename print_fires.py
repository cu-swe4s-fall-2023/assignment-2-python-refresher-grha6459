import my_utils

country='United States of America'
county_column = 1
fires_column = 4
file_name = 'Agrofood_co2_emission.csv'
fires = my_utils.get_column(file_name,country,fires_column,query_column=county_column)
print(fires)
