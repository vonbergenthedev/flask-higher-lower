from time import time


def timer_decorator(func):
    def wrapper(digits):
        start_time = time()
        result = func(digits)
        end_time = time() - start_time
        print(f'Runtime: {end_time}')
        return result
    return wrapper

@timer_decorator
def another_one(digits):

    return list(int(digit[1]) for digit in enumerate(str(int(''.join(str(digit) for digit in digits)) + 1)))

@timer_decorator
def another_one_2(digits):
    # Start from the last digit
    i = len(digits) - 1
    while i >= 0 and digits[i] == 9:
        # Change all 9s to 0
        digits[i] = 0
        i -= 1

    # If we found a non-9 digit, just add 1
    if i >= 0:
        digits[i] += 1
        return digits
    else:
        # All digits were 9, so add a leading 1
        return [1] + digits

print(another_one([9, 9]))
print(another_one_2([9, 9]))
