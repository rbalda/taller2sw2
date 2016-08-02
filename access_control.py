import re
import time
from CardValidator import validate

time_re = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')

def validate_day_and_hour(message, day, hour):
    try:
        day = int(day)
    except ValueError:
        return False
    if day > 7 or day < 1:
        return False
    match = bool(time_re.match(hour))
    try:
        hour = time.strptime(hour,"%H:%M")
    except ValueError:
        return False

    if message=="employee":
        if day == 6 or day == 7:
            if hour > time.strptime("15:00","%H:%M") or hour < time.strptime("10:00","%H:%M"):
                return False
    elif message=="student":
        if day > 0 or day <6:
            if hour > time.strptime("18:00","%H:%M") or hour < time.strptime("08:00","%H:%M"):
                return False
        if day == 6 or day == 7:
            return False
    return True

# def system():
#     card_code = input("insert the digits of your card: ")
#     response = validate(card_code)
#     is_valid = response[0]
#     message = response[1]
#     if is_valid:
#         day = input ("insert the day of the week(1 to 7): ")
#         hour = input ("insert the hour(24 hrs): ")
#         if not validate_day_and_hour(message, day, hour):
#             return 0
#     else:
#         return 0
#     return 1
#
# if __name__=='__main__':
#     response = system()
#     print (response)