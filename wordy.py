st='5 plus 3'
def wordy(coll):
    if coll.isnumeric():                                                           #iteration:0
        return int(coll)
    if "plus" in coll:                                                             #iteration:1
        numbers = [int(num) for num in coll.split() if num.isdigit()]
        return sum(numbers)
    if "minus" in coll:                                                             #iteration:2
        numbers = [int(num) for num in coll.split() if num.isdigit()]
        return numbers[0] - numbers[1]
    if "multiplied by" in coll:    
        numbers = [int(num) for num in coll.split() if num.isdigit()]
        return numbers[0] * numbers[1]
    if "divided by" in coll:
        numbers = [int(num) for num in coll.split() if num.isdigit()]
        return numbers[0] / numbers[1]
    if "plus" in coll and "multiplied by" in coll:                              #iteration:3
        numbers = [int(num) for num in coll.split() if num.isdigit()]
        result = numbers[0]
        for i in range(1, len(numbers), 2):
            if coll.split()[i] == "plus":
                result += numbers[i + 1]
            elif coll.split()[i] == "multiplied":
                result *= numbers[i + 2]
        return result

    raise ValueError("unknown operation")                                       #iteartion:4
x=wordy(st)
print(x)