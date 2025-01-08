filename1 = input("Enter Source file name: ")
with open(filename1, 'r') as file1:
    lines = file1.readlines()

filename2 = input("Enter destination file name: ")
with open(filename2, 'w') as file2:
    for i in range(len(lines)):
        if i % 2 != 0:


            file2.write(lines[i])

print(f"Odd lines copied to '{filename2}'.")
