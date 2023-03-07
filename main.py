def encode(password):
    encoded_pw = ""
    for i in range(0,len(password)):
        num = int(password[i])
        num += 3
        encoded_pw += str(num)
    return encoded_pw

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1.Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 3:
            break
        elif option == 2:
            pass
        elif option == 1:
            pw = input("Please enter your password to encode: ")
            print("\nYour password has been encoded and stored!")