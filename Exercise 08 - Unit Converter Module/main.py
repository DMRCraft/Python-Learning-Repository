# Main File
from converter import *

def main():
    miles_per_hour = km_to_miles(100)
    km_per_hour = miles_to_km(miles_per_hour)
    print(f"{miles_per_hour:.2f}mph")
    print(f"{km_per_hour:.2f}km/h")

if __name__ == "__main__":
    main()
