input_int = int(input())
string = "#"

for _i in range(input_int):
    new_string = string.center(input_int * 2, " ")
    string += "##"
    print(new_string)
