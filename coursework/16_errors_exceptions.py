def divide(a,b) :
    try:
        return (a / b )
    except ZeroDivisionError : #(1,0) #exceptions with certain error !
        return ("Zero division is meaningless")
    except TypeError : #("1" , 2)
        return ("enter numbers only")

print( divide(1,2))