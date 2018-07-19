def calculate(temp_type, temperature):
    if temp_type == 'c':
        return print(str((temperature * (9/5)) + 32) + '˚ F')
    elif temp_type == 'f':
        return print(str((temperature - 32) * (5/9)) + '˚ C')
    else:
        print("I dunno how you got here but cool, let me know how")
        get_proper_input(temperature)

def get_proper_input(temp):
    type = input("C or F?\n")
    type = type.lower()
    if type == 'c' or type == 'f':
        calculate(type, temp)
    else:
        get_proper_input(temp)
temp = input("Enter a temperature\n");
temp = float(temp);

get_proper_input(temp)
