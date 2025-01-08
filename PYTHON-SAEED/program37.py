filename = input("Enter file name: ")
try:
    with open(filename, 'r') as file1:
        lines = file1.readlines()
    lines = [line.strip() for line in lines]
    print("Lines from the file:", lines)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
