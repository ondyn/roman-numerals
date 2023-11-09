import unittest


class RomanNumeralsTest(unittest.TestCase):
    test_list = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        10: 'X',
        11: 'XI',
        14: 'XIV',
        15: 'XV',
        19: 'XIX',
        20: 'XX',
        30: 'XXX',
        39: 'XXXIX',
        40: 'XL',
        45: 'XLV',
        50: 'L',
        60: 'LX',
        70: 'LXX',
        80: 'LXXX',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    def test_Roman_convertor(self):
        for arabic, roman in self.test_list.items():
            self.assertEqual(convert(arabic), roman)


def convert(number):
    if not 0 < number < 4000:
        raise ValueError("Number must be between 1 and 3999. I cant do more for you.")
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_string = ''
    for value, numeral in roman_numerals.items():
        while number >= value:
            roman_string += numeral
            number -= value

    return roman_string
    
print(convert(1))



# run test: /usr/local/bin/python3 -m unittest /Users/ondrejhnyk/Documents/roman-numerals/python/test_roman_numerals.py
# tip:
# def arabic_to_roman(number):
#     if not 0 < number < 4000:
#         raise ValueError("Number must be between 1 and 3999")

#     roman_numerals = {
#         1000: 'M',
#         900: 'CM',
#         500: 'D',
#         400: 'CD',
#         100: 'C',
#         90: 'XC',
#         50: 'L',
#         40: 'XL',
#         10: 'X',
#         9: 'IX',
#         5: 'V',
#         4: 'IV',
#         1: 'I'
#     }

#     roman_string = ''
#     for value, numeral in roman_numerals.items():
#         while number >= value:
#             roman_string += numeral
#             number -= value

#     return roman_string

# # Example usage:
# arabic_number = 354
# roman_numeral = arabic_to_roman(arabic_number)
# print(f"The Roman numeral for {arabic_number} is {roman_numeral}")
