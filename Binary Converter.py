#This Python program is used to convert from decimal to binary.
def Binary_Converter():
    print("Converting Decimal to binary")
    # Convert Decimal to binary
    while True:     #While will be used to keep a loop going
        try:   #Try will check if the user as inputted a number
            decimal = int(input("Please enter a decimal number: "))            #Decimal is a variable that will store a int value
            break           #Break will end the loop
        except ValueError:     #except ValueError is used to check if the user as inputted a number if not it will run into except and tell the user to input the number again
            print("Please enter a valid number.")     #Print is telling the user to enter a number
    binary = bin(decimal)   #Transforms the decimal number into binary
    print("Binary: "+binary) #printing the binary number
Binary_Converter() #running the function