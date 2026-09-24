def celsius_to_fahrenheit(c:float) ->float:
    f = c * 9 / 5 + 32
    return f

c = float(input('input c'))
print(celsius_to_fahrenheit(c))