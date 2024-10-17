def is_harshad(n):
    # Convert the number to a string to easily iterate through digits
    digit_sum = sum(int(digit) for digit in str(n))
    return n % digit_sum == 0

# Example usage:
number = 18
if is_harshad(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")
