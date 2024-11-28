import random
roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

def romanToInt(s):
        s = s.upper()
        sum = 0
        numeral_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for index, item in enumerate(s):
            if item not in roman_numerals:
                return 'invalid'
            
            next = index + 1
            number = numeral_values.get(item)
            if next < len(s):
                second_number = numeral_values.get(s[next])

                if number == 5 and second_number == 5 or number == 50 and second_number == 50 or number == 500 and second_number == 500:
                    return 'Invalid'
                    
                if next + 2 < len(s):
                    third_number = numeral_values.get(s[index + 2])
                    fourth_number = numeral_values.get(s[index + 3])
                    if number == second_number and second_number == third_number and third_number == fourth_number:
                        return 'Invalid'
                    
                if number == 1 and second_number == 5 or number == 1 and second_number == 10:
                    number = number - 2
                elif number == 10 and second_number == 50 or number == 10 and second_number == 100:
                    number = number - 20
                elif number == 100 and second_number == 500 or number == 100 and second_number == 1000:
                    number = number - 200   
            
            sum = sum + number
        return sum

def rgenNumeral():
    with open('/home/cameron/repos/roman-numeral-decoder/random-numerals.txt') as f:
        data = [line.strip('\n') for line in f.readlines()]
        random_numeral = random.randint(0, len(data) - 1)
        return str(data[random_numeral])
    f.close()