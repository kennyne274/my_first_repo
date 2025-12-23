![][스크린샷 2025-12-24 005806.png]

# BMI Calculator

LOG_FILE = "bmi.txt"
BANNER = "=" * 35

# Function to calculate BMI
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

# Main function
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

            # Save the name and result to the BMI file
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"{name}'s BMI is {bmi:.1f}, {status}\n")

            stop = input("Enter 'q' to quit: ")
            if stop.lower() == "q":
                break

        except ValueError:
            print("Please enter numeric values only.")
            continue

if __name__ == "__main__":
    main()
