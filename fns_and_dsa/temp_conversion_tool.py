FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_FAHRENHEIT = 32

def convert_to_celsius(fahrenheit):
    """Converts a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts a Celsius temperature to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Main function to interact with the user and perform the temperature conversions"""

    try:
        temperature= input("Enter the temperature to convert: ")

        if not temperature.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        temperature = float(temperature)
        unit=input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted:.1f}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted:.1f}°C")
        else:
            raise ValueError("Invalid unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
