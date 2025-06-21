def temper():
    print("""
          Temperature!
          Just a unit is fine_""")
    first = input("From: ").lower()
    second = input("To: ").lower()

    if first == "c" and second == "f":
        value = float(input("Value: "))
        temp = (value * 9/5) + 32
        print(f"fahrenheit -:- {temp}F")

    elif first == "f" and second == "c":
        value = float(input("Value: "))
        temp =  (value - 32) * 5/9
        print(f"Celsius -:- {temp}C")

    elif first == "c" and second == "k":
        value = float(input("Value: "))
        temp =  value + 273.15
        print(f"Kelvin -:- {temp}K")


def length():

    def convert(first, second, value):
        file_dict = {
            "mm": 0.001,
            "cm": 0.01,
            "m": 1,
            "km": 1000,
            "in": 0.0254,
            "ft": 0.3048,
            "yd": 0.9144,
            "mi": 1609.34
            }              # got it from you....
        
        # Turning value to meter
        meter = value * file_dict[first]

        # Turning meter to your unit
        result = meter / file_dict[second]

        return f"{value} {first} = {result} {second}"
    

    print("""
          Length!
          Just a unit is fine_""")
    from_unit = input("From: ").lower()
    to_unit = input ("To: ").lower()
    value = float(input("Value: "))
    print(convert(from_unit, to_unit, value))

def weight():

    def convert(first, second, value):
        dict_key_kg = {
                "mg": 0.000001,
                "g": 0.001,
                "kg": 1,
                "t": 1000,
                "oz": 0.02835,
                "lb": 0.4536,
                "st": 6.3503,
                "ton": 907.18
        }

        kilogram = value * dict_key_kg[first]

        result = kilogram / dict_key_kg[second]
        
        return f"{value} {first} = {result} {second}"
    

    print("""
          Weight!
          Just a unit is fine_""")
    from_unit = input("From: ").lower()
    to_unit = input ("To: ").lower()
    value = float(input("Value: "))
    print(convert(from_unit, to_unit, value))

    
def main():
    while True:
        print("""
    You want to convert your units: 
        1. Temperature
        2. Weight
        3. Length
    Your choice!
    """)
        choice = input("Please enter your choice: ")

        match choice:
            case "1":
                temper()
            case "2":
                weight()
            case "3":
                length()
            case _:
                print("Invalid input, exiting....")
                break
            
                

if __name__ == "__main__":
    main()