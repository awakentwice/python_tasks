#average1_ans.py
#TODO задача не сделана
numbers = []
sum = 0
lowest = None
highest = None

while True:
    try:
        line = input('Enter a number or Enter to finish: ')

        if not line:
            break

        number = int(line)
        numbers.append(number)
        sum += number

        if lowest is None or lowest > number:
            lowest = number

        if highest is None or highest < number:
            highest = number

    except ValueError as err:
        print('Error: You should enter a number.')

print('numbers', str(numbers).strip('[]'))

if numbers:
    print(
        'count', len(numbers),
        'sum', sum,
        'lowest', lowest,
        'highest', highest,
        'mean', sum / len(numbers)
    )
