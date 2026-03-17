"""
Exercise 3 — Loop That Builds Something
Multiplication table generator with input validation.
Bonus: prints tables for ALL numbers 1-12 in a single run.
"""


def print_table(n):
    """Print a clean, right-aligned multiplication table for n."""
    print(f"\n--- Multiplication Table for {n} ---")
    for i in range(1, 13):
        product = n * i
        print(f"  {n:>2} x {i:>2} = {product:>4}")


def main():
    while True:
        user_input = input("\nEnter a number (1-12), or 'all' for every table, or 'q' to quit: ").strip()

        if user_input.lower() == "q":
            print("Goodbye!")
            break

        if user_input.lower() == "all":
            for num in range(1, 13):
                print_table(num)
            continue

        try:
            number = int(user_input)
        except ValueError:
            print("That's not a valid number. Try again.")
            continue

        if 1 <= number <= 12:
            print_table(number)
        else:
            print(f"{number} is out of range. Please enter a number between 1 and 12.")


if __name__ == "__main__":
    main()
