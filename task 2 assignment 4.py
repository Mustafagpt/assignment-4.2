

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



