saved_password = ''


def encode(password):
    """Encodes a password and stores a given password"""
    global saved_password  # this function will access the variable in the global namespace
    saved_password_array = [(int(token) + 3) for token in password]  # turn every char into a digit and increase by 3

    saved_password = ''  # make sure previous password is removed
    for char in saved_password_array:

        new_char = str(char)

        if len(new_char) == 1:
            saved_password = ''.join([saved_password, new_char])  # convert list of digits back to password string

        else:
            saved_password = ''.join([saved_password, new_char[-1]])  # account for values that go over 9


def decode(encoded_password):
    """Decodes and returns the stored password"""
    decoded_password = ''  # initialize decoded password as empty string

    for char in encoded_password:  # iterate through encoded password for each character
        char = int(char)
        new_char = char - 3
        if new_char < 0:
            new_char += 10  # account for negative values
        decoded_password = ''.join([decoded_password, str(new_char)])

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
                  decode(saved_password) + '.')
        elif user_selection == '3':
            break
        else:
            print('Invalid selection.')


if __name__ == '__main__':
    main()
