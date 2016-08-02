def money_to_pay(day):
    if day==5:
        return 0
    if day > 0 and day < 5:
        return 0.25

def payment(day, card):
    passage = money_to_pay(day)
    if card.credit<passage:
        return 0
    return 1