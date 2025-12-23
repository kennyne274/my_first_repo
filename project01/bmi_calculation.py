# Simple BMI Calculator

LOG_FILE = "bmi.txt"
BANNER = "=" * 35


# Declare a function for BMI calculation
def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
       
    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    return bmi, status


# Declare the main function
def main():
    print("Please enter numbers only. Decimals are allowed.")
    # Repeat until the user enters 'q'
    while True:

        try:
            name = input("Enter your name: ").strip()
            height = float(input("Enter your height in meters: "))
            weight = float(input("Enter your weight in kilograms: "))

            bmi, status = calculate_bmi(height, weight)

            print(BANNER)
            print(f"{name}'s BMI: {bmi:.1f}, {status}")

            # Write the name and result to the BMI log file
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"{name}'s BMI is {bmi:.1f}, {status}\n")

            stop = input("Enter 'q' to quit: ")
            if stop.lower() == "q":
                break

        except ValueError:
            print("Please enter numeric values only.")
            continue


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()





