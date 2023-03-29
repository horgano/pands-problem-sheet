# es.py
# Author Niall Horgan

# Program is given file to read in as an argument in cmd line and counts the occurrances of the letter 'e'

import sys 

file_to_read = sys.argv[1]

with open (file_to_read) as f:
    data = f.read()
    lower_case = data.count('e')
    upper_case = data.count('E')
    print (f'The numbers of occurrences of the letter \'e\' is: {lower_case + upper_case}')
    
    # print (data)

