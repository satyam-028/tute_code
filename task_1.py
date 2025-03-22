try:
    # Open and read the text file 'sample.txt'
    with open('sample.txt', 'r') as file:
        # Read and print each line in the file
        for line in file:
            print(line, end='')  # The 'end' prevents double newlines from being printed

except FileNotFoundError:
    # Handle the case when the file doesn't exist
    print("Error: The file 'sample.txt' was not found.")