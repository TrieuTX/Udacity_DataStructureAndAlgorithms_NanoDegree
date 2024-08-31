"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
duration_of_phoneNumber = {}
for call in calls:
    call_incoming_number = call[0]
    call_answering_number = call[1]
    duration = int(call[3])

    duration_of_phoneNumber[call_incoming_number] = (
        duration
        if (call_incoming_number not in duration_of_phoneNumber)
        else (duration_of_phoneNumber[call_incoming_number] + duration)
    )
    duration_of_phoneNumber[call_answering_number] = (
        duration
        if (call_answering_number not in duration_of_phoneNumber)
        else (duration_of_phoneNumber[call_answering_number] + duration)
    )

longest_duration = 0
phone_number_longest_duration = ""
for phone_number, duration in duration_of_phoneNumber.items():
    if longest_duration < duration:
        longest_duration = duration
        phone_number_longest_duration = phone_number

print(f"{phone_number_longest_duration} spent the longest time, {longest_duration} seconds, on the phone during September 2016.")
