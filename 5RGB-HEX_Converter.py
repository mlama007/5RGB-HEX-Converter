"""This program uses Bitwise operators that can convert RGB values to Hexadecimal (hex) values, and vice-versa."""

def  rgb_hex():
    invalid_msg = "Invalid value entered."
    #RED
    red = int(raw_input("Enter the Red (R) Value: "))
    if red < 0 or red > 255:
        print invalid_msg
        return
    #GREEN
    green = int(raw_input("Enter the Green (G) Value: "))
    if green < 0 or red > 255:
        print invalid_msg
        return
    #BLUE
    blue = int(raw_input("Enter the Blue (B) Value: "))
    if blue < 0 or red > 255:
        print invalid_msg
        return
    val = (red << 16) + (green << 8) + blue
    print "Hex value: %s" % (hex(val)[2:]).upper()

def hex_rgb():
    """Prints RGB code from hex code.
    Args:
        None
    Returns:
        None. Prints RGB of hex
    Raises:
        None
    """
    #User gives hex value
    hex_val = raw_input("Enter the hexadecimal value: ")
    if len(hex_val) != 6:
        print "Invalid value entered."
        return
    else:
        hex_val = int(hex_val, 16)
    #convert hex to RGB
    two_hex_digits = 2**8
    #blue
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    #green
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    #red
    red = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    print "Red: %s Green: %s Blue: %s" % (red, green, blue)

def convert():
    while True:
        #User states what they want to do
        option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
        if option == "1":
            print "RGB to Hex..."
            rgb_hex()
        elif option == "2":
            print "Hex to RGB..."
            hex_rgb()
        elif option == "X" or option == "x":
            break
        else:
            print "Error."


convert()