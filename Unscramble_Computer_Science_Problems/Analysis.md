## Runtime Analysis (Worst-Case Big-O Notation):
### Task 0
1. Accessing records: `O(1)` for accessing both the first and last records from the texts and calls lists.
2. Printing the results: `O(1)` for each print statement.

The overall runtime complexity is `O(1)`
### Task 1
``` Python
uni_numbers = []

for text in texts:
    if (text[0] not in uni_numbers):
        uni_numbers.append(text[0])
    if (text[1] not in uni_numbers):
        uni_numbers.append(text[1])

for call in calls:
    if (call[0] not in uni_numbers):
        uni_numbers.append(call[0])
    if (call[1] not in uni_numbers):
        uni_numbers.append(call[1])
```
1. Checking if a number is in uni_numbers: has a time complexity of `O(k)`,k is the length of uni_numbers
2. Appending a number: has a time complexity of `O(1)`
3. For n text records, the loop runs `2n` checks, each with a worst-case complexity of `O(k)`, for m call records, the loop runs `2m` checks, each with a worst-case complexity of `O(k)`

The worst-case time complexity for this section is `O(n * k + m * k)`, where k is the number of unique phone numbers. Since k can equal to `2(n + m)`, the complexity can be `O((n + m)^2)`.

### Task 2
1. Iterating Over Calls
``` Python
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
```
 The loop runs n times, update list with time Complexity `O(1)` 
 
 => Overall Time Complexity for the Loop: `O(n)`
 
 2. Find the Longest Duration
 ```Python 
longest_duration = 0
phone_number_longest_duration = ""
for phone_number, duration in duration_of_phoneNumber.items():
    if longest_duration < duration:
        longest_duration = duration
        phone_number_longest_duration = phone_number
 ```
 The loop iterates `k` times, but unique phone numbers `k` is at most `2n`
 
 => Overall Time Complexity for the Loop: `O(k)`

#### Total Complexity:
The total time complexity of the two loops: `O(n + k)`.
unique phone numbers `k` is at most `2n`, the complexity can be simplified to `O(n)`.

### Task 3
```Python
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

```
Part A:
1. Time Complexity for the Loop: `O(n)`
2. Checking Caller Prefix: `O(1)`
3. Fixed-Line Number Handling: `O(k)`  in the worst case
4. Telemarketer and Mobile Number Handling: `O(k)`  in the worst case
5. Insertion into the List: `O(k)`  in the worst case

=> for all `n` calls, the worst-case time complexity is `O(n * k)`

 Part B: The time complexity for Part B is primarily `O(1)`, for all `n` calls, the overall complexity is `O(n)`.

``` Python
for code in sorted(bangalore_receiver_code):
    print(code)
```

Sorting bangalore_receiver_code, which contains k unique codes, has a time complexity of `O(k log k)`.
#### Total Complexity:
Total time complexity `O(n * k + k log k)`.
In the worst case, if every call has a unique code, `k` could be as large as `n`. Thus, the complexity could simplify to `O(n^2 + n log n)`.

### Task 4
``` Python 
for call in calls:
    if call[0] not in outgoing_calls:
        outgoing_calls.append(call[0])
    if call[1] not in incoming_calls:
        incoming_calls.append(call[1])
```
- Loop Over Calls: The loop iterates over all `m` call records.
- Checking condition: The condition call[0] not in outgoing_calls and call[1] not in incoming_calls are `O(n)` operations in the worst case
- Appending to List: Appending to a list is O(1).

Total Complexity for `m` call records: `O(m * n)`
``` Python 
for text in texts:
    if text[0] not in outgoing_texts:
        outgoing_texts.append(text[0])
    if text[1] not in incoming_texts:
        incoming_texts.append(text[1])
```
- Same analysis applies as in previous step, for `p` text records

Total Complexity for `p` text records: `O(p * n)`
```Python
for call in outgoing_calls:
    if (call not in incoming_calls
        and call not in outgoing_texts
            and call not in incoming_texts):
        telemarketers.append(call)
```
- Loop Over Outgoing Calls: The loop iterates over all `n` outgoing calls.
- Checking conditon: Check the call is not in incoming_calls, outgoing_texts, and incoming_texts. Each of these checks has a time complexity of O(n) in the worst case.

Total Complexity for `n` outgoing calls: `O(n^2)`
``` Python 
for call in sorted(telemarketers):
    print(call)
```
- Sorting: Sorting the list of telemarketers has a time complexity of `O(t log t)`, where t is the number of telemarketers

Total Complexity for `t` number of telemarketers: `O(t log t)`

#### Total Complexity: 
The most significant complexity comes from the telemarketer identification step: `O(n^2)`. Total Time Complexity is `O(n^2)`.