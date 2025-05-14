input_file, output_file = None, None
input_string = ""

input_file = open("testfilefolder\data2", "rb")
output_file = open("testfilefolder\data3", "wb")

while True:
    input_string = input_file.read(1)
    if not input_string:
        break
    output_file.write(input_string)

input_file.close()
output_file.close()
