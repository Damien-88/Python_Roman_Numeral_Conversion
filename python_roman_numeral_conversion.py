import os

class Roman:
    
    def __init__(self):
        # Dictionary for Roman Numeral to Integer Conversion
        self.rom_int_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # Inverted Dictionary for Integer to Roman Numeral Conversion 
        self.int_rom_dict = dict([(value, key) for key, value in self.rom_int_dict.items()])
            # {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    
    # Function for Converting Roman Numerals to Integers
    def roman_to_integer(self, numerals):
        # Ensure all input is the same case. Temp variable holding last value, for easy comparison.
        numerals = numerals.upper()
        temp = self.rom_int_dict[numerals[0]]
        answer = self.rom_int_dict[numerals[0]]

        # Loop through each numaral in input
        for letter in numerals[1:]:
            # Check if input is a valid roman numeral
            # If So. Compare values. 
            if letter in self.rom_int_dict:
                # If previous is less than current, reduce total by the value of the previous value 
                # Add the difference of the previous value from the current   to the answer
                if temp < self.rom_int_dict[letter]:
                    answer += self.rom_int_dict[letter] - 2 * temp
                # If current is greater, add the value to the answer.
                else:
                    answer += self.rom_int_dict[letter]
                temp = self.rom_int_dict[letter]
            # If not, output message. Retrieve valid input. Recurse function.
            else:
                print("\nInvalid Entry! \nEnter a Roman Numeral : I, V, X, L, C, D, M\n")
                numerals = input("\nPlease enter the Roman Numeral you wish to convert: ")
                self.roman_to_integer(numerals)
        # Output Converted Value
        return answer
    
    # Function for Converting Integers to Roman Numerals   
    def integer_to_roman(self, number):
        # Ensure the number is within the scope of the function
        if number >= 4000:
            print("\nInvalid Entry! \nThis conversion can only handle numbers less than 4,000")
            number = input("\nPlease enter the number you wish to convert: ")
            self.integer_to_roman(int(number))
        # Convert the number to a string to enable parsing to a list. Set default list.
        num_string = str(number)
        num_list = [0, 0, 0, 0]
        # Get the size and the difference from the length of the list. 
        size = len(num_string)
        dif = 4 - len(num_string)
        roman = ""
        # Loop through the string and add the value to the list.
        # Use dif to ensure the number's digit place coincides with a specific list index.
        for let in range(size):
            num_list[let + dif] = int(num_string[let])
        # Set variables for starting points in the thousands[M]
        prev = 10000
        mid = 5000
        cur = 1000
        # Loop through each number in the list. Verify value and update answer string appropriately.
        # If no place value: default list will be 0, variables will reduce and loop will continue.
        for num in num_list:
            if num == 9:
                roman += self.int_rom_dict[cur] + self.int_rom_dict[prev]
            elif num >= 5:
                roman += self.int_rom_dict[mid] + self.int_rom_dict[cur] * (num - 5)
            elif num == 4:
                roman += self.int_rom_dict[cur] + self.int_rom_dict[mid]
            elif num > 0:
                roman += self.int_rom_dict[cur] * num
            # Reduce the variable to the next digit place: thousands, to hundreds, to tens, to ones
            prev /= 10
            mid /= 10
            cur /= 10
        # Output Converted Value    
        return roman


def convert():
    conversion = Roman()

    print("\n\tROMAN NUMERAL CONVERTER\n")

    int_or_rom = input("Enter 1 to convert a Roman Numeral to a Number.\nEnter 2 to convert a Number to a Roman Numeral. ")

    if int_or_rom == "1":
        numeral = input("\nEnter the Roman Numeral you wish to convert: ")
        answer = conversion.roman_to_integer(numeral)
    elif int_or_rom == "2":
        number = input("\nEnter the Number you wish to convert: ")
        answer = conversion.integer_to_roman(int(number))
    else:
        print("\nPlease Enter A Valid Input! 1 or 2: ")
        convert()

    print(answer)
    
    again = input("\nWould you like to conduct another conversion? y/n: ")

    if again == "y":
        os.system('cls')
        convert()



convert()