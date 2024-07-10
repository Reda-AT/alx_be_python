FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
def convert_to_celsius(fahrenheit):
    Tc= fahrenheit*FAHRENHEIT_TO_CELSIUS_FACTOR
    print (fahrenheit,'°F is',Tc,'°C')
def convert_to_fahrenheit(celsius):
    Tc= celsius*CELSIUS_TO_FAHRENHEIT_FACTOR
    print (celsius,'°C is',Tc,'°F')
while True:
    T = input("Enter the temperature to convert:")
    try:
        t = float(T)
        if t >= 0:
            break
        else:
            print("The number is not positive. Please try again.")
    except ValueError:
        print("That's not a valid number. Please try again.")
U=input("Is this temperature in Celsius or Fahrenheit? (C/F):").lower()
def main(t,U):
    match U:
        case "f":
            convert_to_celsius(t)
        case "c":
            convert_to_fahrenheit(t)
        case _:
            U=input("Invalid answer, please enter C or F")
            main(T)
main(t,U)