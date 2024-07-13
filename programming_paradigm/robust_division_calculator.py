def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Attempt the division
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
    
    except ValueError:
        return f"Error: Please enter numeric values only."
