from collections import Counter
import random

# 1. Read the file and handle errors
try:
    with open("lotto.txt", "r", encoding="utf-8") as file:
        text = file.read()
        numbers = text.split()
except FileNotFoundError:
    print("The file 'lotto.txt' does not exist.")
    exit()

# 2. Convert strings to integers + validate numbers
numbers = [int(num) for num in numbers if num.isdigit() and 1 <= int(num) <= 45]

if len(numbers) < 6:
    print("There are not enough numbers in the file!")
    exit()

# 3. Frequency analysis → extract top 20 numbers
counter = Counter(numbers)
top_20 = counter.most_common(20)

print("Top 20 numbers based on historical data:")
for rank, (num, count) in enumerate(top_20, 1):
    print(f"Rank {rank:2d} → Number {num:2d} ({count} occurrences)")

top_numbers = [num for num, _ in top_20]  # List of numbers only

# 4. Generate 20 lottery sets!
print("\n" + "=" * 60)
print("              This Week's Recommended Lotto Sets (10)")
print("=" * 60)

for i in range(1, 21):
    # Randomly select 6 numbers from the top numbers (no duplicates)
    main_numbers = random.sample(top_numbers, 6)
    main_numbers.sort()
    
    # Bonus number (must not overlap with main numbers)
    bonus = random.randint(1, 45)
    while bonus in main_numbers:
        bonus = random.randint(1, 45)
    
    # Output
    print(f"Set {i:2d}: {main_numbers} + Bonus [{bonus}]")

print("=" * 60)
print("Good luck!")
