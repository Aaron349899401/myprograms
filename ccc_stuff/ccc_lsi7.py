def rotate(string_list, integer):
    if not string_list:
        return ""
    
    integer = integer % len(string_list)  # avoid unnecessary loops
    
    return "".join(string_list[-integer:] + string_list[:-integer])

string = input("Enter your string: ")
string_list = [x.strip() for x in string]
integer = int(input("Enter your integer: "))

print(rotate(string_list, integer))