FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_FAHRENHEIT = 32

def convert_to_celsius(fahrenheit):
    """Converts a Fahrenheit temperature to Celsius."""
    return (fahrenheit-FREEZING_POINT_FAHRENHEIT)*FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts a Celsius temperature to Fahrenheit."""
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+FREEZING_POINT_FAHRENHEIT

def main():
    """Main function to interact with the user and perform the temperature conversions"""

    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit=input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted:.1f}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        else:
            raise ValueError("Invalid unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}. Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()


