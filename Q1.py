def my_func(x1,x2,x3):
    if type(x1) != float and type(x1) != int or type(x2) != float and type(x2) != int or type(x3) != float and type(x3) != int:
        return "None"
    elif type(x1) == int or type(x2) == int or type(x3) == int:
        print("Error: parameters should be float")
    elif x1+x2+x3 == 0:
        print("Not a number – denominator equals zero")
    else:
        return float(((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3))
