file_name = "sample.txt"

try:
    with open(file_name, 'r') as file:
        print("--- Contents of {file_name} ---")
except FileNotFoundError:
    print("Error: The file '{file_name}' was not found.")