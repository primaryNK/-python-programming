input_file = None
input_string = None

input_file = open("testfile.txt", "r")

input_string = input_file.readline()
print(input_string, end="")