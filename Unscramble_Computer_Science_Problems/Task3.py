"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

bangalore_code = "(080)"

bangalore_receiver_code = []

bangalore_receiver_count = 0
bangalore_receiver_internalCall_count = 0

for call in calls:
    caller = call[0]
    receiver = call[1]
# Part A
    if caller.startswith(bangalore_code):
        if receiver.startswith('('):
            start_index = receiver.find('(') + 1
            end_index = receiver.find(')')
            fixed_line_code = receiver[start_index:end_index]
            if fixed_line_code not in bangalore_receiver_code:
                bangalore_receiver_code.append(fixed_line_code)
        elif receiver[:3].startswith('140'):
            telemarketers_code = receiver[:3]
            bangalore_receiver_code.append(telemarketers_code)
        elif ' ' in receiver and receiver[0] in ['7', '8', '9']:
            mobile_code = receiver[:4]
            if mobile_code not in bangalore_receiver_code:
                bangalore_receiver_code.append(mobile_code)

# Part B
        bangalore_receiver_count += 1
        if receiver.startswith(bangalore_code):
            bangalore_receiver_internalCall_count += 1

# Print the list of codes
print("The numbers called by people in Bangalore have codes:")
for code in sorted(bangalore_receiver_code):
    print(code)

# Print the answer as a part of a message::
# The percentage should have 2 decimal digits
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    round(bangalore_receiver_internalCall_count /
          bangalore_receiver_count * 100, 2)
)
)
