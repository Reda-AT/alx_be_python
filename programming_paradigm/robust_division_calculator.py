def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Attempt the division
        result = numerator / denominator
        print("The result of the division is",result)
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
    except ValueError:
        print("Error: Please enter numeric values only.")
    except Exception as e:
        print(e)

