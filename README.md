# assignment-4.2
task 1

file_name = "sample.txt"

try:
    with open(file_name, 'r') as file:
        print("--- Contents of {file_name} ---")
except FileNotFoundError:
    print("Error: The file '{file_name}' was not found.")

task 2========



FILENAME = "output.txt"

try:
    initial_content = input("Enter the text: ")
    with open(FILENAME, 'w') as file:
        file.write(initial_content + '\n')

    additional_content = "learning file handling in python."
    with open(FILENAME, 'a') as file:
        file.write(additional_content + '\n')

    file = open("output.txt", 'r+')
    reading_file =file.read()
    print(reading_file)
    file.close()
except IOError as e:
    print(f"Error: {e}")


