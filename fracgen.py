#
# Generates fractions and writes its decimals
# (c) 2024 Rene Oudeweg
#
# python eo.py [startnumerator (even)] [endnumerator] [startdenominator (odd)] [enddenominator] optional: [float to search]


from termcolor import colored
from fractions import Fraction
import sys

PRECISION = 100
#MASKDIGITS = ['1','2','3', '4','5','6','7','8','9','0']
MASKDIGITS = []
BLINKDIGITS = []
MODE='all'
primes = []

def generate_fractions(startnumerator, endnumerator, startdenominator, enddenominator):
    fractions = []
    for i in range(startnumerator, endnumerator):
        for j in range(startdenominator, enddenominator):
            fractions.append((i, j))
    return fractions

def generate_fractions_e_o(startnumerator, endnumerator, startdenominator, enddenominator):
    fractions = []
    for i in range(startnumerator, endnumerator):
        # Check if i is even
        if i % 2 == 0:
            for j in range(startdenominator, enddenominator):
                if j % 2 != 0:
                    fractions.append((i, j))
    return fractions

def generate_fractions_o_e(startnumerator, endnumerator, startdenominator, enddenominator):
    fractions = []
    for i in range(startnumerator, endnumerator):
        # Check if i is even
        if i % 2 != 0:
            for j in range(startdenominator,enddenominator):
                if j % 2 == 0:
                    fractions.append((i, j))
    return fractions

def generate_fractions_o_o(startnumerator, endnumerator, startdenominator, enddenominator):
    fractions = []
    for i in range(startnumerator, endnumerator):
        # Check if i is even
        if i % 2 != 0:
            for j in range(startdenominator,enddenominator):
                if j % 2 != 0:
                    fractions.append((i, j))
    return fractions

def generate_fractions_e_e(startnumerator, endnumerator, startdenominator, enddenominator):
    fractions = []
    for i in range(startnumerator, endnumerator):
        # Check if i is even
        if i % 2 == 0:
            for j in range(startdenominator,enddenominator):
                if j % 2 == 0:
                    fractions.append((i, j))
    return fractions


def generate_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num*num, limit + 1, num):
                is_prime[multiple] = False
    
    for num in range(max(2, int(limit**0.5) + 1), limit + 1):
        if is_prime[num]:
            primes.append(num)
    
    return primes

def generate_fractions_o_p(startnumerator, endnumerator, primes):
    fractions = []
    for i in range(startnumerator, endnumerator):
        # Check if i is even
        if i % 2 != 0:
            for j in primes:
                fractions.append((i, j))
    return fractions

def generate_fractions_p_o(primes, startdenominator, enddenominator):
    fractions = []
    for i in primes:
        for j in range(startdenominator, enddenominator):
            if i % 2 != 0:
                fractions.append((i, j))
    return fractions

def generate_fractions_e_p(startnumerator, endnumerator, primes):
    fractions = []
    for i in range(startnumerator, endnumerator):
        # Check if i is even
        if i % 2 == 0:
            for j in primes:
                fractions.append((i, j))
    return fractions

def generate_fractions_p_p(primes1, primes):
    fractions = []
    for i in primes1:
        # Check if i is even
        for j in primes:
            fractions.append((i, j))
    return fractions


def generate_fractions_p_e(primes, startdenominator, enddenominator):
    fractions = []
    for i in primes:
        for j in range(startdenominator, enddenominator):
            if j % 2 == 0:
                fractions.append((i, j))
    return fractions


def is_whole_number(num):
    return num.is_integer()

import math

def is_exact_fraction(number):
    # Calculate the fractional part
    fractional_part = number % 1

    # Check if the fractional part is close to zero
    return math.isclose(fractional_part, 0, abs_tol=1e-9)  # Adjust abs_tol as needed

def has_finite_fraction(number):
    if not math.isfinite(number):
        return False
    return True

def read_integer(msg):
    try:
        number = int(input(msg))
        return number
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

def read_float(msg):
    try:
        number = float(input(msg))
        return number
    except ValueError:
        print("Invalid input. Please enter a valid float.")
        return None

def count_fractional_digits(number):
    # Convert the number to a string
    number_str = str(number)

    # Check if the string representation contains a decimal point
    if '.' in number_str:
        # Find the position of the decimal point
        decimal_position = number_str.index('.')
        
        # Count the number of digits after the decimal point
        fractional_digits_count = len(number_str) - decimal_position - 1

        return fractional_digits_count

    # If the number doesn't have a fractional part, return 0
    return 0

