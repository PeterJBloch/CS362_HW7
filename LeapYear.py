def LeapYear(number):
    if number%4 ==0:
        if number%100 ==0:
            if number%400==0:
                return True
            return False
        return True
    return False