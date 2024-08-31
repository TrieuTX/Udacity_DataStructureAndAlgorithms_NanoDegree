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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
first_text = texts[0]
text_incoming_number = first_text[0] if len(first_text[0]) else None
text_answering_number = first_text[1] if len(first_text[1]) else None
text_time = first_text[2] if len(first_text[2]) else None

# Extracting the last record from calls
last_call = calls[-1]
call_incoming_number = last_call[0] if len(last_call[0]) else None
call_answering_number = last_call[1] if len(last_call[1]) else None
call_time = last_call[2] if len(last_call[2]) else None
call_duration = last_call[3] if len(last_call[3]) else None

# Printing the required messages
print(
    f"First record of texts, {text_incoming_number} texts {text_answering_number} at time {text_time}")
print(
    f"Last record of calls, {call_incoming_number} calls {call_answering_number} at time {call_time}, lasting {call_duration} seconds")
