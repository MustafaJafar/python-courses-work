def converter (original_unit , coefficient = 0.3048 ) :
    return original_unit * coefficient

def celsius_to_fahrenheit(c) :
    return (c * (9/5) + 32)

def string_length(mystring):
    if(type(mystring) == int) :
        return "Sorry integers don't have length"
    elif(type(mystring) == float) :
        return "Sorry floats don't have length"
    else :
        return len(mystring)

print (converter(10 , 5))
print (converter(10))

print(celsius_to_fahrenheit(20))

print(string_length(10))
print(string_length(10.0))

#you can write function in 1 single line : 
sqrt = lambda x : x**0.5
print(sqrt(25))