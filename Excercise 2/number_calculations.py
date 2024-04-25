import sys
import random
import json

def main():
    if len(sys.argv) != 7:
        print("Please provide exactly six numbers as arguments.")
        sys.exit(1)
    
    # Convert command line arguments to integers
    numbers = list(map(int, sys.argv[1:]))
    
    # Display the choice menu
    print("Choose an operation to perform:")
    print("1. Subtraction")
    print("2. Multiplication")
    print("3. Random Number")
    print("4. Highest to Lowest")
    print("5. Lowest to Highest")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        # Subtraction
        perform_subtraction(numbers)
    elif choice == '2':
        # Multiplication
        perform_multiplication(numbers)
    elif choice == '3':
        # Random Number
        print("Random number from provided arguments:", random.choice(numbers))
    elif choice == '4':
        # Highest to Lowest
        print("Numbers sorted from highest to lowest:", sorted(numbers, reverse=True))
    elif choice == '5':
        # Lowest to Highest
        print("Numbers sorted from lowest to highest:", sorted(numbers))
    else:
        print("Invalid choice. Please run the script again with a valid option.")

def perform_subtraction(numbers):
    index1 = int(input("Enter the index (1-6) of the first number for subtraction: ")) - 1
    index2 = int(input("Enter the index (1-6) of the second number for subtraction: ")) - 1
    result = numbers[index1] - numbers[index2]
    print(f"Subtraction result ({numbers[index1]} - {numbers[index2]}):", result)

def perform_multiplication(numbers):
    index1 = int(input("Enter the index (1-6) of the first number for multiplication: ")) - 1
    index2 = int(input("Enter the index (1-6) of the second number for multiplication: ")) - 1
    result = numbers[index1] * numbers[index2]
    data = {
        f"InputNumber{i+1}": num for i, num in enumerate(numbers)
    }
    data["Multiplication result for 2 numbers selected by you"] = result
    with open('multiplication_result.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Multiplication result stored in 'multiplication_result.json'.")

if __name__ == "__main__":
    main()

