# Sample Python Code: Reading a file and processing its contents

# Function to read a file and count the number of words
def count_words_in_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire content of the file
            words = content.split()  # Split the content into a list of words
            word_count = len(words)  # Count the number of words
            print(f"Total number of words in the file: {word_count}")
    except FileNotFoundError:
        print("The file was not found. Please check the filename.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Sample usage
filename = "sample.txt"  # Make sure to have a sample.txt file in the same directory or provide the correct path
count_words_in_file(filename)
