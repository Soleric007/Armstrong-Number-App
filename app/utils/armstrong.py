def is_armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    total = sum(int(digit) ** num_len for digit in num_str)
    return total == number

def find_armstrong_in_range(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num)]
