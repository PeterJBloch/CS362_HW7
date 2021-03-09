def FizzBuzz(number):
    text = ""
    if number%3 ==0:
        text+="Fizz"
    if number%5 ==0:
        text+="Buzz"
    return text