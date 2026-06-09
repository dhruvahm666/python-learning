file = open("myfile.txt", "w")
file.write("Hello! This is my first file.")
file.write("\nMy name is Dhruva.")
file.close()

print("File written successfully!")
file = open("myfile.txt", "r")
content = file.read()
file.close()

print("File contents:")
print(content)