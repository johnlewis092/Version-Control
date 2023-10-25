def menu():
    print(
        "\nMenu\n"
        "-------------\n"
        "1. Encode\n"
        "2. Decode\n"
        "3. Quit\n"
    )

def encode(password):
    if len(password) == 8:
        encoded_password = ""
        for digit in password:
            new = (int(digit) + 3) % 10
            encoded_password += str(new)
        return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        new = (int(digit) - 3) % 10
        decoded_password += str(new)
    return decoded_password



def main():

    loop = True

    while loop:

        menu()

        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("You password has been encoded and stored!")

        if option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")

        if option == 3:
            loop = False

if __name__=="__main__":
    main()
