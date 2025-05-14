input_file = None
input_list, input_string = [], ""

input_file = open("testfilefolder\data1", "r", encoding="utf-8")
output_file = open("testfilefolder\data2", "w", encoding="utf-8")

security_key = 123

while True:
    input_string = input_file.readline()
    if not input_string:
        break

    output_string = ""
    for i in range(len(input_string)):
        char = input_string[i]
        char_num = ord(char)
        char_num = char_num + security_key
        char2 = chr(char_num)
        output_string += char2
    output_file.write(output_string)

input_file.close()
output_file.close()