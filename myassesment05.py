# Sample Python Code: Working with a list of numbers

# Function to calculate the sum, average, and sort a list of numbers
def process_numbers(numbers):
    # Calculate the sum
    total_sum = sum(numbers)
    
    # Calculate the average
    average = total_sum / len(numbers) if numbers else 0
    
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Print the results
    print(f"Original list: {numbers}")
    print(f"Sum of numbers: {total_sum}")
    print(f"Average of numbers: {average}")
    print(f"Sorted list: {sorted_numbers}")

# Sample usage
numbers = [12, 5, 3, 8, 15, 9, 21, 7]  # A list of numbers
process_numbers(numbers)
