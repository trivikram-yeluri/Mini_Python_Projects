## Temparature Conversion

def temparature_conversion(temp,unit):
    """Convert temparature between Celcius and Farhenheit"""
    if unit == "C":
        return temp * 9/5 + 32
    elif unit == "F":
        return (temp - 32) * 5/9
    else:
        return None
conversion = temparature_conversion(32,"C")
print(conversion)