"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_texts = []
incoming_texts = []
outgoing_calls = []
incoming_calls = []
telemarketers = []

for call in calls:
    if call[0] not in outgoing_calls:
        outgoing_calls.append(call[0])
    if call[1] not in incoming_calls:
        incoming_calls.append(call[1])

for text in texts:
    if text[0] not in outgoing_texts:
        outgoing_texts.append(text[0])
    if text[1] not in incoming_texts:
        incoming_texts.append(text[1])

for call in outgoing_calls:
    if (call not in incoming_calls
        and call not in outgoing_texts
            and call not in incoming_texts):
        telemarketers.append(call)

# Print a message:
print("These numbers could be telemarketers: ")
for call in sorted(telemarketers):
    print(call)
