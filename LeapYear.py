def LeapYear(number):
    if number%4 ==0:
        if number%100 ==0:
            return False
        return True
    return False