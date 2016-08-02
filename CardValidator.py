

def validate(card_digits):
    """
    This function validate a string of numbers
    """
    i=0
    student = None
    first = None
    if len(card_digits) != 7:
        return [False,'is not a valid code']
    for digit in card_digits:
        i = i+1
        try:
            int(digit)
        except ValueError:
            return [False,'is not a valid code, not a number']
        if i == 1 and digit == "0":
            first = 0
            pass
        if i==2 and digit == "0" and first == 0:
            i = 7
            break
        if i == 7:
            student = 1
        else:
            student =0
    if i == 7:
        if student == 1:
            return [True,'student']
        elif student == 0:
            return [True, 'employee']