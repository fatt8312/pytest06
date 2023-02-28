def validate_number(number):
    if type(number) != int :
        if type(number) == str:
            return "input_integer"
        if number >= 1 and number <= 12 :
            return "input_integer"
        else:
            return "out_of_range"
    elif number >= 1 and number <= 12 :
        return number
    else:
        return "out_of_range"

def number_to_month(number):
    month = ["january","february","march","april","May","June","July","August","September","October","November","December"]
    return month[number-1]

def display_month(number):
    result = validate_number(number)
    if type(result) == int:
        return number_to_month(result)
    else:
        return result
