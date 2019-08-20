def increment_string(strng):

    # if string is empty, return '1'

    if not strng:
        return '1'
    else:

        # if string is not empty, check if it consists only of numbers

        if strng.isnumeric():
            digits = strng
            letters = ''
            number = int(digits)
            number_plus_one = str(number + 1)
        else:

            # if string does not consist only of numbers

            digits_reversed = ''
            counter = -1

            while strng[counter].isdigit():
                digits_reversed += strng[counter]
                counter -= 1

            digits = digits_reversed[::-1]
            letters = strng[:counter+1]

            # if there were no digits at the end of the string, add '1' to the end of the string

            if not digits:
                return strng + '1'

            else:
                number = int(digits)
                number_plus_one = str(number + 1)

        # check for leading zeroes and increment accordingly

        if len(digits) != len(number_plus_one):
            for i in range((len(digits)-len(number_plus_one))):
                letters += '0'
        incremented_string = letters + number_plus_one

        return incremented_string
