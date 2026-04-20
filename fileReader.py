# 1. Writing data to a file (creates/overwrites file)
file = open("demo.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("Python file handling example.\n")
file.close()   # Proper closing

# 2. Reading the file
file = open("demo.txt", "r")
print("Content after writing:\n")
print(file.read())
file.close()

# 3. Appending additional content
file = open("demo.txt", "a")
file.write("This line is added later.\n")
file.close()

# 4. Reading again after appending
file = open("demo.txt", "r")
print("\nContent after appending:\n")
print(file.read())
file.close()