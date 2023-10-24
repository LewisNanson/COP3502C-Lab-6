saved_password = ''
saved_password_list = []

def encode(password):
    """Encodes a password and stores a given password"""
    global saved_password  # this function will access the variable in the global namespace
    global  saved_password_list
    saved_password_list = [(int(token) + 3) for token in password]  # turn every character into a digit and increase by 3
    saved_password = ''.join(str(char) for char in saved_password_list)  # convert list of digits back to password string


def decode(encoded_password):
    """Decodes and returns the stored password"""
    decoded_password = ''  # initialize decoded password as empty string

    for char in encoded_password:  # iterate through encoded password for each character
        char = int(char)
        new_char = char - 3
        decoded_password += str(new_char)

    return decoded_password


def main():
    while True:
        print('Menu')
        print('-' * 13)
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')

        user_selection = input('Please enter an option: ')
        if user_selection == '1':
            user_password = input('Please enter your password to encode: ')
            encode(user_password)
            print('Your password has been encoded and stored!')

        elif user_selection == '2':
            print('The encoded password is ' + saved_password + ', and the original password is ' +
                  decode(saved_password_list) + '.')
        elif user_selection == '3':
            break
        else:
            print('Invalid selection.')


if __name__ == '__main__':
    main()
