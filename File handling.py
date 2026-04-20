# 1. Writing to a file (creates file if not exists)
file = open("example.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("File handling in Python.\n")
file.close()

# 2. Reading from the file
file = open("example.txt", "r")
content = file.read()
print("File Content after writing:")
print(content)
file.close()

# 3. Appending to the file
file = open("example.txt", "a")
file.write("This line is appended later.\n")
file.close()

# 4. Reading again after appending
file = open("example.txt", "r")
content = file.read()
print("\nFile Content after appending:")
print(content)
file.close()