def has_repeating_fractional_digits(number):
    # Convert the fractional part to a string
    fractional_str = str(number).split('.')[1] if '.' in str(number) else ''

    # Check for repeating digits in the truncated fractional part
    for i in range(1, len(fractional_str) // 2 + 1):
        pattern = fractional_str[:i]
        truncated_fractional = fractional_str[:-2]  # Exclude the last two digits
        if all(truncated_fractional[j:j+i] == pattern for j in range(0, len(truncated_fractional), i)):
            return True
        truncated_fractional2 = fractional_str[:-3]  # Exclude the last three digits
        if all(truncated_fractional2[j:j+i] == pattern for j in range(0, len(truncated_fractional2), i)):
            return True

    return False

from decimal import Decimal, getcontext
import mpmath

def is_decimal_integer(decimal_number):
    # Set the precision for the Decimal module
    getcontext().prec = PRECISION  # Adjust the precision as needed

    # Check if the Decimal is equal to its integer representation
    return decimal_number == decimal_number.to_integral_value()


def has_repeating_fractional_digits_2(number):
    # Set the precision for the Decimal module
    getcontext().prec = PRECISION  # Adjust the precision as needed

    # Convert the Decimal to a string
    number_str = str(Decimal(str(number)))

    # Check for repeating digits in the truncated fractional part
    if '.' in number_str:
        fractional_str = number_str.split('.')[1]
        truncated_fractional = fractional_str[:-2]  # Exclude the last digit
        for i in range(1, len(truncated_fractional) // 2 + 1):
            pattern = truncated_fractional[:i]
            if all(truncated_fractional[j:j+i] == pattern for j in range(0, len(truncated_fractional), i)):
                return True
        truncated_fractional = fractional_str[:-3]  # Exclude the last digit
        for i in range(1, len(truncated_fractional) // 2 + 1):
            pattern = truncated_fractional[:i]
            if all(truncated_fractional[j:j+i] == pattern for j in range(0, len(truncated_fractional), i)):
                return True
    return False

def has_repeating_fractional_digits_3(number):
    # Set the precision for the Decimal module
    getcontext().prec = PRECISION  # Adjust the precision as needed

    # Convert the Decimal to a string
    number_str = str(Decimal(str(number)))

    # Check for repeating digits in the truncated fractional part
    if '.' in number_str:
        fractional_str = number_str.split('.')[1]
        truncated_fractional = fractional_str[1:-1]  # Exclude the first digit
        for i in range(1, len(truncated_fractional) // 2 + 1):
            pattern = truncated_fractional[:i]
            if all(truncated_fractional[j:j+i] == pattern for j in range(0, len(truncated_fractional), i)):
                return True
    return False

def print_fractional_digits_with_color(number, greppattern):
    # Convert the number to a string
    number_str = str(number)

 # Check if the string representation contains a decimal point
    if '.' in number_str:
        integer_part, fractional_str = number_str.split('.')
    else:
        integer_part, fractional_str = number_str, ''

    # Print the non-fractional part with white color
    for digit in integer_part:
        print(colored(digit, 'white', attrs=['bold']), end='')
    print('.', end='')

    index = fractional_str.find(greppattern)
    greplen = len(greppattern)
    indexstop = index+greplen-1

    n = 0
    # Print each digit with a different color
    for digit in fractional_str:
        color = 'white' if digit == '0' else 'light_green' if digit == '1' else 'light_yellow' if digit == '2' else 'light_blue' if digit == '3' else 'light_magenta' if digit == '4' else 'light_cyan' if digit == '5' else 'white' if digit == '6' else 'light_grey' if digit == '7' else 'white' if digit == '8' else 'red'
        if digit in MASKDIGITS:
            print(' ', end='')
        else:
            if n >= index and n <= indexstop:
                print(colored(digit, color, attrs=['bold', 'blink']), end='') 
            else:    
                if digit in BLINKDIGITS:
                    print(colored(digit, color, attrs=['bold', 'blink']), end='') 
                else:
                    if digit=='7':
                        print(colored(digit, color, attrs=['bold']), end='') 
                    else:
                        print(colored(digit, color), end='')      
            
        if n > indexstop:
            index = fractional_str.find(greppattern,n+2)
            if index != 0:
                indexstop = index+greplen-1
        n += 1

def compare_float_and_decimal(float_value, decimal_value):
    # Convert the float to Decimal for consistent comparison
    float_as_decimal = Decimal(str(float_value))

    # Compare the Decimal and the original Decimal
    if float_as_decimal == decimal_value:
        return True
    elif float_as_decimal < decimal_value:
        return False
    else:
        return False

from decimal import Decimal, getcontext

def compare_digit_by_digit_float_and_decimal(float_value, decimal_value):
    # Set the precision based on the number of digits in the float
    float_precision = len(str(float_value).split('.')[1])
    getcontext().prec = float_precision

    # Convert the float to Decimal
    float_as_decimal = Decimal(str(float_value))

    # Iterate through digits and compare
    for float_digit, decimal_digit in zip(str(float_as_decimal), str(decimal_value)):
        if float_digit == '.':
            continue  # Skip the decimal point
        if float_digit == decimal_digit:
            continue  # Digits match, continue to the next
        elif float_digit < decimal_digit:
            return "Less than"
        else:
            return "Greater than"

    # All digits match
    return "Equal"

""" # Example usage:
float_value = 3.141592653589793
decimal_value = Decimal('3.14159265358979323846')

result = compare_digit_by_digit_float_and_decimal(float_value, decimal_value)
print(f"Comparison result digit by digit: {result}")
 """

def grep_decimal(d, number_to_find, num_decimals):
    # Set the precision for Decimal operations
    getcontext().prec = num_decimals + 2  # Set precision to include more decimals

    # Convert the Decimal to a string
    decimal_str = str(d)

    # Check if the string representation contains a decimal point
    if '.' in decimal_str:
        # Extract the digits after the decimal point
        decimal_digits = decimal_str.split('.')[1]

        # Check if the number 'number_to_find' is in the decimal part
        return str(number_to_find) in decimal_digits
    else:
        return False  # No decimal digits if there is no decimal point


def main():
    startnumerator = 0
    startdenominator = 0
    endnumerator = 0
    enddenominator = 0
    grepfloat = 0
    grepnum = 0

    if len(sys.argv) > 1:
        startnumerator = int(sys.argv[1])
    else:
        startnumerator = read_integer("Enter start numerator:")
    if len(sys.argv) > 2:
        endnumerator = int(sys.argv[2]) + 1
    else:
        endnumerator = read_integer("Enter end numerator:")
        endnumerator += 1 
    if len(sys.argv) > 3:
        startdenominator = int(sys.argv[3])
    else:
        startdenominator = read_integer("Enter start denominator:")
    if len(sys.argv) > 4:
        enddenominator = int(sys.argv[4]) + 1
    else:
        enddenominator = read_integer("Enter end denominator:")
        enddenominator += 1
        
    if len(sys.argv) > 5:
        if '.' in sys.argv[5]:
            grepfloat = float(sys.argv[5])  
        else:
            grepnum = int(sys.argv[5])
            grepfloat = 0
  
    global MODE
    if len(sys.argv) > 6:
        MODE = sys.argv[6]  
    
    global PRECISION
    if len(sys.argv) > 7:
        PRECISION = int(sys.argv[7]) 

    print(f"MODE: {MODE} - PRECISION: {PRECISION}-\nnumerator:\t{startnumerator} - {endnumerator}\ndenominator:\t{startdenominator} - {enddenominator}\ngrepnum: {grepnum} grepfloat: {grepfloat}")


    getcontext().prec = PRECISION  # Adjust the precision as needed
    mpmath.mp.dps = PRECISION  # Set the precision to 50 digits

    if MODE=='eo':
        fractions = generate_fractions_e_o(startnumerator, endnumerator, startdenominator, enddenominator)    
    elif MODE == 'oe':
        fractions = generate_fractions_o_e(startnumerator, endnumerator, startdenominator, enddenominator)
    elif MODE == 'ee':
        fractions = generate_fractions_e_e(startnumerator, endnumerator, startdenominator, enddenominator)
    elif MODE == 'oo':
        fractions = generate_fractions_o_o(startnumerator, endnumerator, startdenominator, enddenominator)
    elif MODE == 'all':
        fractions = generate_fractions(startnumerator, endnumerator, startdenominator, enddenominator)
    elif MODE == 'ep':
        primes = generate_primes(enddenominator)
        fractions = generate_fractions_e_p(startnumerator, endnumerator, primes)
    elif MODE == 'pe':
        primes = generate_primes(enddenominator)
        fractions = generate_fractions_p_e(primes,startdenominator, enddenominator)
    elif MODE == 'op':
        primes = generate_primes(enddenominator)
        fractions = generate_fractions_o_p(startnumerator, endnumerator, primes)
    elif MODE == 'po':
        primes = generate_primes(enddenominator)
        fractions = generate_fractions_p_o(primes, startdenominator, enddenominator)
    elif MODE == 'pp':
        primes = generate_primes(enddenominator)
        fractions = fractions = generate_fractions_p_p(primes, primes)


    for fraction in fractions:

        # Initialize a Decimal with a fraction
        
        frac = Fraction(str(fraction[0])+"/"+str(fraction[1]))
        num = Decimal(str(mpmath.mpf(frac.numerator) / mpmath.mpf(frac.denominator)))

        #num = Decimal(mpmath.mpf(Fraction('3/27')))

        # num = fraction[0]/fraction[1]
        
        if (grepfloat!=0):
            result = compare_digit_by_digit_float_and_decimal(grepfloat, num)
            if (result=="Equal"):
                print(f"{fraction[0]}/{fraction[1]}  \t= ", end='')
                print_fractional_digits_with_color(num, str(grepfloat))
                print()
            continue
        if (grepnum!=0):
            if grep_decimal(num, grepnum, len(str(grepnum))):
                print(f"{fraction[0]}/{fraction[1]}  \t= ", end='')
                print_fractional_digits_with_color(num, str(grepnum))
                print()
                continue
        elif (grepnum==0):    
            if is_decimal_integer(num):
                print(f"{fraction[0]}/{fraction[1]}  \t= " +  colored(str(num), "red", attrs=["bold"]))
            else:
                print(f"{fraction[0]}/{fraction[1]}  \t= ", end='')
                print_fractional_digits_with_color(num, '')
                print()
    print("\n\n")

if __name__ == "__main__":
    main()
