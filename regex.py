# Regular Expression 
import re 

date_data = '13/Feb/2019 lorem ipsum'
# pattern
date_pattern = re.compile(r'\d+/[a-zA-Z]+/\d{4}')

# r is raw string  
'''
if re.match(r'\d+/[a-zA-Z]+/\d{4}', date_data):
    print("Matched")
else:
    print("Mismatched")
'''

'''
if date_pattern.match(date_data):
    print("Matched")
else:
    print("Mismatched")
'''

'''
result = date_pattern.findall(date_data)
print(result)
'''
